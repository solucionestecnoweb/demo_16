# -*- coding: utf-8 -*-
{
    'name': "ListContact",

    'summary': """List Contact Sale""",

    'description': """Module to view the Contacts list""",

    'license': 'OPL-1',
    'author': "Ing.MarilynMillan",
    'website': "www.odoo.com",

    'category': 'Custom Modules/Tech Training',

    'depends': ['base', 'contacts', 'sale_management'],

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