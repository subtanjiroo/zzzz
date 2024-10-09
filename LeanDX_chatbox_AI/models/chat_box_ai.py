from odoo import models, fields, api

class Chatbox(models.TransientModel):
    _name = 'leandx.ai.chatbox'
    _description = 'Chat Message'

    session = fields.Many2one('leandx.ai.session', string='Session')
    name = fields.Char(string='Name')

