from odoo import http
from odoo.http import request

class CuentaCorriente(http.Controller):
    @http.route('/my/cuenta_corriente', type='http', auth='user', website=True)
    def cuenta_corriente(self, **kwargs):
        """Render the Cuenta Corriente page."""
        records = request.env['x_cuenta_corriente'].sudo().search([
            ('x_studio_cliente', '=', request.env.user.partner_id.id)
        ])
        return request.render('cuentacorriente.portal_cuenta_corriente_list', {
            'records': records
        })

