import pygame
import sys

pygame.init()
man_hinh = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Dang Nhap & Dang Ky")
phong = pygame.font.SysFont("arial", 20)

danh_sach = {"admin": "123456"}
trang = "dn"
tai_khoan = ""
thong_bao = ""

dn_tk = pygame.Rect(150, 80, 200, 35)
dn_mk = pygame.Rect(150, 130, 200, 35)
nut_dn = pygame.Rect(150, 190, 200, 35)
nut_sang_dk = pygame.Rect(150, 240, 200, 30)

dk_tk = pygame.Rect(150, 80, 200, 35)
dk_mk = pygame.Rect(150, 130, 200, 35)
dk_nmk = pygame.Rect(150, 180, 200, 35)
nut_dk = pygame.Rect(150, 230, 200, 35)
nut_sang_dn = pygame.Rect(150, 280, 200, 30)

nut_dx = pygame.Rect(150, 180, 200, 35)

van_ban_dn_tk, van_ban_dn_mk = "", ""
van_ban_dk_tk, van_ban_dk_mk, van_ban_dk_nmk = "", "", ""
o_dang_nhap = ""

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            if trang == "dn":
                if dn_tk.collidepoint(e.pos):
                    o_dang_nhap = "dn_tk"
                elif dn_mk.collidepoint(e.pos):
                    o_dang_nhap = "dn_mk"
                else:
                    o_dang_nhap = ""

                if nut_dn.collidepoint(e.pos):
                    if not van_ban_dn_tk or not van_ban_dn_mk:
                        thong_bao = "Vui long nhap du thong tin!"
                    elif danh_sach.get(van_ban_dn_tk) == van_ban_dn_mk:
                        tai_khoan, thong_bao, trang = van_ban_dn_tk, "", "home"
                    else:
                        thong_bao = "Sai tai khoan hoac mat khau!"
                elif nut_sang_dk.collidepoint(e.pos):
                    thong_bao, trang = "", "dk"

            elif trang == "dk":
                if dk_tk.collidepoint(e.pos):
                    o_dang_nhap = "dk_tk"
                elif dk_mk.collidepoint(e.pos):
                    o_dang_nhap = "dk_mk"
                elif dk_nmk.collidepoint(e.pos):
                    o_dang_nhap = "dk_nmk"
                else:
                    o_dang_nhap = ""

                if nut_dk.collidepoint(e.pos):
                    if not van_ban_dk_tk or not van_ban_dk_mk:
                        thong_bao = "Vui long nhap du thong tin!"
                    elif van_ban_dk_tk in danh_sach:
                        thong_bao = "Tai khoan da ton tai!"
                    elif van_ban_dk_mk != van_ban_dk_nmk:
                        thong_bao = "Mat khau nhap lai khong khop!"
                    else:
                        danh_sach[van_ban_dk_tk] = van_ban_dk_mk
                        thong_bao, trang = "Dang ky thanh cong!", "dn"
                elif nut_sang_dn.collidepoint(e.pos):
                    thong_bao, trang = "", "dn"

            elif trang == "home" and nut_dx.collidepoint(e.pos):
                tai_khoan, thong_bao, trang = "", "", "dn"

        if e.type == pygame.KEYDOWN and o_dang_nhap:
            def cap_nhat(val):
                return val[:-1] if e.key == pygame.K_BACKSPACE else (val + e.unicode if len(val) < 20 and e.unicode.isprintable() else val)

            if o_dang_nhap == "dn_tk":
                van_ban_dn_tk = cap_nhat(van_ban_dn_tk)
            elif o_dang_nhap == "dn_mk":
                van_ban_dn_mk = cap_nhat(van_ban_dn_mk)
            elif o_dang_nhap == "dk_tk":
                van_ban_dk_tk = cap_nhat(van_ban_dk_tk)
            elif o_dang_nhap == "dk_mk":
                van_ban_dk_mk = cap_nhat(van_ban_dk_mk)
            elif o_dang_nhap == "dk_nmk":
                van_ban_dk_nmk = cap_nhat(van_ban_dk_nmk)

    man_hinh.fill((240, 240, 240))

    if trang == "dn":
        man_hinh.blit(phong.render("DANG NHAP", True, (0, 0, 0)), (200, 30))
        for r, val, txt, lay_focus in [(dn_tk, van_ban_dn_tk, "Tai khoan", o_dang_nhap == "dn_tk"), (dn_mk, "*" * len(van_ban_dn_mk), "Mat khau", o_dang_nhap == "dn_mk")]:
            pygame.draw.rect(man_hinh, (255, 255, 255), r)
            pygame.draw.rect(man_hinh, (0, 120, 255) if lay_focus else (180, 180, 180), r, 2)
            man_hinh.blit(phong.render(val if val else txt, True, (0, 0, 0) if val else (150, 150, 150)), (r.x + 5, r.y + 5))

        pygame.draw.rect(man_hinh, (0, 120, 255), nut_dn)
        man_hinh.blit(phong.render("Dang nhap", True, (255, 255, 255)), (nut_dn.x + 50, nut_dn.y + 5))
        man_hinh.blit(phong.render("Chua co tai khoan? Dang ky", True, (0, 100, 200)), (nut_sang_dk.x - 20, nut_sang_dk.y + 5))

    elif trang == "dk":
        man_hinh.blit(phong.render("DANG KY", True, (0, 0, 0)), (210, 30))
        for r, val, txt, lay_focus in [(dk_tk, van_ban_dk_tk, "Tai khoan", o_dang_nhap == "dk_tk"), (dk_mk, "*" * len(van_ban_dk_mk), "Mat khau", o_dang_nhap == "dk_mk"), (dk_nmk, "*" * len(van_ban_dk_nmk), "Nhap lai MK", o_dang_nhap == "dk_nmk")]:
            pygame.draw.rect(man_hinh, (255, 255, 255), r)
            pygame.draw.rect(man_hinh, (0, 120, 255) if lay_focus else (180, 180, 180), r, 2)
            man_hinh.blit(phong.render(val if val else txt, True, (0, 0, 0) if val else (150, 150, 150)), (r.x + 5, r.y + 5))

        pygame.draw.rect(man_hinh, (0, 180, 100), nut_dk)
        man_hinh.blit(phong.render("Dang ky", True, (255, 255, 255)), (nut_dk.x + 60, nut_dk.y + 5))
        man_hinh.blit(phong.render("Quay lai dang nhap", True, (0, 100, 200)), (nut_sang_dn.x + 10, nut_sang_dn.y + 5))

    elif trang == "home":
        man_hinh.blit(phong.render(f"Xin chao, {tai_khoan}!", True, (0, 0, 0)), (180, 100))
        pygame.draw.rect(man_hinh, (220, 50, 50), nut_dx)
        man_hinh.blit(phong.render("Dang xuat", True, (255, 255, 255)), (nut_dx.x + 55, nut_dx.y + 5))

    if thong_bao:
        man_hinh.blit(phong.render(thong_bao, True, (220, 0, 0)), (130, 340))

    pygame.display.flip()