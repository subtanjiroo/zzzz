'''
Author: Thinh dep trai
Model Description: 
'''

import odoo
from odoo import http
from odoo.http import Controller, route, request
import logging
_logger = logging.getLogger(__name__)
import os

from odoo import models, fields


class document_loader(http.Controller):

    @http.route('/LeanDX_chatbox_AI/document', type='json', auth='public')
    def get_document(self):
        """
            json response{
                 "customer_data" : {"customer_name": [list document]},


            }
        :param message:
        :return:
        """
        _logger.info(f"concact document")

        #return all the customer documents
        customer_data = {}
        #query the database for all the customers
        customers = request.env['res.partner'].sudo().search([])
        for customer in customers:
            #get the documents for the customer
            documents = request.env['leandx.chatbox.ai.document'].search([('partner_id','=',customer.id)])
            # if(len(documents)>0):
            _logger.info(f"Customer data: {customer.name}")
            customer_data[customer.name] = [doc.name for doc in documents]

        _logger.info(f"Customer data: {customer_data}")
        return {"customer_data": customer_data, "status": "success"}

