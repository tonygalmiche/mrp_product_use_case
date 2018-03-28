# -*- coding: utf-8 -*-
# Copyright 2018 Tony Galmiche - InfoSaône <tony.galmiche@infosaone.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'MRP Product Use Case',
    'version': '10.0.1.0.0',
    'category' : 'mrp',
    'description': """
MRP Product Use Case
===================================================
""",
    'author' : 'Tony Galmiche - InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'license': 'AGPL-3',
    'depends'    : [
        'mrp',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'wizard/mrp_product_use_case_wizard.xml',
    ],
    'update_xml': [],
    'demo_xml': [],
    'installable': True,
    'application': False,
}

