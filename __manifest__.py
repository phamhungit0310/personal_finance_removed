# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Personal Finance',
    'version': '0.0',
    'category': 'Accounting',
    'author': 'Pham Hung',
    'support': 'phamhungit0310@gmail.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/personal_finance_menus.xml',
        'views/money_flow_views.xml',

        'report/money_flow_report.xml',
        ],
    'installable': True,
    'application': True,
    'assets': {
        
    },
    'license': 'LGPL-3',
    'price': -9,
    'currency': 'USD',
}
