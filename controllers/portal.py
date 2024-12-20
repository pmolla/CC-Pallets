from odoo import http
from odoo.http import request


class CuentaCorriente(http.Controller):
    @http.route('/my/cuenta_corriente', type='http', auth='user', website=True)
    def cuenta_corriente(self, **kwargs):
        """Route for displaying the list of 'Cuenta Corriente' records"""
        records = request.env['x_cuenta_corriente'].sudo().search([
            ('x_studio_cliente', '=', request.env.user.partner_id.id)
        ])
        return request.render('cuentacorriente.portal_cuenta_corriente_list', {
            'records': records
        })

    @http.route('/my/cuenta_corriente/<int:record_id>', type='http', auth='user', website=True)
    def cuenta_corriente_detail(self, record_id, **kwargs):
        """Route for displaying details of a single 'Cuenta Corriente' record"""
        record = request.env['x_cuenta_corriente'].sudo().browse(record_id)
        if not record.exists():
            return request.not_found()
        return request.render('cuentacorriente.portal_cuenta_corriente_detail', {
            'record': record
        })

