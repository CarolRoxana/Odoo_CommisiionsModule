# -*- coding: utf-8 -*-
# from odoo import http


# class TdvCommissions(http.Controller):
#     @http.route('/tdv_commissions/tdv_commissions', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tdv_commissions/tdv_commissions/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tdv_commissions.listing', {
#             'root': '/tdv_commissions/tdv_commissions',
#             'objects': http.request.env['tdv_commissions.tdv_commissions'].search([]),
#         })

#     @http.route('/tdv_commissions/tdv_commissions/objects/<model("tdv_commissions.tdv_commissions"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tdv_commissions.object', {
#             'object': obj
#         })
