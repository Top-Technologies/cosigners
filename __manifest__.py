# -*- coding: utf-8 -*-
{
    'name': 'HR Cosigner',
    'version': '18.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Manage Cosigners for Employees',
    'description': """
        This module adds a Cosigner management feature to the Employee Profile.
        
        Features:
        - Add cosigners with photo, name, phone and document attachments
        - Cosigner tab in employee profile
        - Full CRUD functionality
        - Integration with Odoo's attachment system
    """,
    'author': 'Custom Dev Team Top Tech',
    'website': '',
    'depends': ['hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_cosigner_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_cosigner_reporting.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
