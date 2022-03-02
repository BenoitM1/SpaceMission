# -*- coding: utf-8 -*-
# from odoo import http


# class Myfirstmodule(http.Controller):
#     @http.route('/myfirstmodule/myfirstmodule', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myfirstmodule/myfirstmodule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('myfirstmodule.listing', {
#             'root': '/myfirstmodule/myfirstmodule',
#             'objects': http.request.env['myfirstmodule.myfirstmodule'].search([]),
#         })

#     @http.route('/myfirstmodule/myfirstmodule/objects/<model("myfirstmodule.myfirstmodule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myfirstmodule.object', {
#             'object': obj
#         })
