{
    'name': 'Cuenta Corriente Portal',
    'version': '1.0',
    'depends': ['base', 'portal', 'website'],

    'data': [
        'security/ir.model.access.csv',
        'views/portal_menu.xml',  # Load this after related dependencies
    ],

    'installable': True,
    'application': False,
}

