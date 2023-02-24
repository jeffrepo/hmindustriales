# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('partner_id')
    def _change_partner_hm(self):
        for move in self:
            if move.partner_id and move.partner_id.l10n_mx_edi_usage:
                move.l10n_mx_edi_usage = move.partner_id.l10n_mx_edi_usage