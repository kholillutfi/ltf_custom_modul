# -*- coding: utf-8 -*-
{
    'name': "Sales & Invoice Customize by ltf",

    'summary': "Sales & Invoice Customize",

    'description': """
Sales & Invoice Customize
    """,

    'author': "M. Kholil Lutfi",
    'category': 'accounting,sales',
    'version': '17.0.1.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','account','sale','sale_management','ferp_so_po_printing_template'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move_views.xml',
        'views/sale_views.xml',
        'reports/inv_template_inherit.xml',
    ],
    'installable': True,
    'auto_install': True,
}

