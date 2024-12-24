from odoo import http
from odoo.http import request

class CCPalletsPortal(http.Controller):
    
    @http.route(['/my/cc_pallets'], type='http', auth="user", website=True)
    def portal_cc_pallets(self, **kw):
        user = request.env.user
        pallets = request.env['cc.pallets.model'].sudo().search([('contact_id', '=', user.partner_id.id)])
        return request.render('cc_pallets_module.portal_cc_pallets_list', {
            'cc_pallets': pallets,
        })

    @http.route(['/my/cc_pallets/<int:pallet_id>'], type='http', auth="user", website=True)
    def portal_cc_pallets_view(self, pallet_id, **kw):
        pallet = request.env['cc.pallets.model'].sudo().browse(pallet_id)
        return request.render('cc_pallets_module.cc_pallets_portal_view', {
            'cc_pallet': pallet,
        })
