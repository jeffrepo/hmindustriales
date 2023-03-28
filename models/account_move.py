# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('partner_id')
    def _change_partner_hm(self):
        for move in self:
            if move.partner_id and move.partner_id.l10n_mx_edi_usage:
                move.l10n_mx_edi_usage = move.partner_id.l10n_mx_edi_usage


class PosOrder(models.Model):
    _inherit = 'pos.order'
    
    def buscar_stock(self, dicc_productos):
        productos_sin_stock = []
        logging.warning(dicc_productos)
        productos_stock = self.env['stock.quant']
        return productos_sin_stock
