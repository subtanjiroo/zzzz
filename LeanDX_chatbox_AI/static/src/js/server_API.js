/** @odoo-module **/

export async function sendMessage(component) {
    const messageInput = document.getElementById('message_input'); // Lấy ô nhập văn bản bằng getElementById
    const chatInput = document.getElementById('CHAT_INPUT');

    component.messageState.message = messageInput.value; // *****Save Value From TextArea*******

    const message = component.messageState.message; // Lấy giá trị tin nhắn từ messageState
    if (message) {
        try {
            const response = await component.env.services.rpc('/LeanDX_chatbox_AI/chat', { message: message });
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
            component.messageState.message = '';
            messageInput.style.height = '30px'; // Đặt lại chiều cao ban đầu cho textarea
            chatInput.style.height = '4em'; // Đặt lại chiều cao ban đầu cho phần chat input

        } catch (error) {
            console.error("Error sending message:", error);
        }
    }
}
