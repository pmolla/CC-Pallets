from odoo import http
from odoo.http import request

class CuentaCorriente(http.Controller):
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


