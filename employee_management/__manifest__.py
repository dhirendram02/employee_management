# -*- coding: utf-8 -*-
# Part of Softprime consulting Pvt Ltd.
{
    'name': 'Employee Management',
    'category': 'Custom',
    'summary': 'This module is a custom module',
    'description': """
        This module is a custom module
    """,
    'author': 'SoftPrime Consulting Pvt Ltd',
    'website': 'http://www.softprimeconsulting.com',
    'company': 'SoftPrime Consulting Pvt Ltd',
    'license': 'Other proprietary',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee.xml',
        'menu/menu.xml',

    ],

    'installable': True,
    'application': True,
}