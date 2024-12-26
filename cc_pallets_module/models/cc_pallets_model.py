from odoo import models, fields

class CCPalletsModel(models.Model):
    _name = 'cc.pallets.model'
    _description = 'CC Pallets Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Agregar funcionalidades de chatter y actividades

    name = fields.Char(string='Name', tracking=True)  # Habilita seguimiento en este campo
    description = fields.Text(string='Description')
    contact_id = fields.Many2one('res.partner', string='Contact')  # Relacional con contactos
    product_id = fields.Many2one('product.product', string='Product')  # Relacional con productos
