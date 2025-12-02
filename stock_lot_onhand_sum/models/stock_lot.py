# -*- coding: utf-8 -*-
from odoo import api,  models
import itertools


class StockLot(models.Model):
    _inherit = 'stock.lot'

    def _read_group_select(self, aggregate_spec, query):
        # flag value as aggregatable, and manually sum the values from the
        # records in the group
        if aggregate_spec == 'product_qty:sum':
            return super()._read_group_select('id:recordset', query)
        return super()._read_group_select(aggregate_spec, query)

    def _read_group_postprocess_aggregate(self, aggregate_spec, raw_values):
        if aggregate_spec == 'product_qty:sum':
            column = super()._read_group_postprocess_aggregate('id:recordset', raw_values)
            return (sum(records.mapped('product_qty')) for records in column)
        return super()._read_group_postprocess_aggregate(aggregate_spec, raw_values)


