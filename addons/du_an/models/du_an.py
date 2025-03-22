from odoo import models, fields, api
from datetime import date

class DuAn(models.Model):
    _name = 'du_an'
    _description = 'Bảng chứa thông tin dự án'

    ten_du_an = fields.Char("Tên dự án", required=True)
    ma_du_an = fields.Char("Mã dự án", required=True)
    mo_ta = fields.Text("Mô tả")
    ngay_bat_dau = fields.Date("Ngày bắt đầu")
    ngay_ket_thuc = fields.Date("Ngày kết thúc")
    nguoi_chiu_trach_nhiem = fields.Many2one('res.users', string="Người chịu trách nhiệm")
    nhan_vien_ids = fields.Many2many('nhan_vien', string="Nhân Viên Tham Gia")
    trang_thai = fields.Selection([
        ('chuẩn_bị', 'Chuẩn bị'),
        ('dang_thuc_hien', 'Đang thực hiện'),
        ('hoan_thanh', 'Hoàn thành'),
        ('dung', 'Dừng lại')
    ], string="Trạng thái", default='chuẩn_bị', readonly=True)
    chi_phi_ids = fields.One2many('chi_phi_du_an', 'du_an_id', string="Chi Phí Dự Án")
    so_tien = fields.Float(string="Tổng Chi Phí", compute='_compute_so_tien', store=True)
    ten_nhan_vien = fields.Many2many('nhan_vien', 'du_an_id', string='Nhân viên', required=True)
    so_ngay_con_lai = fields.Integer(string="Số ngày còn lại", compute='_compute_so_ngay_con_lai', store=True)
    bao_cao_ids = fields.One2many('bao_cao_du_an', 'du_an_id', string='Báo Cáo')
    tien_do_ids = fields.One2many('tien_do_du_an', 'du_an_id', string='Tiến Độ')
    chi_phi_ids = fields.One2many('chi_phi_du_an', 'du_an_id', string="Chi Phí Dự Án")

    @api.depends('chi_phi_ids.so_tien')
    def _compute_so_tien(self):
        """Tính tổng số tiền của tất cả các chi phí liên quan đến dự án"""
        for record in self:
            record.so_tien = sum(record.chi_phi_ids.mapped('so_tien'))

    @api.depends('ngay_ket_thuc')
    def _compute_so_ngay_con_lai(self):
        for record in self:
            if record.ngay_ket_thuc:
                so_ngay_con_lai = (record.ngay_ket_thuc - date.today()).days
                record.so_ngay_con_lai = so_ngay_con_lai
                
                # Cập nhật trạng thái dựa trên số ngày còn lại
                if so_ngay_con_lai > 0:
                    if so_ngay_con_lai > 90:
                        record.trang_thai = 'chuẩn_bị'
                    elif 5 < so_ngay_con_lai <= 90:
                        record.trang_thai = 'dang_thuc_hien'
                    elif so_ngay_con_lai <= 5:
                        record.trang_thai = 'hoan_thanh'
                else:
                    record.trang_thai = 'dung'  # Trạng thái là "Dừng lại" nếu số ngày còn lại <= 0
            else:
                record.so_ngay_con_lai = 0
                record.trang_thai = 'dung'  # Trạng thái mặc định nếu không có ngày kết thúc
                