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

class ytdp_donvitinh(models.Model):
    _name = "ytdp.donvitinh"
    name= fields.Char(string="Tên đơn vị", required=True, size=64)

ytdp_donvitinh()

class ytdp_bienso(models.Model):
    _name = "ytdp.bienso"

    name = fields.Char(string='Tên biến số', size=250, required=True)
    ghichu = fields.Char(string='Ghi chú', size=250)
    congthuc = fields.Char(string='Công thức tính', size=250)
    ghichu_gioihan = fields.Char(string='Diễn giải giới hạn', size=250)
    kyhieu = fields.Char(string='Ký hiệu', size=250, required=True)
    gioihantren = fields.Float(string='Giới hạn trên')
    gioihanduoi = fields.Float(string='Giới hạn dưới')
    lientuc = fields.Selection(selection = [('lientuc', 'Liên tục'),('khong_lientuc', 'Không liên tục'),]
                                    , string='Liên tục', required=True, default='khong_lientuc')
    donvitinh = fields.Many2one(comodel_name='ytdp.donvitinh', string='Đơn vị tính', required=True)
    loaibienso = fields.Selection(selection = [('doclap', 'Độc lập'), ('phuthuoc', 'Phụ thuộc'),]
                                    , string='Loại biến số', required=True, default='doclap')
    giatri_bienso_lines = fields.One2many(comodel_name='ytdp.giatribienso', inverse_name='bienso_id', string='Giá trị biến số')

ytdp_bienso()

class ytdp_giatribienso(models.Model):
    _name = "ytdp.giatribienso"
    
    bienso_id = fields.Many2one(comodel_name='ytdp.bienso', string='Biến số', ondelete='cascade', required=True)
    giatri = fields.Float(string='Giá trị', required=True)
    thoigian = fields.Date(string='Thời gian', required=True)
    diemdo = fields.Many2one(comodel_name='ytdp.diaphuong', string='Điểm đo/Địa phương', required=True)
        
ytdp_giatribienso()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
