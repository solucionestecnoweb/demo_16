# -*- coding: utf-8 -*-
{
    'name': "camposmc",

    'summary': """Modulo para crear campos""",

    'description': """Aqui se crearan varios campos en especifico para PandaID""",

    'license': 'OPL-1',
    'author': "BetolotiPanda",
    'website': "www.odoo.com",

    'category': 'Custom Modules/Tech Training',

    'depends': ['base', 'helpdesk', 'contacts', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}