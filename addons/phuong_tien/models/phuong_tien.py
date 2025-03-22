from odoo import models, fields, api


class phuong_tien(models.Model):
    _name = 'phuong_tien'
    _description = 'Bảng chứa thông tin phương tiện'

    ma_dinh_danh_phuong_tien = fields.Char("Mã định danh phương tiện", required=True)
    ten_chu_xe = fields.Char("Tên chủ xe")
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
    gia_cho_thue_theo_gio = fields.Char("Giá cho thuê theo giờ: ")
    gia_cho_thue_theo_ngay = fields.Char("Giá cho thuê theo ngày: ")
    gia_ban_xe = fields.Char("Giá bán xe(đã bao gồm thuế)")
    hop_dong_mua_ban_xe = fields.Char("Hợp đồng mua bán xe ")
    tinh_trang_xe = fields.Char("Tình trạng xe hiện tại ")
    hinh_anh_xe_mot = fields.Binary("Hình anh xe 1")
    hinh_anh_xe_hai = fields.Binary("Hình anh xe 2")
    hinh_anh_xe_ba = fields.Binary("Hình ảnh xe 3")
    hinh_anh_xe_bon = fields.Binary("Hình ảnh xe 4")
