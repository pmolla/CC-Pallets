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
        'views/menu.xml',
        'views/cc_pallets_views.xml',  # Agrega este si creaste un archivo separado
        'views/cc_pallets_portal_page.xml',
        'views/cc_pallets_portal_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
