from odoo import http
from odoo.http import request

class CuentaCorriente(http.Controller):

    @http.route('/my/cuenta_corriente', type='http', auth='user', website=True)
    def cuenta_corriente(self, **kwargs):
        """Render the Cuenta Corriente page."""
        # Buscar los registros de 'x_cuenta_corriente' vinculados al usuario actual
        records = request.env['x_cuenta_corriente'].sudo().search([
            ('x_studio_cliente', '=', request.env.user.partner_id.id)
        ])
        return request.render('cuentacorriente.portal_cuenta_corriente_list', {
            'records': records
        })

    @http.route('/my/cuenta_corriente/movements', type='http', auth='user', website=True)
    def cuenta_corriente_movements(self, **kwargs):
        """Render the Inventory Movements page for the Cuenta Corriente."""
        # Buscar movimientos de inventario vinculados al cliente actual
        inventory_moves = request.env['stock.move'].sudo().search([
            ('partner_id', '=', request.env.user.partner_id.id),
            ('state', '=', 'done')  # Solo movimientos completados
        ])
        return request.render('cuentacorriente.portal_inventory_movements', {
            'inventory_moves': inventory_moves
        })


