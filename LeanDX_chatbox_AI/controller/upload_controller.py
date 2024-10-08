import odoo
from odoo import http
from odoo.http import Controller, route, request
from ..models.RAG_system.RAG import RAG
import base64
import logging
_logger = logging.getLogger(__name__)
import os








class UploadController(http.Controller):
    @http.route('/LeanDX_chatbox_AI/upload/pdf',type='json', auth="public", methods=['POST'],csrf=False)
    def upload_pdf(self, file_name,file_type,file_size,customer,file):

        _logger.info(f"File received: {file_name}")
        # base64_data = kw['attachments'].split(",")[1]

        user_folder = "/tmp/odoo/LeanDX_chatbox_AI/documents/"+customer
        #check if the folder exists
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        #save the file
        with open(f"{user_folder}/{file_name}", "wb") as f:
            f.write(base64.b64decode(file))
        ICP = request.env['ir.config_parameter'].sudo()
        #store the file path in the database
        API_KEY = ICP.get_param('LeanDX_chatbox_AI.openai_api_key')
        RAG_model = RAG(API_KEY)
        RAG_model.store_embedding_pdf(file_name, f"{user_folder}/{file_name}")
        _logger.info(f"File saved: {file_name}")
        return {"status": "success", "message": "File received successfully"}

    # @http.route('/LeanDX_chatbox_AI/upload/docx', type='json', auth='user')
    # def upload_docx(self, message):
    #     """
    #         json{
    #
    #         }
    #     :param message:
    #     :return:
    #     """
    #
    #     pass
    # @http.route('/LeanDX_chatbox_AI/upload/csv', type='json', auth='user')
    # def upload_csv(self, message):
    #     """
    #         json{
    #
    #         }
    #     :param message:
    #     :return:
    #     """
    #
    #     pass
    # @http.route('/LeanDX_chatbox_AI/upload/xlss', type='json', auth='user')
    # def upload_pdf(self, message):
    #     """
    #         json{
    #
    #         }
    #     :param message:
    #     :return:
    #     """
    #     pass
    #
    #
