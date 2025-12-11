# -*- coding: utf-8 -*-
from odoo import models, fields

class PaqueteriaCamion(models.Model):
    _name = 'gestion.paqueteria.camion'
    _description = 'Camión de reparto'

    name = fields.Char(string='Matrícula', required=True)
    modelo = fields.Char(string='Modelo')
    capacidad_kg = fields.Float(string='Capacidad (kg)')
    activo = fields.Boolean(string='Activo', default=True)

    empresa_id = fields.Many2one(
        'gestion.paqueteria.empresa',
        string='Empresa',
        required=True,
    )

    paquete_ids = fields.One2many(
        'gestion.paqueteria.paquete',
        'camion_id',
        string='Paquetes cargados'
    )
