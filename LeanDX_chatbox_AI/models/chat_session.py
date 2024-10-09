
'''
Author: Thinh dep trai
Model Description:
    These model is used to manage the chat history for the user.
        Chat history is bound to user (not partner) as it easier to get the user uid than the partner id.
'''


from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class User(models.Model):
    """
        This model is the user model
            We override the res.users model to add the chat history
            Note: The chat history is a one to many relationship with the chat message
    """
    _inherit = 'res.users'
    chat_session_ids = fields.One2many('leandx.ai.session', 'user_id')


    def get_chat_history(self):
        """
            This function is used to get the chat history of the user
                We return list of object of the chat history with the history name and the history id
                    The name is for displaying.
                    The id is for getting the chat message (for requesting).
        """
        _logger = logging.getLogger(__name__)
        chat_session_ids = self.env['leandx.ai.session'].search([('user_id','=',self.id)])
        _logger.error(chat_session_ids)
        return [{"history_name":history.name, "id":history.id} for history in chat_session_ids]


class Chat_session(models.Model):
    _name = 'leandx.ai.session'
    _description = 'Chat'
    """
        This model is the chat history model
            We use this model to store the chat history of the user
            Note: The chat history is a one to many relationship with the chat message
            The name of the message might be interpreted by open AI. (just like the AI chat system).
    """
    name = fields.Char(string='Name')
    chat_message_ids = fields.One2many('leandx.ai.session.message', 'chat_session_id', string='Chat Messages')
    user_id = fields.Many2one('res.users', string='User')

    def get_message(self):
        """
            This function is used to get the message of the chat history
                We return list of object of the chat message with the message and the role
                    The message is the message that the user sent or from the assistant.
                    The role is the role of the user (user or assistant)
                Note that the text we store here is markdown text, as GPT given the markdown text.
        """
        return [{"message":message.message, "role":message.role} for message in self.chat_message_ids]


    def input_message(self,message,role):
        """
            This function is used to input the message to the chat history
                We input the message and the role to the chat history
            :param
                message: the message that the user sent or from the assistant
                role: the role of the user (user or assistant) (1 for user and 0 for assistant)
        """
        self.env['leandx.ai.session.message'].sudo().create({
            'message':message,
            'role': role,
            'chat_session_id':self.id
        })



class chat_message(models.Model):
    _name = 'leandx.ai.session.message'
    _description = 'Chat Message'
    """
        This model is the chat message model
            We use this model to store the chat message of the user
            Note: The chat message is a one to many relationship with the chat history
            The message is the message that the user sent.

            The role is the role of the user (user or assistant)
                Note the role is used to distinguish the user and the assistant.
    """
    role = fields.Selection([
        ('1', 'User'),
        ('0', 'Assistant'),
    ], string='Role', required=True, default='1')
    message = fields.Text(string='Message', required=True)
    chat_session_id = fields.Many2one('leandx.ai.session', string='Chat History')



