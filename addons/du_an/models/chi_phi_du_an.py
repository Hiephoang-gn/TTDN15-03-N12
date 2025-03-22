from odoo import models, fields, api

class ChiPhiDuAn(models.Model):
    _name = 'chi_phi_du_an'
    _description = 'Bảng chi phí dự án'

    name = fields.Char("Mã Chi Phí", readonly=True, copy=False, index=True, default="Mới")
    ten_chi_phi = fields.Char("Tên chi phí", required=True)
    du_an_id = fields.Many2one('du_an', string="Dự án", required=True, ondelete='cascade')
    so_tien = fields.Float("Số tiền", required=True)
    loai_chi_phi = fields.Selection([
        ('nhan_cong', 'Nhân công'),
        ('vat_lieu', 'Vật liệu'),
        ('thiet_bi', 'Thiết bị'),
        ('khac', 'Khác')
    ], string="Loại chi phí", required=True)
    ngay_chi = fields.Date("Ngày chi", default=fields.Date.context_today)
    ghi_chu = fields.Text("Ghi chú")

    @api.model
    def create(self, vals):
        """Tự động tạo mã chi phí theo định dạng CP-YYYYMMDD-XXX"""
        if vals.get('name', "Mới") == "Mới":
            sequence = self.env['ir.sequence'].next_by_code('chi_phi_du_an') or '000'
            vals['name'] = f"CP-{fields.Date.today().strftime('%Y%m%d')}-{sequence}"
        return super(ChiPhiDuAn, self).create(vals)
