from odoo import models, fields, api
import random

class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng Nhân Viên'

    ma_nhan_vien = fields.Char(string="Mã Nhân Viên", required=True, copy=False, readonly=True, default=lambda self: self._generate_ma_nhan_vien())
    ten_nhan_vien = fields.Char(string="Tên Nhân Viên", required=True)
    anh_nhan_vien = fields.Binary(string="Ảnh Nhân Viên", attachment=True)
    so_dien_thoai = fields.Char(string="Số Điện Thoại")
    ngay_sinh = fields.Date(string="Ngày Sinh")
    can_cuoc_cong_dan = fields.Char(string="Căn Cước Công Dân")
    dia_chi = fields.Text(string="Địa Chỉ")
    chuc_vu = fields.Selection([
        ('nhan_vien', 'Nhân Viên'),
        ('quan_ly', 'Quản Lý'),
        ('giam_doc', 'Giám Đốc')
    ], string="Chức Vụ", required=True)
    du_an_ids = fields.Many2many('du_an', string="Dự Án Tham Gia")

    @api.model
    def _generate_ma_nhan_vien(self):
        """Tạo mã nhân viên tự động với 9 chữ số ngẫu nhiên"""
        ma_nhan_vien = str(random.randint(100000000, 999999999))
        while self.search([('ma_nhan_vien', '=', ma_nhan_vien)]):  # Đảm bảo không trùng lặp
            ma_nhan_vien = str(random.randint(100000000, 999999999))
        return ma_nhan_vien
