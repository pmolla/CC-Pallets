from odoo import http
from odoo.http import request

class CuentaCorrientePortal(http.Controller):

    @http.route(['/my/cuenta_corriente'], type='http', auth='user', website=True)
    def portal_cuenta_corriente(self, **kwargs):
        user = request.env.user
        cuenta_corriente_records = request.env['x_cuenta_corriente'].sudo().search([
            ('x_studio_cliente', '=', user.partner_id.id)  # Adjust field names if needed
        ])
        return request.render('custom_portal_cuenta_corriente.portal_cuenta_corriente_list', {
            'records': cuenta_corriente_records,
        })

    @http.route(['/my/cuenta_corriente/<int:record_id>'], type='http', auth='user', website=True)
    def portal_cuenta_corriente_detail(self, record_id, **kwargs):
        record = request.env['x_cuenta_corriente'].sudo().browse(record_id)
        return request.render('custom_portal_cuenta_corriente.portal_cuenta_corriente_detail', {
            'record': record,
        })
