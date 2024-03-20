import logging

from odoo import fields, models, api, exceptions
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = 'stock.move'

    qty_available = fields.Float(related='product_id.qty_available', string="Remaining Quantity",
                                 compute='_check_qty_available')
    product_id = fields.Many2one('product.product', string="Product", onchange='__onchange_product_id')
    picking_type_code = fields.Selection(
        related='picking_type_id.code',
        readonly=True)
    # check qty_available
    @api.onchange('product_id', 'quantity_done', 'picking_type_code')
    def _check_qty_available(self):
        if self.picking_type_code == 'outgoing' and self.product_id and self.quantity_done:
            if self.quantity_done > self.qty_available:
                error_message = (
                        f"selected quantity ({self.quantity_done}) exceeds the available stock ({self.qty_available}).\n"
                        f" stock for this product: {self.qty_available}"
                )
                raise UserError(error_message)



