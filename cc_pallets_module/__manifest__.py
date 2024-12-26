{
    'name': 'CC Pallets Module',
    'version': '1.2',
    'category': 'Custom',
    'summary': 'Custom module for CC Pallets project.',
    'author': 'Pablo Molla',
    'website': 'https://github.com/pmolla/cc-pallets',
    'depends': [
        'base',
        'portal',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/cc_pallets_portal_page.xml',
        'views/cc_pallets_portal_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
