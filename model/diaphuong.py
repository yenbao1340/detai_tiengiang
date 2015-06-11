# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
#
##############################################################################

from openerp import models, fields
from openerp import SUPERUSER_ID

class ytdp_diaphuong(models.Model):
    _name = "ytdp.diaphuong"

    name = fields.Char(string='Tên địa phương', size=64, required=True)
    dientich = fields.Float(string='Diện tích', required=True)
    danso = fields.Integer(string='Dân số', required=True)
    capdo = fields.Selection(selection=[('huyen', 'Huyện'),('xa', 'Xã'),('tinh', 'Tỉnh'),]
                                , string='Cấp độ', required=True, default='huyen')

ytdp_diaphuong()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
