import pygame
import sys

pygame.init()
man_hinh = pygame.display.set_mode((450, 350))
pygame.display.set_caption("He thong Tai Khoan")
phong = pygame.font.SysFont("arial", 18)

danh_sach = {"admin": "Admin@123"}
trang = "dn"
dang_chon = ""
thong_bao = ""

tk_dn, mk_dn = "", ""
tk_dk, mk_dk, nmk_dk = "", "", ""

o_tk_dn = pygame.Rect(125, 60, 200, 35)
o_mk_dn = pygame.Rect(125, 110, 200, 35)
nut_dn = pygame.Rect(125, 170, 200, 40)
nut_qua_dk = pygame.Rect(125, 230, 200, 30)

o_tk_dk = pygame.Rect(125, 45, 200, 35)
o_mk_dk = pygame.Rect(125, 90, 200, 35)
o_nmk_dk = pygame.Rect(125, 135, 200, 35)
nut_dk = pygame.Rect(125, 190, 200, 40)
nut_qua_dn = pygame.Rect(125, 245, 200, 30)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            if trang == "dn":
                if o_tk_dn.collidepoint(e.pos):
                    dang_chon = "tk_dn"
                elif o_mk_dn.collidepoint(e.pos):
                    dang_chon = "mk_dn"
                else:
                    dang_chon = ""

                if nut_dn.collidepoint(e.pos):
                    if not tk_dn or not mk_dn:
                        thong_bao = "Vui long nhap du thong tin!"
                    elif danh_sach.get(tk_dn) == mk_dn:
                        thong_bao = "Dang nhap thanh cong!"
                    else:
                        thong_bao = "Sai tai khoan hoac mat khau!"

                elif nut_qua_dk.collidepoint(e.pos):
                    trang = "dk"
                    thong_bao = ""
                    dang_chon = ""

            elif trang == "dk":
                if o_tk_dk.collidepoint(e.pos):
                    dang_chon = "tk_dk"
                elif o_mk_dk.collidepoint(e.pos):
                    dang_chon = "mk_dk"
                elif o_nmk_dk.collidepoint(e.pos):
                    dang_chon = "nmk_dk"
                else:
                    dang_chon = ""

                if nut_dk.collidepoint(e.pos):
                    co_hoa = any(c.isupper() for c in mk_dk)
                    co_thuong = any(c.islower() for c in mk_dk)
                    co_so = any(c.isdigit() for c in mk_dk)
                    co_dac_biet = any(not c.isalnum() for c in mk_dk)

                    if not tk_dk or not mk_dk:
                        thong_bao = "Vui long nhap du thong tin!"
                    elif tk_dk in danh_sach:
                        thong_bao = "Tai khoan da ton tai!"
                    elif mk_dk != nmk_dk:
                        thong_bao = "Mat khau nhap lai khong khop!"
                    elif len(mk_dk) < 8:
                        thong_bao = "Mat khau phai tu 8 ky tu tro len!"
                    elif not co_hoa:
                        thong_bao = "Mat khau phai co it nhat 1 chu in hoa!"
                    elif not co_thuong:
                        thong_bao = "Mat khau phai co it nhat 1 chu in thuong!"
                    elif not co_so:
                        thong_bao = "Mat khau phai co it nhat 1 chu so!"
                    elif not co_dac_biet:
                        thong_bao = "Mat khau phai co 1 ky tu dac biet (!@#...)!"
                    else:
                        danh_sach[tk_dk] = mk_dk
                        thong_bao = "Dang ky thanh cong! Hay dang nhap."
                        trang = "dn"
                        tk_dn = tk_dk
                        mk_dn = ""

                elif nut_qua_dn.collidepoint(e.pos):
                    trang = "dn"
                    thong_bao = ""
                    dang_chon = ""

        if e.type == pygame.KEYDOWN and dang_chon:
            if dang_chon == "tk_dn":
                if e.key == pygame.K_BACKSPACE:
                    tk_dn = tk_dn[:-1]
                elif e.unicode.isprintable():
                    tk_dn += e.unicode
            elif dang_chon == "mk_dn":
                if e.key == pygame.K_BACKSPACE:
                    mk_dn = mk_dn[:-1]
                elif e.unicode.isprintable():
                    mk_dn += e.unicode
            elif dang_chon == "tk_dk":
                if e.key == pygame.K_BACKSPACE:
                    tk_dk = tk_dk[:-1]
                elif e.unicode.isprintable():
                    tk_dk += e.unicode
            elif dang_chon == "mk_dk":
                if e.key == pygame.K_BACKSPACE:
                    mk_dk = mk_dk[:-1]
                elif e.unicode.isprintable():
                    mk_dk += e.unicode
            elif dang_chon == "nmk_dk":
                if e.key == pygame.K_BACKSPACE:
                    nmk_dk = nmk_dk[:-1]
                elif e.unicode.isprintable():
                    nmk_dk += e.unicode

    man_hinh.fill((240, 240, 240))

    if trang == "dn":
        pygame.draw.rect(man_hinh, (255, 255, 255), o_tk_dn)
        pygame.draw.rect(man_hinh, (0, 0, 0), o_tk_dn, 1)
        txt_tk = phong.render(tk_dn if tk_dn else "Tai khoan", True, (0, 0, 0) if tk_dn else (150, 150, 150))
        man_hinh.blit(txt_tk, (o_tk_dn.x + 5, o_tk_dn.y + 5))

        pygame.draw.rect(man_hinh, (255, 255, 255), o_mk_dn)
        pygame.draw.rect(man_hinh, (0, 0, 0), o_mk_dn, 1)
        txt_mk = phong.render("*" * len(mk_dn) if mk_dn else "Mat khau", True, (0, 0, 0) if mk_dn else (150, 150, 150))
        man_hinh.blit(txt_mk, (o_mk_dn.x + 5, o_mk_dn.y + 5))

        pygame.draw.rect(man_hinh, (0, 120, 255), nut_dn)
        txt_nut = phong.render("Dang nhap", True, (255, 255, 255))
        man_hinh.blit(txt_nut, (nut_dn.x + 50, nut_dn.y + 8))

        txt_chuyen = phong.render("Chua co tai khoan? Dang ky", True, (0, 100, 200))
        man_hinh.blit(txt_chuyen, (nut_qua_dk.x - 20, nut_qua_dk.y + 5))

    elif trang == "dk":
        pygame.draw.rect(man_hinh, (255, 255, 255), o_tk_dk)
        pygame.draw.rect(man_hinh, (0, 0, 0), o_tk_dk, 1)
        txt_tk = phong.render(tk_dk if tk_dk else "Tai khoan moi", True, (0, 0, 0) if tk_dk else (150, 150, 150))
        man_hinh.blit(txt_tk, (o_tk_dk.x + 5, o_tk_dk.y + 5))

        pygame.draw.rect(man_hinh, (255, 255, 255), o_mk_dk)
        pygame.draw.rect(man_hinh, (0, 0, 0), o_mk_dk, 1)
        txt_mk = phong.render("*" * len(mk_dk) if mk_dk else "Mat khau", True, (0, 0, 0) if mk_dk else (150, 150, 150))
        man_hinh.blit(txt_mk, (o_mk_dk.x + 5, o_mk_dk.y + 5))

        pygame.draw.rect(man_hinh, (255, 255, 255), o_nmk_dk)
        pygame.draw.rect(man_hinh, (0, 0, 0), o_nmk_dk, 1)
        txt_nmk = phong.render("*" * len(nmk_dk) if nmk_dk else "Nhap lai mat khau", True, (0, 0, 0) if nmk_dk else (150, 150, 150))
        man_hinh.blit(txt_nmk, (o_nmk_dk.x + 5, o_nmk_dk.y + 5))

        pygame.draw.rect(man_hinh, (0, 180, 100), nut_dk)
        txt_nut = phong.render("Dang ky", True, (255, 255, 255))
        man_hinh.blit(txt_nut, (nut_dk.x + 60, nut_dk.y + 8))

        txt_chuyen = phong.render("Quay lai Dang nhap", True, (0, 100, 200))
        man_hinh.blit(txt_chuyen, (nut_qua_dn.x + 15, nut_qua_dn.y + 5))

    if thong_bao:
        txt_tb = phong.render(thong_bao, True, (200, 0, 0))
        man_hinh.blit(txt_tb, (20, 295))

    pygame.display.flip()