from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResUsers(models.Model):
    _inherit = 'res.users'

    restricted_warehouse = fields.Boolean(string='Restrict Warehouse Operations')

    # Preferences
    default_warehouse_operations = fields.Many2many(
        'stock.picking.type', 
        string='Allowed Operations',
        help='User will only be able to access these operations'
    )
    restrict_location = fields.Boolean(string='Restrict Locations')

    # Allowed Stock Locations
    allowed_locations = fields.Many2many(
        'stock.location',
        string='Allowed Stock Locations',
        help='User will only be able to access these stock locations'
    )

    @api.constrains('restricted_warehouse', 'default_warehouse_operations')
    def _check_default_warehouse_operations(self):
        for user in self:
            if user.restricted_warehouse and not user.default_warehouse_operations:
                raise ValidationError(self.env._("You must select at least one allowed operation if 'Restrict Warehouse Operations' is enabled."))