from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BaoCaoDuAn(models.Model):
    _name = 'bao_cao_du_an'
    _description = 'Báo Cáo Dự Án'

    du_an_id = fields.Many2one('du_an', string='Dự Án', required=True)
    tieu_de = fields.Char(string='Tiêu Đề', required=True)
    mo_ta = fields.Text(string='Mô Tả')
    ngay_bao_cao = fields.Date(string='Ngày Báo Cáo')
    
    ten_du_an = fields.Char(related='du_an_id.ten_du_an', string='Tên Dự Án', store=True)
    ma_du_an = fields.Char(related='du_an_id.ma_du_an', string='Mã Dự Án', store=True)
    ngay_bat_dau = fields.Date(related='du_an_id.ngay_bat_dau', string='Ngày bắt đầu')
    ngay_ket_thuc = fields.Date(related='du_an_id.ngay_ket_thuc', string='Ngày kết thúc')
    @api.constrains('ngay_bao_cao', 'du_an_id')
    def _check_ngay_bao_cao(self):
        for record in self:
            if record.du_an_id:
                if record.ngay_bao_cao:
                    if record.ngay_bao_cao < record.du_an_id.ngay_bat_dau or record.ngay_bao_cao > record.du_an_id.ngay_ket_thuc:
                        raise ValidationError(
                            "Ngày báo cáo phải nằm trong khoảng từ ngày bắt đầu đến ngày kết thúc của dự án."
                        )