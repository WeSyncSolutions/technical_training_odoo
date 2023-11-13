{
    'name': 'Motorcycle Registry',
    'category': 'Kawiil/Custom Module Motorcycle',
    'author': "william1089",
    'summary': 'This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand',
    'version': '0.0.1.',
    'license': 'OPL-1', 
    'images': ['static/description/icon.png'],
    'website': 'https://github.com/william1089/technical_training_odoo.git',
    'description': """Motorcycle Registry""",
    'data': [
        'security/registry_groups.xml',
        'security/motorcycle_security.xml',
        'security/ir.model.access.csv',
        'views/motorcycle_menu_items.xml',
        'views/motorcycle_registry_view.xml',
    ],
    'demo': [
        'demo/motorcycle_demo.xml',
    ],
    'application': True,
    'installable': True,
}