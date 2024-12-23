from odoo import models, fields, api

class AccountInventory(models.Model):
    _name = 'account.inventory'
    _description = 'Cuenta Corriente de Inventario'

    name = fields.Char(string="Descripción", required=True)
    partner_id = fields.Many2one('res.partner', string="Contacto", required=True)
    product_id = fields.Many2one('product.product', string="Producto", required=False)
    inventory_move_ids = fields.One2many('stock.move', 'account_inventory_id', string="Movimientos de Inventario")

    @api.depends('partner_id', 'product_id')
    def get_inventory_movements(self):
        """
        Search and retrieve inventory movements based on the selected partner and product.
        """
        for record in self:
            domain = [('partner_id', '=', record.partner_id.id), ('state', '=', 'done')]
            if record.product_id:
                domain.append(('product_id', '=', record.product_id.id))
            moves = self.env['stock.move'].search(domain)
            record.inventory_move_ids = moves
