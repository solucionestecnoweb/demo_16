# -*- coding: utf-8 -*-
{
    'name': "List Contact Sale",

    'summary': """Module to view the Contacts list""",

    'description': """List Contact Sale""",

    'license': 'OPL-1',
    'author': "Ing.MarilynMillan",
    'website': "www.odoo.com",

    'category': 'Custom Modules/Tech Training',

    'depends': ['base', 'contacts', ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}