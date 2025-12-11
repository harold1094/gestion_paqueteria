# -*- coding: utf-8 -*-
{
    'name': 'Gestión de Paquetería',
    'version': '1.0',
    'author': 'Harold',
    'category': 'Operations',
    'summary': 'Gestión sencilla de paquetería: empresas, camiones, paquetes y seguimiento',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/empresa_views.xml',
        'views/camion_views.xml',
        'views/paquete_views.xml',
        'views/seguimiento_views.xml',
        'views/paqueteria_menu.xml',
    ],
    'installable': True,
    'application': True,
}
