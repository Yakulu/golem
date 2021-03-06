# -*- coding: utf-8 -*-
#
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

""" GOLEM Member adaptations """

from odoo import models, fields, api


class GolemMember(models.Model):
    """ GOLEM Member adaptations """
    _inherit = 'golem.member'

    member_history_ids = fields.One2many('golem.member.history', 'member_id',
                                         readonly=True, string='History details')

    @api.constrains('gender', 'area_id', 'zip', 'city', 'family_quotient',
                    'pcs_id', 'nationality_id', 'season_ids')
    def save_history(self):
        """ Saves member history """
        default_season = self.env['golem.season'].search([('is_default', '=', True)], limit=1)
        for member in self:
            history_id = self.env['golem.member.history'].search([
                ('member_id', '=', member.id),
                ('season_id', '=', default_season.id)], limit=1)
            history_data = {'gender': member.gender,
                            'nationality_id': member.nationality_id.id,
                            'zip_code': member.zip,
                            'city': member.city,
                            'family_quotient': member.family_quotient,
                            'pcs_id': member.pcs_id.id,
                            'area_id': member.area_id.id}
            if history_id:
                history_id.write(history_data)
            else:
                history_data.update({'member_id': member.id,
                                     'season_id': default_season.id})
                self.env['golem.member.history'].create(history_data)
