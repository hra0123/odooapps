# -*- coding: utf-8 -*-
from odoo import models, fields, api
class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    is_foc = fields.Boolean(string="FOC")
    @api.onchange('product_qty', 'product_uom', 'is_foc')
    def _onchange_quantity(self):
        res = super(PurchaseOrderLine, self)._onchange_quantity()
        if self.is_foc:
            self.price_unit = 0.0
        return res

    def write(self, vals):
        res = super(PurchaseOrderLine, self).write(vals)
        if vals.get('is_foc'):
            self.price_unit = 0.0
        return res
