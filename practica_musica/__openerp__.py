# -*- coding: utf-8 -*-
{

    'name' : 'Música',
    'summary' : """
                Tutorial Odoo 8.0
                """,

    'description' : """
                aprendisaje personal de Odoo 8.0 Aplicación musical
                -Este módulo sirve para ver la mejoría de conocimientos de Odoo
                    """,

    'author' : '-Alumno: Jesus pablo Ndong',

    'category' : 'learning',
    'version' : '8.0.0.2',

    'depends' : [

                ],

    'data' : [
            'views/musica_menu.xml',
            'views/musica_author.xml',
            'views/musica_disk.xml',
            'views/musica_song.xml',
            #'security/ir.model.access.csv',



    ],



    "installable": True,
    # only loaded in demonstration mode


}
