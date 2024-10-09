'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields


class wizard_pop_up_pdf(models.TransientModel):
    _name = 'wizard.upload.pdf'
    _description = ''

    name = fields.Char(string='Name')
    file = fields.Binary(string='File')
    partner_id = fields.Many2one('res.partner', string='Customer')



