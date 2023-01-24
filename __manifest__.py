# -*- coding: utf-8 -*-
{
    'name': "tdv_commissions",

    'summary': """
       Service commissions and technical support
    """,

    'author': "3DVision, C.A",
    'website': "https://www.3dvisionve.com",

    'category': 'Uncategorized',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'account', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
