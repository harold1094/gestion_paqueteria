# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /var/lib/odoo/addons/18.0/gestion_paqueteria(models.Model):
#     _name = '/var/lib/odoo/addons/18.0/gestion_paqueteria./var/lib/odoo/addons/18.0/gestion_paqueteria'
#     _description = '/var/lib/odoo/addons/18.0/gestion_paqueteria./var/lib/odoo/addons/18.0/gestion_paqueteria'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

