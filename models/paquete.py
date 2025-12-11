# -*- coding: utf-8 -*-
from odoo import models, fields

class PaqueteriaPaquete(models.Model):
    _name = 'gestion.paqueteria.paquete'
    _description = 'Paquete'

    name = fields.Char(string='Código de seguimiento', required=True)
    descripcion = fields.Text(string='Descripción')
    peso_kg = fields.Float(string='Peso (kg)')

    remitente_id = fields.Many2one(
        'res.partner',
        string='Remitente',
    )

    destinatario_id = fields.Many2one(
        'res.partner',
        string='Destinatario',
    )

    empresa_id = fields.Many2one(
        'gestion.paqueteria.empresa',
        string='Empresa',
        required=True,
    )

    camion_id = fields.Many2one(
        'gestion.paqueteria.camion',
        string='Camión asignado',
    )

    estado = fields.Selection(
        [
            ('borrador', 'Borrador'),
            ('en_ruta', 'En ruta'),
            ('entregado', 'Entregado'),
            ('incidencia', 'Incidencia'),
        ],
        string='Estado',
        default='borrador',
    )

    fecha_envio = fields.Date(string='Fecha de envío')
    fecha_entrega_estimada = fields.Date(string='Fecha estimada')

    seguimiento_ids = fields.One2many(
        'gestion.paqueteria.seguimiento',
        'paquete_id',
        string='Seguimiento'
    )
