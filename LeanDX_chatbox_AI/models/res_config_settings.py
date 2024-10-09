

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    openapi_api_key = fields.Char(string="API Key", help="Provide the API key here", config_parameter="LeanDX_chatbox_AI.openai_api_key")
    chatgpt_model_id = fields.Many2one('chatgpt.model', 'ChatGPT Model', ondelete='cascade',  config_parameter="LeanDX_chatbox_AI.chatgp_model")



from odoo import fields, models


class ChatGPTModel(models.Model):
    _name = 'chatgpt.model'
    _description = "ChatGPT Model"

    name = fields.Char(string='ChatGPT Model', required=True)
