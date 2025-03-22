from odoo import models, fields, api
from odoo.exceptions import ValidationError

class NhiemVuDuAn(models.Model):
    _name = 'nhiem_vu_du_an'
    _description = 'Nhiệm Vụ Dự Án'

    du_an_id = fields.Many2one('du_an', string='Dự Án', required=True)
    bao_cao_id = fields.Many2one('bao_cao_du_an', string='Báo Cáo Dự Án', required=True)
    tieu_de = fields.Char(string='Tiêu Đề', required=True)
    mo_ta = fields.Text(string='Mô Tả')
    trang_thai = fields.Selection([
        ('lap_ke_hoach', 'Lập kế hoạch'),
        ('dang_thuc_hien', 'Đang thực hiện'),
        ('hoan_thanh', 'Hoàn thành'),
        ('dung', 'Dừng lại')
    ], string="Trạng thái", default='lap_ke_hoach')

    @api.constrains('du_an_id', 'bao_cao_id')
    def _check_du_an_bao_cao(self):
        for record in self:
            if record.bao_cao_id and record.bao_cao_id.du_an_id != record.du_an_id:
                raise ValidationError(
                    "Báo cáo không liên kết với dự án này."
                )