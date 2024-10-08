'''
Author: Thinh dep trai
Model Description: 
'''
from odoo import http
from odoo.http import Controller, route, request
import logging
import json
_logger = logging.getLogger(__name__)

class ChatHistoryController(http.Controller):
    @http.route('/LeanDX_chatbox_AI/chat/history', type='json', auth='public')
    def get_chat_session_list(self):
        """
            json{
                "uid" : user's id (int)
            }
        :param uid:
        :return:
            json{
                "list_session": [{"name": "Session 1", "id": 1},{"name": "Session 2", "id": 2}],
                "status": 200
            }
        """
        data = json.loads(request.httprequest.data)  
        return {"list_session":[{"name": "Session 1", "id": 1},{"name": "Session 2", "id": 2}],"data":data,"status":200}

        # user = request.env['res.users'].browse({'id':uid})[0]
        # list_history = list(user.get_chat_history())
        # _logger.error(list_history)
        #
        # return {"list_history":list_history,"status":200}






