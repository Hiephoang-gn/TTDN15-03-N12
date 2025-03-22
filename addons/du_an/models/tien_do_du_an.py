from odoo import models, fields,api
from odoo.exceptions import ValidationError

class TienDoDuAn(models.Model):
    _name = 'tien_do_du_an'
    _description = 'Tiến Độ Dự Án'

    du_an_id = fields.Many2one('du_an', string='Dự Án', required=True)
    ti_le_tien_do = fields.Float(string='Tiến Độ (%)', required=True)
    ghi_chu = fields.Text(string='Ghi Chú')
    ngay_xac_nhan = fields.Date(string='Ngày Xác Nhận')
    
    ten_du_an = fields.Char(related='du_an_id.ten_du_an', string='Tên Dự Án', store=True)
    ma_du_an = fields.Char(related='du_an_id.ma_du_an', string='Mã Dự Án', store=True)

    @api.constrains('ti_le_tien_do')
    def _check_ti_le_tien_do(self):
        for record in self:
            if record.ti_le_tien_do < 0 or record.ti_le_tien_do > 100:
                raise ValidationError("Tỉ lệ tiến độ phải nằm trong khoảng từ 0% đến 100%.")