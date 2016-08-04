# -*- coding: utf-8 -*-

#    Copyright 2016 Fabien Bourgeois <fabien@yaltik.com>
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

from openerp.tests.common import TransactionCase
from openerp.models import ValidationError


class GolemSeasonTestCase(TransactionCase):

    def setUp(self):
        super(GolemSeasonTestCase, self).setUp()
        self.season_model = self.env['golem.season'].sudo()

    def test_season_default(self):
        """ Test uniqueness of default season """
        first = self.season_model.create({'name': u'First'})
        self.assertTrue(first.is_default)
        second = self.season_model.create({'name': u'Second'})
        self.assertFalse(second.is_default)
        second.do_default_season()
        self.assertTrue(second.is_default)
        self.assertFalse(first.is_default)

    def test_check_period(self):
        """ Tests constraints on periods """
        old = self.season_model.create({'name': 'Valid',
                                        'date_start': '2010-01-01',
                                        'date_end': '2010-12-31'})
        self.assertTrue(old.date_end > old.date_start)
        with self.assertRaises(ValidationError):
            old.write({'date_start': '2011-01-01'})
        with self.assertRaises(ValidationError):
            self.season_model.create({'name': 'Conflict for start',
                                      'date_start': '2010-11-01',
                                      'date_end': '2011-12-31'})
        with self.assertRaises(ValidationError):
            self.season_model.create({'name': 'Conflict : include existing',
                                      'date_start': '2009-11-01',
                                      'date_end': '2011-12-31'})