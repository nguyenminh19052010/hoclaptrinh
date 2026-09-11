import pygame
import sys

pygame.init()
chieu_rong, chieu_cao = 700, 550
man_hinh = pygame.display.set_mode((chieu_rong, chieu_cao))
pygame.display.set_caption("Mini Social - Login System")
dong_ho = pygame.time.Clock()

phong_chu = pygame.font.SysFont("arial", 22)
phong_nho = pygame.font.SysFont("arial", 17)
phong_tieu_de = pygame.font.SysFont("arial", 35, bold=True)

mau_trang, mau_den, mau_xam = (255, 255, 255), (30, 30, 30), (120, 120, 120)
xanh_duong, xanh_la, mau_do = (70, 100, 240), (40, 180, 110), (220, 70, 70)
mau_nen = (235, 238, 245)

danh_sach_tai_khoan = {"admin": "123456"}
trang = "login"
tai_khoan_hien_tai = ""
thong_bao = ""

class ONhap:
    def __init__(self, x, y, goi_y, mat_khau=False):
        self.khung = pygame.Rect(x, y, 300, 50)
        self.noi_dung = ""
        self.goi_y = goi_y
        self.mat_khau = mat_khau
        self.dang_chon = False

    def xu_ly(self, su_kien):
        if su_kien.type == pygame.MOUSEBUTTONDOWN:
            self.dang_chon = self.khung.collidepoint(su_kien.pos)
        elif su_kien.type == pygame.KEYDOWN and self.dang_chon:
            if su_kien.key == pygame.K_BACKSPACE:
                self.noi_dung = self.noi_dung[:-1]
            elif len(self.noi_dung) < 25 and su_kien.unicode.isprintable():
                self.noi_dung += su_kien.unicode

    def ve(self, man_hinh):
        mau_vien = xanh_duong if self.dang_chon else (190, 195, 210)
        pygame.draw.rect(man_hinh, mau_trang, self.khung, border_radius=10)
        pygame.draw.rect(man_hinh, mau_vien, self.khung, 2, border_radius=10)
        
        van_ban_hien_thi = "*" * len(self.noi_dung) if self.mat_khau else self.noi_dung
        hinh_anh_chu = phong_chu.render(van_ban_hien_thi, True, mau_den) if van_ban_hien_thi else phong_nho.render(self.goi_y, True, mau_xam)
        man_hinh.blit(hinh_anh_chu, (self.khung.x + 15, self.khung.y + (50 - hinh_anh_chu.get_height()) // 2))

    def xoa(self):
        self.noi_dung = ""

def ve_chu(noi_dung, phong, mau, tam):
    hinh_anh_chu = phong.render(noi_dung, True, mau)
    man_hinh.blit(hinh_anh_chu, hinh_anh_chu.get_rect(center=tam))

def ve_nut(khung, noi_dung, mau=xanh_duong):
    di_chuot = khung.collidepoint(pygame.mouse.get_pos())
    mau_nut = (50, 75, 210) if di_chuot and mau == xanh_duong else mau
    pygame.draw.rect(man_hinh, mau_nut, khung, border_radius=10)
    ve_chu(noi_dung, phong_chu, mau_trang, khung.center)

dn_tai_khoan = ONhap(200, 220, "Tên đăng nhập")
dn_mat_khau = ONhap(200, 290, "Mật khẩu", True)
nut_dang_nhap = pygame.Rect(200, 365, 300, 50)
nut_sang_dang_ky = pygame.Rect(200, 440, 300, 30)

dk_tai_khoan = ONhap(200, 180, "Tên đăng nhập")
dk_mat_khau = ONhap(200, 250, "Mật khẩu", True)
dk_nhap_lai_mk = ONhap(200, 320, "Nhập lại mật khẩu", True)
nut_dang_ky = pygame.Rect(200, 395, 300, 50)
nut_sang_dang_nhap = pygame.Rect(200, 465, 300, 30)

nut_dang_xuat = pygame.Rect(250, 370, 200, 50)

while True:
    for su_kien in pygame.event.get():
        if su_kien.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if trang == "login":
            dn_tai_khoan.xu_ly(su_kien)
            dn_mat_khau.xu_ly(su_kien)
            if su_kien.type == pygame.MOUSEBUTTONDOWN:
                if nut_dang_nhap.collidepoint(su_kien.pos):
                    tk, mk = dn_tai_khoan.noi_dung.strip(), dn_mat_khau.noi_dung
                    if not tk or not mk:
                        thong_bao = "Vui lòng nhập đầy đủ thông tin!"
                    elif tk not in danh_sach_tai_khoan:
                        thong_bao = "Tài khoản không tồn tại!"
                    elif danh_sach_tai_khoan[tk] != mk:
                        thong_bao = "Mật khẩu không đúng!"
                    else:
                        tai_khoan_hien_tai, thong_bao, trang = tk, "", "home"
                elif nut_sang_dang_ky.collidepoint(su_kien.pos):
                    thong_bao, trang = "", "register"

        elif trang == "register":
            dk_tai_khoan.xu_ly(su_kien)
            dk_mat_khau.xu_ly(su_kien)
            dk_nhap_lai_mk.xu_ly(su_kien)
            if su_kien.type == pygame.MOUSEBUTTONDOWN:
                if nut_dang_ky.collidepoint(su_kien.pos):
                    tk, mk, nmk = dk_tai_khoan.noi_dung.strip(), dk_mat_khau.noi_dung, dk_nhap_lai_mk.noi_dung
                    if not tk or not mk:
                        thong_bao = "Vui lòng nhập đầy đủ thông tin!"
                    elif tk in danh_sach_tai_khoan:
                        thong_bao = "Tên đăng nhập đã tồn tại!"
                    elif len(tk) < 3:
                        thong_bao = "Tên đăng nhập phải từ 3 ký tự!"
                    elif len(mk) < 4:
                        thong_bao = "Mật khẩu phải từ 4 ký tự!"
                    elif mk != nmk:
                        thong_bao = "Mật khẩu nhập lại không đúng!"
                    else:
                        danh_sach_tai_khoan[tk] = mk
                        dn_tai_khoan.noi_dung = tk
                        dn_mat_khau.xoa()
                        for o_nhap in (dk_tai_khoan, dk_mat_khau, dk_nhap_lai_mk):
                            o_nhap.xoa()
                        thong_bao, trang = "", "login"
                elif nut_sang_dang_nhap.collidepoint(su_kien.pos):
                    thong_bao, trang = "", "login"

        elif trang == "home":
            if su_kien.type == pygame.MOUSEBUTTONDOWN and nut_dang_xuat.collidepoint(su_kien.pos):
                dn_mat_khau.xoa()
                tai_khoan_hien_tai, thong_bao, trang = "", "", "login"

    man_hinh.fill(mau_nen)

    if trang == "login":
        ve_chu("MINI SOCIAL", phong_tieu_de, xanh_duong, (350, 80))
        ve_chu("Kết nối - Chia sẻ - Khám phá", phong_nho, mau_xam, (350, 125))
        ve_chu("ĐĂNG NHẬP HỆ THỐNG", phong_chu, mau_den, (350, 175))
        dn_tai_khoan.ve(man_hinh)
        dn_mat_khau.ve(man_hinh)
        ve_nut(nut_dang_nhap, "ĐĂNG NHẬP")
        ve_chu("Chưa có tài khoản?  ĐĂNG KÝ", phong_nho, xanh_duong, nut_sang_dang_ky.center)

    elif trang == "register":
        ve_chu("TẠO TÀI KHOẢN", phong_tieu_de, xanh_duong, (350, 80))
        ve_chu("Đăng ký tài khoản Mini Social", phong_nho, mau_xam, (350, 120))
        dk_tai_khoan.ve(man_hinh)
        dk_mat_khau.ve(man_hinh)
        dk_nhap_lai_mk.ve(man_hinh)
        ve_nut(nut_dang_ky, "ĐĂNG KÝ", xanh_la)
        ve_chu("< Quay lại đăng nhập", phong_nho, xanh_duong, nut_sang_dang_nhap.center)

    elif trang == "home":
        ve_chu("MINI SOCIAL", phong_tieu_de, xanh_duong, (350, 100))
        ve_chu(f"Xin chào, {tai_khoan_hien_tai}!", phong_chu, mau_den, (350, 210))
        ve_chu("Bạn đã đăng nhập thành công vào hệ thống.", phong_nho, mau_xam, (350, 260))
        pygame.draw.circle(man_hinh, xanh_duong, (350, 320), 35)
        ve_chu(tai_khoan_hien_tai[0].upper() if tai_khoan_hien_tai else "U", phong_chu, mau_trang, (350, 320))
        ve_nut(nut_dang_xuat, "ĐĂNG XUẤT", mau_do)

    if thong_bao and trang != "home":
        ve_chu(thong_bao, phong_nho, mau_do, (350, 510))

    pygame.display.flip()
    dong_ho.tick(60)