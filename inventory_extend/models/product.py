# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import operator as py_operator
from ast import literal_eval
from collections import defaultdict

import self
from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.osv import expression
from odoo.tools import float_is_zero, check_barcode_encoding
from odoo.tools.float_utils import float_round
from odoo.tools.mail import html2plaintext, is_html_empty




class Product(models.Model):
    _inherit = "product.product"



    # price_unit = fields.Float('Unit Price', compute='_compute_quantities_dict', readonly=True)
    #
    # @api.depends('stock_move_ids', 'stock_move_ids.price_unit')
    # def _compute_quantities_dict(self):
    #     for product in self:
    #         # Use the existing method to compute quantities
    #         quantities = product._compute_quantities_dict()
    #         # Extract the price_unit from the move results
    #         price_unit = quantities[product.id].get('price_unit', 0.0)
    #         # Update the price_unit field on the product
    #         product.price_unit = price_unit



