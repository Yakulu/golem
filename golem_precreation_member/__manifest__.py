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

{
    'name': 'GOLEM Pre-creation search member',
    'summary': 'Pre-creation search member',
    'version': '10.0.0.0.0',
    'category': 'GOLEM',
    'author': 'Fabien Bourgeois, Youssef El ouahby',
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'depends': ['golem_member', 'golem_family'],
    'data': ['views/golem_member_views.xml',
             'views/partner_views.xml',
             'wizard/golem_precreation_member_request_wizard_views.xml',
             'wizard/golem_precreation_member_result_wizard_views.xml']
}
