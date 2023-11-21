{
    'name': 'Motorcycle Stock',
    'category': 'Kawiil/Custom Module Motorcycle',
    'author': "william1089",
    'summary': 'This Module is used to have stock control about motorcycles',
    'version': '0.0.1.',
    'license': 'OPL-1', 
    'images': ['static/description/icon.png'],
    'website': 'https://github.com/william1089/technical_training_odoo.git',
    'description': """Motorcycle Stock""",
    'depends':['stock'],
    'data': [
        'views/product_template_inherit.xml',
    ],
    'demo': [
        'demo/product_demo.xml',
    ],
    'application': True,
    'installable': True,
}