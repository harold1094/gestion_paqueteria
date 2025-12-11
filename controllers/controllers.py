# -*- coding: utf-8 -*-
# from odoo import http


# class /var/lib/odoo/addons/18.0/gestionPaqueteria(http.Controller):
#     @http.route('//var/lib/odoo/addons/18.0/gestion_paqueteria//var/lib/odoo/addons/18.0/gestion_paqueteria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//var/lib/odoo/addons/18.0/gestion_paqueteria//var/lib/odoo/addons/18.0/gestion_paqueteria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/var/lib/odoo/addons/18.0/gestion_paqueteria.listing', {
#             'root': '//var/lib/odoo/addons/18.0/gestion_paqueteria//var/lib/odoo/addons/18.0/gestion_paqueteria',
#             'objects': http.request.env['/var/lib/odoo/addons/18.0/gestion_paqueteria./var/lib/odoo/addons/18.0/gestion_paqueteria'].search([]),
#         })

#     @http.route('//var/lib/odoo/addons/18.0/gestion_paqueteria//var/lib/odoo/addons/18.0/gestion_paqueteria/objects/<model("/var/lib/odoo/addons/18.0/gestion_paqueteria./var/lib/odoo/addons/18.0/gestion_paqueteria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/var/lib/odoo/addons/18.0/gestion_paqueteria.object', {
#             'object': obj
#         })

