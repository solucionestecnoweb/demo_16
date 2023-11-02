# -*- coding: utf-8 -*-

from odoo import models, fields, api


    
class testVenta(models.Model):
    _inherit = 'sale.order'
   
    lista_contactos = fields.Many2one('res.partner', string='Contacto del Cliente', domain="['&','&',('is_company','=',False),('parent_id','=',partner_id),('type','=','contact')]")

class testVentaFactura(models.Model):
    _inherit = 'account.move'
   
    lista_contactos = fields.Many2one('res.partner', string='Contacto del Cliente', domain="['&','&',('is_company','=',False),('parent_id','=',partner_id),('type','=','contact')]")

class TestNombreContacto(models.Model):
    _inherit = 'res.partner'
    
    def name_get(self):
        result = []
        for record in self:
            #result.append((record.id, '%s - %s' % (record.phone, record.name)))
            result.append((record.id, record.name))
        return result