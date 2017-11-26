# -*- coding: utf-8 -*-

from openerp import models, fields, api


class MusicaSong(models.Model):
    _name = 'musica.song'


    name = fields.Char(
        string='Genero')

    disk_song_ids = fields.Many2many('musica.disk',
                                'res_disk_song_rel',
                                'song_id',
                                'disk_id',
                                string='Canciones')

    author_song_id = fields.Many2one('musica.author',
        string='Author')

    titulo = fields.Char(
        string='Título')

    fecha_creacion = fields.Date(
        string='Fecha creación')

    duracion = fields.Float(
        string='Duración')

    tipo = fields.Selection(
        [('mp3', 'MP3'),('mp4','MP4'),('normal','NORMAL')],
        string='Type')
