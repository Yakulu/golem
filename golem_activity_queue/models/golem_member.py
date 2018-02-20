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

from odoo import models, fields, api, _

class GolemMember(models.Model):
    """ GOLEM Member adaptations """
    _inherit = 'golem.member'

    @api.onchange('activity_registration_ids')
    def _checkRemain(self):

        if len(self.activity_registration_ids) > self.places and self.queue_allowed:
            return {
                'warning' : {
                    'title' : _('Warning'),
                    'message': _('No remaining place, please register in the queue'),
                }
            }

    def queue_register(self):

        return {
            'name'      : _('Choose the activity to register in'),
            'type'      : 'ir.actions.act_window',
            'res_model' : 'golem.activity.queue.choose.wizard',
            'view_mode': 'form',#'context' :{'default_activity_id' : activity_id.id},'domain' : [('activity_id.places_remain', '=', 0)],# activity_id.name)],#"('activity_id', '=', True)"'flags': {'action_buttons': True},
            'target': 'new',
        }
