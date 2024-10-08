'''
Author: Thinh dep trai
Model Description:
    These model is used to manage the documents for the customer.
        Note that the document here is not the file itself but the information about the file.
        Also note that, the document is used in RAG system.
'''

from odoo import models, fields


class DocumentManaging(models.Model):
    _name = 'leandx.chatbox.ai.document'
    _description = ''

    name = fields.Char(string='Name', required=True, help='Enter the name for the document')
    description = fields.Text(string='Description', help='Enter the description for the document')
    file_type = fields.Selection([
        ('pdf', 'PDF'),
        ('docx', 'DOCX'),
        ('csv', 'CSV'),
        ('xlsx', 'XLSX'),
    ], string='File Type', required=True, help='Choose the file type for the document')

    file_path = fields.Char(string='File Path', help='Enter the file path for the document')
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, help='Choose the customer for the document')

class Customer(models.Model):
    """
        Overide the Customer model to add documents management.
            #document list.
        Note that we don't want to store the file in the database because it can be large (ir.attachment is not a good idea).
    """
    _inherit = 'res.partner'

    document_ids = fields.One2many('leandx.chatbox.ai.document', 'partner_id', string='Documents')
