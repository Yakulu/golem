# -*- coding: utf-8 -*-

#    Copyright 2017 Fabien Bourgeois <fabien@yaltik.com>
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

""" GOLEM season testing """

from odoo.tests.common import TransactionCase
from odoo.models import ValidationError

class TestGolemSeason(TransactionCase):
    """ GOLEM season testing """

    def setUp(self, *args, **kwargs):
        """ Bootstrap res partner sale sector """
        super(TestGolemSeason, self).setUp(*args, **kwargs)
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

        with self.assertRaises(ValidationError):
            self.season_model.create({'name': 'date_end is empty',
                                      'date_start': '2009-11-01',
                                      'date_end': False})

        with self.assertRaises(ValidationError):
            self.season_model.create({'name': 'date_start is empty',
                                      'date_start' : False,
                                      'date_end': '2009-11-01'})

    def test_membership(self):
        """ Test if membership """
        new_season = self.env['golem.season'].create({'name': 'Name'})
        membership = self.env['product.template'].create({
            'name': 'Name',
            'season_id': new_season.id,
            'membership': True,
            'membership_date_from': '2017-11-01',
            'membership_date_to': '2018-11-01'
        })
        self.assertEqual(new_season.membership_ids[0], membership)
        self.assertEqual(membership.season_id, new_season)
        membership2 = self.env['product.template'].create({
            'name': 'Name2',
            'membership': True,
            'membership_date_from': '2017-11-01',
            'membership_date_to': '2018-11-01'
        })
        new_season.membership_ids = [(4, membership2.id, False)]
        self.assertEqual(len(new_season.membership_ids), 2)
        self.assertEqual(new_season.membership_ids[1], membership2)
        self.assertEqual(membership2.season_id, new_season)
