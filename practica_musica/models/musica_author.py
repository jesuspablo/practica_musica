# -*- coding: utf-8 -*-

from openerp import models, fields, api


class MusicaAuthor(models.Model):
    _name = 'musica.author'


    name = fields.Char(
        string='Author')

    image = fields.Binary(string='Imagen')

    ciudad_natal = fields.Char(
        string='Ciudad natal')

    edad = fields.Integer('Edad')

    sexo = fields.Char(string='Sexo')

    disk_author_ids = fields.Many2many('musica.disk',
                                       'res_disk_author_rel',
                                       'author_id',
                                       'disk_aut_id',
                                       string='Discos')

    song_author_ids = fields.Many2many('musica.song',
                                       'res_author_song_rel',
                                       'author_id',
                                       'song_aut_id',
                                       string='Canciones')