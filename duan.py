import pygame
import sys

pygame.init()
man_hinh = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Giao diện cơ bản")
phong_chu = pygame.font.SysFont("arial", 20)

o_nhap = pygame.Rect(100, 80, 200, 40)
nut = pygame.Rect(100, 150, 200, 40)

van_ban = ""
dang_nhap_chuot = False

while True:
    for su_kien in pygame.event.get():
        if su_kien.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if su_kien.type == pygame.MOUSEBUTTONDOWN:
            dang_nhap_chuot = o_nhap.collidepoint(su_kien.pos)
            if nut.collidepoint(su_kien.pos):
                print("Đã bấm nút! Nội dung ô nhập:", van_ban)

        if su_kien.type == pygame.KEYDOWN and dang_nhap_chuot:
            if su_kien.key == pygame.K_BACKSPACE:
                van_ban = van_ban[:-1]
            elif su_kien.unicode.isprintable():
                van_ban += su_kien.unicode

    man_hinh.fill((240, 240, 240))

    mau_vien = (0, 120, 255) if dang_nhap_chuot else (180, 180, 180)
    pygame.draw.rect(man_hinh, (255, 255, 255), o_nhap)
    pygame.draw.rect(man_hinh, mau_vien, o_nhap, 2)
    hinh_van_ban = phong_chu.render(van_ban, True, (0, 0, 0))
    man_hinh.blit(hinh_van_ban, (o_nhap.x + 10, o_nhap.y + 10))

    pygame.draw.rect(man_hinh, (0, 120, 255), nut)
    hinh_nut = phong_chu.render("Bấm vào đây", True, (255, 255, 255))
    man_hinh.blit(hinh_nut, (nut.x + 45, nut.y + 10))

    pygame.display.flip()