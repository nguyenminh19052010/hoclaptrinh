import pygame, sys

pygame.init()
man_hinh = pygame.display.set_mode((400, 300))
phong = pygame.font.SysFont("arial", 20)
o_nhap, nut = pygame.Rect(100, 80, 200, 40), pygame.Rect(100, 150, 200, 40)
van_ban, dang_chon = "", False

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            dang_chon = o_nhap.collidepoint(e.pos)
            if nut.collidepoint(e.pos): print("Nội dung:", van_ban)
        if e.type == pygame.KEYDOWN and dang_chon:
            van_ban = van_ban[:-1] if e.key == pygame.K_BACKSPACE else van_ban + e.unicode

    man_hinh.fill((240, 240, 240))
    pygame.draw.rect(man_hinh, (255, 255, 255), o_nhap)
    pygame.draw.rect(man_hinh, (0, 120, 255) if dang_chon else (180, 180, 180), o_nhap, 2)
    man_hinh.blit(phong.render(van_ban, True, (0, 0, 0)), (o_nhap.x + 10, o_nhap.y + 10))

    pygame.draw.rect(man_hinh, (0, 120, 255), nut)
    man_hinh.blit(phong.render("Bấm vào đây", True, (255, 255, 255)), (nut.x + 45, nut.y + 10))
    pygame.display.flip()
