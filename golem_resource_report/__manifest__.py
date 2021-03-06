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
    'name': 'GOLEM resources reports',
    'summary': 'GOLEM resources reports',
    'description': ''' GOLEM resources reports ''',
    'version': '10.0.0.1.1',
    'category': 'GOLEM',
    'author': 'Youssef El Ouahby, Fabien Bourgeois',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': ['golem_resource'],
    'data': ['data/golem_resource_report_data.xml',
             'reports/golem_reservation_report.xml',
             'reports/golem_reservation_report_menu.xml',
             'wizard/golem_resource_report_wizard_views.xml',
             'views/golem_resource_report_menu.xml']
}
