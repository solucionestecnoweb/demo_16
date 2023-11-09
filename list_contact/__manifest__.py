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
        'views/sale_order.views.xml',
        'views/sale_document_inherit_list.xml',

    ],

    'application': True,
}