{
    'name': 'Portal Cuenta Corriente',
    'version': '1.0',
    'author': 'Pablo Molla',
    'category': 'Custom',
    'summary': 'Portal View for Cuenta Corriente',
    'depends': ['portal', 'x_studio_custom'],  # Replace with the actual Studio module name
    'data': [
        'views/portal_templates.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.cuenta_corriente.xml',
    ],
    'installable': True,
    'application': False,
}
