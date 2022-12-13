import pygame as pg
import random
import sys
import time


def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    # 爆弾の大きさ
    big = 2.0
    clock =pg.time.Clock()
    
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1200, 600))
    scrn_rct = scrn_sfc.get_rect()
    # 背景を変更
    pgbg_sfc = pg.image.load("fig/uni.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    
    tori_sfc = pg.image.load("fig/4.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, big)
    tori_rct = tori_sfc.get_rect()
    # 配置を変更
    tori_rct.center = 600, 300
    scrn_sfc.blit(tori_sfc, tori_rct) 

    # bomb1
    bomb_sfc = pg.Surface((20, 20)) 
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 
    vx, vy = +1, +1

    # bomb2
    bomb_sfc2 = pg.Surface((20, 20)) 
    bomb_sfc2.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc2, (255, 0, 0), (10, 10), 10)
    bomb_rct2 = bomb_sfc2.get_rect()
    bomb_rct2.centerx = random.randint(0, scrn_rct.width)
    bomb_rct2.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc2, bomb_rct2) 
    vx2, vy2 = +1, +1

    # bomb3
    bomb_sfc3 = pg.Surface((20, 20)) 
    bomb_sfc3.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc3, (255, 0, 0), (10, 10), 10)
    bomb_rct3 = bomb_sfc3.get_rect()
    bomb_rct3.centerx = random.randint(0, scrn_rct.width)
    bomb_rct3.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc3, bomb_rct3) 
    vx3, vy3 = +1, +1

    
    while True:
        # 動く度にこうかとんが少しずつ大きくなる。
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 
        tori_sfc = pg.image.load("fig/4.png")
        tori_sfc = pg.transform.rotozoom(tori_sfc, 0, big)        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 方向に従って画像を入れ替える
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP]: 
            tori_rct.centery -= 1
            tori_sfc = pg.image.load("fig/6.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, big)
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
            tori_sfc = pg.image.load("fig/8.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, big)        
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
            tori_sfc = pg.image.load("fig/5.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, big)
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
            tori_sfc = pg.image.load("fig/2.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, big)
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1 
   
        scrn_sfc.blit(tori_sfc, tori_rct) 

        # 練習６
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        bomb_rct2.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb_sfc2, bomb_rct2) 
        yoko2, tate2 = check_bound(bomb_rct2, scrn_rct)
        vx2 *= yoko2
        vy2 *= tate2

        bomb_rct3.move_ip(vx3, vy3)
        scrn_sfc.blit(bomb_sfc3, bomb_rct3) 
        yoko3, tate3 = check_bound(bomb_rct3, scrn_rct)
        vx3 *= yoko3
        vy3 *= tate3

        # 練習８
        if tori_rct.colliderect(bomb_rct):
            tori_sfc = pg.image.load("fig/20.png")
            scrn_sfc.blit(tori_sfc, tori_rct) 
            pg.display.update()
            time.sleep(3)
            return
            
        if tori_rct.colliderect(bomb_rct2):
            tori_sfc = pg.image.load("fig/20.png")
            scrn_sfc.blit(tori_sfc, tori_rct) 
            pg.display.update()
            time.sleep(3)
            return
            
        if tori_rct.colliderect(bomb_rct3):
            tori_sfc = pg.image.load("fig/20.png")
            scrn_sfc.blit(tori_sfc, tori_rct) 
            pg.display.update()
            time.sleep(3)
            return
        

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()