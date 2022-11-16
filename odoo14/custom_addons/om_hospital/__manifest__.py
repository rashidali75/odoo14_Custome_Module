{
    'name': 'Hospital Management',
    'version': '14.0.0.0.1',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management System""",
    'category': 'productivity',
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',

    'depends': [
        'sale',
        'mail',
        # 'website_slides',
        # 'hr',
        # 'report_xlsx'

    ],

    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/sale.xml',
        'report/patient_card.xml',
        # 'report/patient_details_template.xml',
        'report/report.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
