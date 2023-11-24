{
    'name': 'Motorcycle Website',
    'category': 'Kawiil/Custom Module Motorcycle',
    'author': "william1089",
    'summary': 'This Module is used to show motorcycles on website',
    'version': '0.0.1.',
    'license': 'OPL-1', 
    'images': ['static/description/icon.png'],
    'website': 'https://github.com/william1089/technical_training_odoo.git',
    'description': """Motorcycle Website""",
    'depends':['motorcycle_stock','website'],
    'data': [
        'views/motorcycle_templates.xml',
    ],
    'demo': [
    ],
    'application': True,
    'installable': True,
    'autoinstall': True, 
}