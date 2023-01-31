# -*- coding: utf-8 -*-
{
    'name': "Transporte y Flete",

    'summary': """
        Módulo para la gestión de transportes y Fletes""",

    'description': """
        Gestión de camiones, conductores y los viajes que estos realizan,
        Gestión de Carga y descarga de paquetes.
    """,

    'author': "RicardoTeranNet",
    'website': "www.ricardoteran.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
        'security/transportes_security.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application':True,
}
