# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
import logging

class PosOrder(models.Model):
    _inherit = 'pos.order'
    
    def buscar_stock(self, dicc_productos, tipo_operacion):
        productos_sin_stock = []
        tipo_operacion_id = self.env['stock.picking.type'].search([('id','=',tipo_operacion)])
        ubicacion = self.env['stock.location'].search([('id','=',tipo_operacion_id.default_location_src_id.id)])
        for pid in dicc_productos:
            producto = self.env['product.product'].search([('id','=',pid)])
            if producto.detailed_type == "product":
                cantidad = self.env['stock.quant']._get_available_quantity(producto,ubicacion, False, False, False,False,False)
                if dicc_productos[pid] > cantidad:
                    productos_sin_stock.append(producto.name)
        return productos_sin_stock