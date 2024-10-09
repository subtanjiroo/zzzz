{
    'name': 'LeanDX - Chatbox AI',
    'version': '1.0',
    'depends': ['base', 'base_setup','web'],
    'data': [
        'security/resgroup.xml',
        'security/ir.model.access.csv',
        
        'views/chatbox_view.xml',
        'data/chatgpt_model_data.xml',
        'views/res_config_settings_views.xml',
        'views/session.xml',
        'views/message.xml',
        'views/menu_items.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'LeanDX_chatbox_AI/static/src/js/chatbox_script.js',
            'LeanDX_chatbox_AI/static/src/js/server_API.js',
            'LeanDX_chatbox_AI/static/src/css/chatbox_style.css',
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css',

        ],
    },
    'installable': True,
    'application': True,
    "license": "LGPL-3"
}
