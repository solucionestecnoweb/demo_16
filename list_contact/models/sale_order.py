# -*- coding: utf-8 -*-

from odoo import models, fields, api

   
class SaleOrder(models.Model):
    _inherit = 'sale.order'
   
    partner_contact_id  = fields.Many2one('res.partner', domain="[('is_company','=',False),('parent_id','=',partner_id),('type','=','contact')]" )


class ResPartnerContact(models.Model):
    _inherit = 'res.partner'
    
    def name_get(self):
        result = []
        for record in self:
            #result.append((record.id, '%s - %s' % (record.phone, record.name)))
            result.append((record.id, record.name))
        return result