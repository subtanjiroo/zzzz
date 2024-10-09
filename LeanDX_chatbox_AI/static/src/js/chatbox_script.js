/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, xml, useState } from "@odoo/owl";

class CustomField extends Component {
    static template = xml`
        <div id="chatbox_wrapper">
            <!-- Sidebar -->
            <div id="sidebar" t-att-class="state.showSidebar ? 'show' : ''">
                <div id="sidebar_toggle" t-on-click="toggleSidebar">☰</div>
                <ul id="task_list">
                    <li t-on-mouseenter="handleMouseEnter" t-on-click="HistoryBar" t-on-mouseleave="handleMouseLeave" t-foreach="state.tasks" t-as="task" t-key="task">
                        <span t-esc="task"></span>
                    </li>
                </ul>
            </div>

            <!-- Main Chatbox Area -->
            <div id="chatbox">
                <div class="sidebar2">
                    <div id="sidebar_toggle2" t-on-click="toggleSidebar" t-att-class="state.showSidebar ? 'hidden' : ''">☰</div>
                </div>
                <div id="messages">
                    <!-- Các tin nhắn sẽ được thêm vào đây -->
                </div>
                <div id="CHAT_INPUT">
                    <button name="Upload" type="button" id="upload_button" t-on-click="UploadHandle">
                        <i class="fa-solid fa-paperclip"></i>
                    </button>                    
                    <textarea t-on-keydown="handleKeyDown" id="message_input" placeholder="Type your message..." t-model="messageState.message" t-ref="messageInput"></textarea>
                    <button name="send-message" type="button" id="send_button" t-on-click="sendMessage">Send</button>
                </div>
            </div>
        </div>
    `;

    setup() {
        this.state = useState({
            showSidebar: true,
            tasks: [] // Sử dụng state để lưu danh sách task
        });
        this.messageState = useState({ message: "" }); // State lưu trữ tạm thời tin nhắn
        console.log(this.env.searchModel._context.uid);
        // Gọi RPC
        this.loadTasks();
    }

    async loadTasks() {
        try {
            const response = await this.env.services.rpc('/LeanDX_chatbox_AI/chat/history', { uid: this.env.searchModel._context.uid });
            console.log("day la res: ", response);
            // Kiểm tra xem list_session có tồn tại trong response không
            if (response.list_session) {
                // Cập nhật this.state.tasks bằng danh sách từ list_session
                this.state.tasks = response.list_session.map(session => session.name);
                console.log(this.state.tasks);
            }
        } catch (error) {
            console.error("Có lỗi xảy ra khi lấy dữ liệu:", error);
        }
    }

    toggleSidebar() {
        this.state.showSidebar = !this.state.showSidebar;
    }

    handleMouseEnter(event) {
        event.target.style.backgroundColor = '#f0f0f0'; // Hiển thị hiệu ứng khi hover vào
    }

    handleMouseLeave(event) {
        event.target.style.backgroundColor = ''; // Bỏ hiệu ứng khi rời chuột
    }

    handleKeyDown(event) {
        const messageInput = document.getElementById('message_input');
        const chatInput = document.getElementById('CHAT_INPUT');

        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault(); // Ngăn chặn hành động mặc định (xuống dòng)
            this.sendMessage(); // Gọi hàm gửi tin nhắn
        } else if (event.key === 'Enter' && event.shiftKey) {
            event.preventDefault(); // Ngăn chặn hành động mặc định
            const cursorPos = messageInput.selectionStart; // Lưu vị trí con trỏ
            const currentValue = messageInput.value; // Lấy giá trị hiện tại
            // Chèn ký tự xuống dòng tại vị trí con trỏ
            messageInput.value = currentValue.slice(0, cursorPos) + "\n" + currentValue.slice(cursorPos);
            messageInput.selectionStart = messageInput.selectionEnd = cursorPos + 1; // Cập nhật vị trí con trỏ
        }

        // Cập nhật chiều cao của textarea chỉ khi scrollHeight > 30px
        if (messageInput.scrollHeight > 30) {
            messageInput.style.height = 'auto'; // Đặt chiều cao về auto để tự điều chỉnh
            messageInput.style.height = messageInput.scrollHeight + 'px'; // Cập nhật chiều cao dựa trên scrollHeight
            chatInput.style.height = (messageInput.scrollHeight + 10) + 'px'; // Cập nhật chiều cao dựa trên scrollHeight
        }
    }

    async UploadHandle() {
        // Logic Upload File
    }

    async sendMessage() {
        const messageInput = document.getElementById('message_input'); // Lấy ô nhập văn bản bằng getElementById
        const chatInput = document.getElementById('CHAT_INPUT');

        this.messageState.message = messageInput.value; // *****Save Value From TextArea*******

        const message = this.messageState.message; // Lấy giá trị tin nhắn từ messageState
        if (message) {
            try {
                const response = await this.env.services.rpc('/LeanDX_chatbox_AI/chat', { message: message });
                console.log(response);
                // Tạo div chứa tin nhắn của người dùng
                const client_message = document.createElement('div');
                client_message.className = 'client_message';
                client_message.textContent = message;

                // Sử dụng CSS để hiển thị văn bản có ký tự xuống dòng
                client_message.style.whiteSpace = 'pre-line';

                const messagesContainer = document.getElementById('messages');
                messagesContainer.appendChild(client_message);

                // Tạo div chứa tin nhắn từ server
                const server_message = document.createElement('div');
                server_message.className = 'server_message';

                // Kiểm tra và hiển thị tin nhắn từ server đúng định dạng
                server_message.textContent = response.response;
                server_message.style.whiteSpace = 'pre-line';

                messagesContainer.appendChild(server_message);
                messagesContainer.scrollTo(0, messagesContainer.scrollHeight);

                // Reset tin nhắn sau khi gửi
                this.messageState.message = '';
                messageInput.style.height = '30px'; // Đặt lại chiều cao ban đầu cho textarea
                chatInput.style.height = '4em'; // Đặt lại chiều cao ban đầu cho phần chat input

            } catch (error) {
                console.error("Error sending message:", error);
            }
        }
    }
}

registry.category("fields").add("custom_char", {
    component: CustomField,
    supportedTypes: ["char"],
});
