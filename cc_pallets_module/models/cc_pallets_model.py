from odoo import models, fields


class CCPalletsModel(models.Model):
    _name = 'cc.pallets.model'
    _description = 'CC Pallets Model'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    contact_id = fields.Many2one('res.partner', string='Contact')  # Relational field to Contacts
    product_id = fields.Many2one('product.product', string='Product')  # Relational field to Products
