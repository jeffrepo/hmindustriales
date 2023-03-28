# -*- coding: utf-8 -*-
{
    'name': "HM Industriales",

    'summary': """ HM Industriales """,

    'description': """
       HM Industriales
    """,

    'author': "STECHNOLOGIES",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['sale','base','l10n_mx_edi','point_of_sale'],

    'data': [
        'views/sale_order_views.xml',
        'report/ir_actions_report_templates.xml',
        'views/res_partner_view.xml',
    ],
    'assets':{
        'point_of_sale.assets': [
            'hmindustriales/static/src/js/Screens/ProductScreen.js',
        ],
        'web.assets_qweb':[
        ],
        'web.assets_backend': [
        ],
    },
    'qweb': [
    ],
    'license': 'LGPL-3',
}
