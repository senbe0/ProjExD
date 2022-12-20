import sys
import os
import random

# import basic pygame modules
import pygame as pg

# 使用する音源のパス
main_dir = os.path.split(os.path.abspath(__file__))[0]
file_shot = os.path.join(main_dir, "data", "boom.wav")
file_walk = os.path.join(main_dir, "data", "whiff.wav")

# ベース画面クラス
class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 

# 操作キャラクター
class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
                walk_sound.play()
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
                walk_sound.play()
        self.blit(scr)                    

# 爆弾クラス
class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

# 敵キャラを追加する。敵キャラの大きさに合わせて、難易度向上。
class Enemy:
    def __init__(self, enemy_path, vxy, scr:Screen):
        self.sfc = pg.image.load(enemy_path)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

# 壁との衝突判定
def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
        shoot_sound.play()
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
        shoot_sound.play()
    return yoko, tate
    

def main():
    clock =pg.time.Clock()

    # 練習１
    scr = Screen("逃げろ！こうかとん", (1300,700), "fig/pg_bg.jpg")

    # 操作キャラクター
    kkt = Bird("fig/6.png", 2.0, (900,400))
    kkt.update(scr)

    # 爆弾
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    bkd.update(scr)

    # 敵キャラ、大きさに合わせて難易度調整可能
    # ※実行環境に応じて、ファイルの読み込みパスに注意
    enemy = Enemy("data/danger.gif", (+1, +1), scr)
    enemy.update(scr) 

    # 練習２
    while True:        
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)
        bkd.update(scr)
        enemy.update(scr) 

        # キャラクターとの衝突判定
        if kkt.rct.colliderect(bkd.rct):
            return
        if kkt.rct.colliderect(enemy.rct):
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    # サウンド読み込み前の初期設定
    pg.mixer.init()
    # サウンド読み込み
    shoot_sound = pg.mixer.Sound(file_shot)
    walk_sound = pg.mixer.Sound(file_walk)
    main()
    pg.quit()
    sys.exit()