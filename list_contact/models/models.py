# -*- coding: utf-8 -*-

from odoo import models, fields, api

   
class testSale(models.Model):
    _inherit = 'sale.order'
   
    list_contact = fields.Many2one('res.partner', string='Contacto del Cliente', domain="['&','&',('is_company','=',False),('parent_id','=',partner_id),('type','=','contact')]")


class TestNameContact(models.Model):
    _inherit = 'res.partner'
    
    def name_get(self):
        result = []
        for record in self:
            #result.append((record.id, '%s - %s' % (record.phone, record.name)))
            result.append((record.id, record.name))
        return result