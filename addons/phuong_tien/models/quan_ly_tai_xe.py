from odoo import models, fields, api


class quan_ly_tai_xe(models.Model):
    _name = 'quan_ly_tai_xe'
    _description = 'Quản lý tài xế'

    ma_dinh_danh_tai_xe = fields.Char("Mã định danh tài xế", required=True)
    ten_tai_xe = fields.Char("Tên tài xế")
    ten_phuong_tien = fields.Char("Tên phương tiện")
    ngay_mua_xe = fields.Date("Ngày mua xe")
    dia_chi = fields.Char("Địa chỉ")
    nhan_hieu = fields.Char("Nhãn hiệu")
    mau_son = fields.Char("Màu sơn")
    bien_so_dang_ky = fields.Char("Biển số đăng ký")
    dang_ky_lan_dau_ngay = fields.Date("Đăng ký lần đầu ngày:")
    so_may = fields.Char("Số máy")
    so_khung = fields.Char("Số khung")
    dung_tich = fields.Char("Dung tích")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    lich_lam_viec = fields.Char("Lịch làm việc")
    tinh_trang_xe = fields.Char("Tình trạng xe hiện tại ")
    hinh_anh_tai_xe = fields.Binary("Hình ảnh tài xế")
    hinh_anh_xe_mot = fields.Binary("Hình anh xe 1")
    hinh_anh_xe_hai = fields.Binary("Hình anh xe 2")
    hinh_anh_xe_ba = fields.Binary("Hình ảnh xe 3")
    hinh_anh_xe_bon = fields.Binary("Hình ảnh xe 4")
