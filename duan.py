import pygame
import sys

pygame.init()
man_hinh = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Dang nhap")
phong = pygame.font.SysFont("arial", 20)

o_tk = pygame.Rect(100, 50, 200, 35)
o_mk = pygame.Rect(100, 100, 200, 35)
nut = pygame.Rect(100, 160, 200, 40)

tk = ""
mk = ""
dang_chon = ""
thong_bao = ""

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            if o_tk.collidepoint(e.pos):
                dang_chon = "tk"
            elif o_mk.collidepoint(e.pos):
                dang_chon = "mk"
            else:
                dang_chon = ""

            if nut.collidepoint(e.pos):
                if tk == "admin" and mk == "123456":
                    thong_bao = "Dang nhap thanh cong!"
                else:
                    thong_bao = "Sai tai khoan hoac mat khau!"

        if e.type == pygame.KEYDOWN:
            if dang_chon == "tk":
                if e.key == pygame.K_BACKSPACE:
                    tk = tk[:-1]
                elif e.unicode.isprintable():
                    tk += e.unicode
            elif dang_chon == "mk":
                if e.key == pygame.K_BACKSPACE:
                    mk = mk[:-1]
                elif e.unicode.isprintable():
                    mk += e.unicode

    man_hinh.fill((240, 240, 240))

    pygame.draw.rect(man_hinh, (255, 255, 255), o_tk)
    pygame.draw.rect(man_hinh, (0, 0, 0), o_tk, 1)
    hien_tk = phong.render(tk if tk else "Tai khoan", True, (0, 0, 0) if tk else (150, 150, 150))
    man_hinh.blit(hien_tk, (o_tk.x + 5, o_tk.y + 5))

    pygame.draw.rect(man_hinh, (255, 255, 255), o_mk)
    pygame.draw.rect(man_hinh, (0, 0, 0), o_mk, 1)
    hien_mk = phong.render("*" * len(mk) if mk else "Mat khau", True, (0, 0, 0) if mk else (150, 150, 150))
    man_hinh.blit(hien_mk, (o_mk.x + 5, o_mk.y + 5))

    pygame.draw.rect(man_hinh, (0, 120, 255), nut)
    hien_nut = phong.render("Dang nhap", True, (255, 255, 255))
    man_hinh.blit(hien_nut, (nut.x + 50, nut.y + 8))

    if thong_bao:
        hien_tb = phong.render(thong_bao, True, (200, 0, 0))
        man_hinh.blit(hien_tb, (60, 220))

    pygame.display.flip()