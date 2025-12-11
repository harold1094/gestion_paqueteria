# -*- coding: utf-8 -*-
from odoo import models, fields

class PaqueteriaSeguimiento(models.Model):
    _name = 'gestion.paqueteria.seguimiento'
    _description = 'Seguimiento del paquete'

    name = fields.Char(string='Evento', required=True)
    fecha = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    estado = fields.Char(string='Estado')
    notas = fields.Text(string='Notas adicionales')

    paquete_id = fields.Many2one(
        'gestion.paqueteria.paquete',
        string='Paquete',
        required=True,
    )
