# -*- coding: utf-8 -*-
from odoo import models, fields

class PaqueteriaEmpresa(models.Model):
    _name = 'gestion.paqueteria.empresa'
    _description = 'Empresa de paquetería'

    name = fields.Char(string='Nombre', required=True)
    street = fields.Char(string='Dirección')
    city = fields.Char(string='Ciudad')
    zip = fields.Char(string='Código postal')
    phone = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo electrónico')

    country_id = fields.Many2one(
        'res.country',
        string='País',
    )

    camion_ids = fields.One2many(
        'gestion.paqueteria.camion',
        'empresa_id',
        string='Camiones'
    )

    paquete_ids = fields.One2many(
        'gestion.paqueteria.paquete',
        'empresa_id',
        string='Paquetes'
    )
