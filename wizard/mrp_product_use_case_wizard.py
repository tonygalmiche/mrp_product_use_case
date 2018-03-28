# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.tools.translate import _
from openerp.exceptions import Warning


class  mrp_product_use_case_wizard(models.TransientModel):
    _name = 'mrp.product.use.case.wizard'
    
    product_id = fields.Many2one('product.product','Component', required=True)


    @api.multi
    def mrp_product_use_case(self, wizard_id, component_id, level):
        cr=self._cr
        sql="""
            select 
                mbl.sequence,
                mbl.product_id,
                mbl.product_qty,
                mb.product_tmpl_id,
                mb.id mb_id,
                (select id from product_product where product_tmpl_id=mb.product_tmpl_id limit 1) compose_id
            from mrp_bom_line mbl inner join mrp_bom mb on mbl.bom_id=mb.id
            where mbl.product_id="""+str(component_id)+"""
        """
        cr.execute(sql)
        result=cr.fetchall()
        for row in result:
            compose_id=row[5]
            compose=self.env['product.product'].browse(compose_id)
            level_txt=''
            for i in range(1, level):
                level_txt=level_txt+u'-'
            level_txt=level_txt+str(level)
            vals={
                'wizard_id'   : wizard_id,
                'level'       : level_txt,
                'component_id': component_id,
                'line'        : row[0],
                'quantity'    : row[2],
                'mrp_bom_id'  : row[4],
            }
            res=self.env['mrp.product.use.case.line'].create(vals)
            self.mrp_product_use_case(wizard_id, compose_id,level+1)


    @api.multi
    def do_search_component(self):
        for obj in self:
            if obj.product_id:
                self.mrp_product_use_case(obj.id, obj.product_id.id,1)
        return {
            'name': u"MRP Product Use Case "+str(obj.product_id.name),
            'view_mode': 'tree,form',
            'view_type': 'form',
            'res_model': 'mrp.product.use.case.line',
            'type': 'ir.actions.act_window',
            'domain': [('wizard_id','=',obj.id)],
        }


class mrp_product_use_case_line(models.TransientModel):
    _name = 'mrp.product.use.case.line'
    
    wizard_id    = fields.Many2one('mrp.product.use.case.wizard','Wizard')
    level        = fields.Char('Level')
    component_id = fields.Many2one('product.product','Component')
    line         = fields.Integer('Line')
    quantity     = fields.Float('Quantity', digits=(14,6))
    mrp_bom_id   = fields.Many2one('mrp.bom','Product')

