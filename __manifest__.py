{
    'name': 'Cuenta Corriente Portal',
    'version': '1.0',
    'depends': ['base', 'portal', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'security/ir.rule.xml',
        'views/portal_menu.xml',
        'views/portal_templates.xml',
    ],
    'installable': True,
    'application': False,
}

