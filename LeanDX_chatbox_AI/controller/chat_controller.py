from odoo import http
from odoo.http import Controller, route, request
import json

class ChatController(http.Controller):
    @http.route('/LeanDX_chatbox_AI/chat', type='json', auth='public', methods=['POST'])
    def chat(self):
        # Nhận dữ liệu JSON từ yêu cầu
        # Dùng request.httprequest để lấy dữ liệu và phân tích từ JSON
        data = json.loads(request.httprequest.data)  

        return {
            "response": "Hello",
            "role": "assistant",
            "data": data,  # Trả về dữ liệu nhận được từ yêu cầu
        }
