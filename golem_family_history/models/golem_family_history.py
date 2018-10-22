# -*- coding: utf-8 -*-

#    Copyright 2018 Youssef El Ouahby <youssef@yaltik.com>
#    Copyright 2018 Fabien Bourgeois <fabien@yaltik.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

""" GOLEM Family History Management """

from odoo import models, fields, api, _

class GolemFamilyHistory(models.Model):
    """ GOLEM Family History  Management """
    _name = 'golem.family.history'
    _description = 'GOLEM Family History Management'
    _order = "season_id desc, id desc"

    family_id = fields.Many2one('golem.family', required=True, auto_join=True,
                                ondelete="cascade")
    season_id = fields.Many2one('golem.season', required=True, auto_join=True,
                                ondelete="cascade")
    city = fields.Char()
    country_id = fields.Many2one('res.country', string='Country')
    member_ids = fields.Many2many('res.partner')
