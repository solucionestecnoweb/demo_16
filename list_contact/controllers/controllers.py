# -*- coding: utf-8 -*-
# from odoo import http


# class Camposmc(http.Controller):
#     @http.route('/camposmc/camposmc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/camposmc/camposmc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('camposmc.listing', {
#             'root': '/camposmc/camposmc',
#             'objects': http.request.env['camposmc.camposmc'].search([]),
#         })

#     @http.route('/camposmc/camposmc/objects/<model("camposmc.camposmc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('camposmc.object', {
#             'object': obj
#         })
