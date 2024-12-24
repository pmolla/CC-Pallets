{
    'name': 'CC Pallets Module',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Custom module for CC Pallets project.',
    'author': 'Pablo Molla',
    'website': 'https://github.com/pmolla/cc-pallets',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/cc_pallets_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
