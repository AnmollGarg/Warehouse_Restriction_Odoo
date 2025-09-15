from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    restricted_warehouse = fields.Boolean(string='Restricted Warehouse')

    #Preferences
    default_warehouse_operations = fields.Many2one('stock.warehouse', string='Default Warehouse Operations')
    restrict_location = fields.Boolean(string='Restrict Location')

    #Allowed Stock Locations
    allowed_locations = fields.Many2many('stock.location', string='Allowed Stock Locations')