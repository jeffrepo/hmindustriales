# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict
from datetime import timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.fields import Command
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare, float_round


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    ultimo_precio_venta = fields.Float(string='Último precio de venta', readonly=True)
    
    @api.onchange('product_id')
    def _change_ultimo_precio_venta(self):
        for line in self:
            precio_ultima_venta = 0
            if line.product_id:
                ultima_venta_id = self.env['sale.order.line'].search([('product_id','=', line.product_id.id),('state','=','sale')], order="id desc")
                if ultima_venta_id:
                    precio_ultima_venta = ultima_venta_id[0].price_unit
                    line.ultimo_precio_venta = precio_ultima_venta
                else:
                    line.ultimo_precio_venta = precio_ultima_venta
