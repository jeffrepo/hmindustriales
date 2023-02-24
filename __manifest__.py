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

    'depends': ['sale','base','l10n_mx_edi'],

    'data': [
        'views/sale_order_views.xml',
        'report/ir_actions_report_templates.xml',
        'views/res_partner_view.xml',
    ],
    'assets':{
        'point_of_sale.assets': [
            #'pos_technotrade/static/src/js/**/*.js',
            #'pos_technotrade/static/src/xml/**/*.xml',
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
