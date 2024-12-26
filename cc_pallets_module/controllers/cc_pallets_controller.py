from odoo import http
from odoo.http import request

class CCPalletsPortal(http.Controller):

    @http.route(['/my/cc_pallets'], type='http', auth='user', website=True)
    def portal_cc_pallets_list(self, **kwargs):
        """Controlador para listar los CC Pallets en el portal."""
        # Obtener los pallets asociados al usuario actual
        cc_pallets = request.env['cc.pallets.model'].search([('contact_id', '=', request.env.user.partner_id.id)])
        
        return request.render('cc_pallets_module.cc_pallets_portal_page', {
            'cc_pallets': cc_pallets
        })

    @http.route(['/my/cc_pallets/<int:pallet_id>'], type='http', auth='user', website=True)
    def portal_cc_pallet_view(self, pallet_id, **kwargs):
        """Controlador para ver los detalles de un CC Pallet."""
        # Buscar el pallet por ID y asegurar que pertenece al usuario actual
        pallet = request.env['cc.pallets.model'].sudo().browse(pallet_id)
        if not pallet or pallet.contact_id.id != request.env.user.partner_id.id:
            return request.render('website.404')
        
        return request.render('cc_pallets_module.cc_pallets_portal_view', {
            'cc_pallet': pallet
        })
