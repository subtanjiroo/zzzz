/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, xml, useState } from "@odoo/owl";
import { sendMessage } from "./server_API";
class CustomField extends Component {
    static template = xml`
        <div id="chatbox_wrapper">
            <!-- Sidebar -->
            <div id="sidebar" t-att-class="state.showSidebar ? 'show' : ''">
                <div class="SibarMenu">
                    <div id="sidebar_toggle" t-on-click="toggleSidebar">☰</div>
                    <div id="New_session" t-on-click="NewSession">+</div>
                </div>
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
                    <div class="DRD">
                    <!-- Dropdown Upload Options -->
                    <div id="upload_dropdown" t-att-class="state.showDropdown ? 'show' : 'hidden'">
                        <div class="upload_box">Testing upload file 1</div>
                        <div class="upload_box">Testing upload file 2</div>
                        <div class="upload_box">Testing upload file 2</div>
                    </div>
                    <button name="Upload" type="button" id="upload_button" t-on-click="UploadHandle">
                        <i class="fa-solid fa-paperclip"></i>
                    </button>
                    </div>
                    <textarea t-on-keydown="handleKeyDown" id="message_input" placeholder="Type your message..." t-model="messageState.message" t-ref="messageInput"></textarea>
                    <button name="send-message" type="button" id="send_button" t-on-click="sendMessageHandler">Send</button>
                </div>
            </div>
        </div>
    `;

    setup() {
        this.state = useState({
            showSidebar: true,
            showDropdown: false, // Trạng thái hiển thị của dropdown
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
    NewSession(){
        //New session
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
        // Hiển thị hoặc ẩn dropdown khi nhấn vào nút Upload
        this.state.showDropdown = !this.state.showDropdown;
    }

    sendMessageHandler() {
        sendMessage(this);  // Sử dụng hàm sendMessage được import
    }
}

registry.category("fields").add("custom_char", {
    component: CustomField,
    supportedTypes: ["char"],
});
