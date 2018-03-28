# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    def use_case_action(self):
        for obj in self:
            products=self.env['product.product'].search([('product_tmpl_id','=',obj.id)])
            for product in products:
                return product.use_case_action()


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.multi
    def use_case_action(self):
        for obj in self:
            vals={
                'product_id': obj.id
            }
            wizard=self.env['mrp.product.use.case.wizard'].create(vals)
            return wizard.do_search_component()



