# -*- coding: utf-8 -*-

from openerp import models, fields, api


class MusicaDisk(models.Model):
    _name = 'musica.disk'


    name = fields.Char(
        string='Título')

    fecha_publicacion = fields.Date(
        string='Fecha publicación')

    author_disk_id = fields.Many2one('musica.author',
        string='Author')


    description = fields.Text(
        string='Descripción')

    puntuacion = fields.Char(
        string='Puntuacion AllMusil')


    song_disk_ids = fields.Many2many('musica.song',
                                    'res_disk_song_rel',
                                    'disk_id',
                                    'song_id',
                                    string='Canciones')

    author_disk_ids = fields.Many2many('musica.author',
                                'res_disk_author_rel',
                                'disk_aut_id',
                                'author_id',
                                string='Autores')