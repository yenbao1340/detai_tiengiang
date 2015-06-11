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
import time
from openerp import SUPERUSER_ID

class ytdp_mohinh(models.Model):
    _name = "ytdp.mohinh"

    name = fields.Char(string='Tên mô hình', required=True)
    giatritiendoanam = fields.Float(string='Giá trị tiên đoán âm', required=False)
    giatritiendoanduong = fields.Float(string='Giá trị tiên đoán dương', required=False)
    log_likelihood = fields.Float(string='Log likelihood', required=False)
    thoigian = fields.Date(string='Thời gian', required=False)
    gioihantren = fields.Float(string='Giới hạn trên')
    gioihanduoi = fields.Float(string='Giới hạn dưới')
    giatriROC = fields.Float(string='Giá trị ROC')
    giatri_p = fields.Float(string='Giá trị p')
    saisochuan = fields.Float(string='Sai số chuẩn')
    khoantincay = fields.Float(string='Khoản tin cậy')
    thamso = fields.Float(string='Tham số', digits=(4,5), required=True)
    giatri_bienso_lines = fields.One2many(comodel_name='ytdp.biensomohinh', inverse_name='mohinh_id', string='Giá trị biến số')
        
ytdp_mohinh()

class ytdp_biensomohinh(models.Model):
    _name = "ytdp.biensomohinh"
    
    mohinh_id = fields.Many2one(comodel_name='ytdp.mohinh', string='Mô hình', required=True)
    maso_bienso = fields.Many2one(comodel_name='ytdp.bienso', string='Mã số biến số')
    thamso = fields.Float(string='Tham số', digits=(4,5), required=True)
        
ytdp_biensomohinh()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
