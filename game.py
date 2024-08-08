from pygame import *
import rand
from graph import step
font.init() 
window = display.set_mode((0, 0))
win_width, win_height = display.get_surface().get_size()
display .set_caption("game")
img = image.load("pacman.png")
img = transform.scale(img, (60, 60))
IMG = image.load("pacman2.png")
IMG = transform.scale(IMG, (25, 25))
Bullet = image.load("bullets.png")
Bullet = transform.scale(Bullet, (20, 20))
game = False
x = 0
y = 0
speed = 1
timer = time.Clock()
WIN = image.load("win.png")
WIN = transform.scale(WIN, (1600, 900))
class finish:
    def __init__(self):
        
        self.img = Surface([50,50])
        self.img.fill((0, 255, 0))
        self.rect = Surface([50, 50]).get_rect()
        self.rect.x = 575
        self.rect.y = 525
    def draw(self):
        window.blit(self.img, camera.apply(self))
Finish = finish()
class Wall:
    def __init__(self, x, y, width, height):
        self.w = width
        self.h = height
        self.image = Surface([self.w, self.h])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
     
    def reset(self):
        window.blit(self.image, (camera.apply(self)))
        
xw = 0
yw = 0
ll_sprites = []   
file1 = open('generator.txt', 'r')
for stroc in file1:
    yw += 25
    for j in range(len(stroc)):
        xw += 25
        if stroc[j] == '-':
            sprit = Wall(xw, yw, 25, 25)
            ll_sprites.append(sprit)
    xw = 0

bullets = []
class ball:
    def __init__(self, x, y, q):
        if q == 0:
            self.imag = transform.rotate(Bullet, 90)
        if q == 1:
            self.imag = Bullet
        if q == 2:
            self.imag = transform.rotate(Bullet, -90)
        if q == 3:
            self.imag = transform.flip(Bullet, 1,0)
        self.rect = Bullet.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.q = q
       
            
    def draw(self):
        window.blit(self.imag, camera.apply(self))
    def update(self):
        if self.q == 0:
            self.rect.y -= 12
        if self.q == 1:
            self.rect.x += 12
        if self.q == 2:
            self.rect.y += 12
        if self.q ==3:
            self.rect.x -= 12
k = 50
class Player:
    def __init__(self, img, naprx, napry, life):
        self.img = img
        self.imgro = img
        self.x = 300
        self.y = 325
        self.speed = 2
        self.rect = self.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.naprx = naprx
        self.napry = napry
        self.life = life
        self.firenapr = 1
        self.f1 = font.SysFont(None, 28)
        
        
    def reset(self):
        window.blit(self.imgro, camera.apply(self) )
        window.blit(self.text, (600, 0))
    def update(self):
        global k
        keys =  key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
           self.rect.y = self.rect.y - self.speed
           self.napry =  1
           self.imgro = transform.rotate(self.img, 90)
           self.firenapr = 0
           
        if keys[K_a]  and self.rect.x > 0:
           self.rect.x = self.rect.x - self.speed
           self.naprx = -2
           self.imgro = transform.flip(self.img, 1,0)
           self.firenapr = 3
        if keys[K_s] and self.rect.y < 1940:
           self.rect.y = self.rect.y + self.speed
           self.napry = -1
           self.imgro = transform.rotate(self.img, -90)
           self.firenapr = 2
        if keys[K_d] and self.rect.x < 1940:
           self.rect.x = self.rect.x +  self.speed
           self.naprx = 2
           self.imgro = self.img
           self.firenapr = 1
        if not keys[K_d] and not keys[K_a]:
           self.naprx = 0
        if not keys[K_w] and not keys[K_s]:
           self.napry = 0
        if keys[K_SPACE] and k >= 40:
            a = ball(self.rect.x, self.rect.y + 30, self.firenapr)
            bullets.append(a)
            k = 0
            
        self.text1 = "HP:" + str(self.life)
        self.text = self.f1.render(self.text1, True, (255, 0, 0))
    def dtp(self):
        for i in ll_sprites:
            if sprite.collide_rect(i,d):
                if self.naprx == 2:
                    self.rect.x = self.rect.x - self.speed
                    
                if self.naprx == -2:
                    self.rect.x = self.rect.x + self.speed
                    
                if self.napry == 1:
                    self.rect.y = self.rect.y + self.speed
                    
                if self.napry == -1:
                     self.rect.y = self.rect.y - self.speed
                
                self.life = self.life - 10
                  
        
                if self.life < 1:
                    self.rect.x = 300
                    self.rect.y = 330
                    self.life = 3000
                    '''Boss.life = 500
                    Boss.rect.x = 600
                    Boss.rect.y = 100'''
d = Player(img, 0, 0, 3000)
bullets1 = []
t = 0
pyte = step(2600, 1052, 0)
class boss:
    def __init__(self, img):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = 1000
        self.rect.y = 800
        self.life = 500
        self.isgoing = False 
        self.speedx = 0
        self.speedy = 0
    def check_life(self):
        self.life -= 250
        if self.life <= 0:
            Boss.remove(self)
    def draw(self):
        window.blit(self.img, camera.apply(self) )
    def update(self):
        global t, pyte

        
        sum1 = self.rect.x//25 + self.rect.y//25*80
        s1k = pyte[1]
        if not self.isgoing:
            if len(pyte) > 2:
                pyte.pop(0)
            
                if sum1 < s1k:
                    if sum1 < s1k - 50:
                        self.speedy += 25
                    else:
                        self.speedx += 25
                else:
                    if sum1 > s1k + 50:
                        self.speedy -= 25
                    else:
                        self.speedx -= 25
                self.isgoing = True
        t += 1
        if t >= 50:
            r = ball(self.rect.x, self.rect.y + 30, 3)
            bullets1.append(r) 
            t = 0
        
        '''if d.rect.x < self.rect.x:
            speedx = -2
        if d.rect.x > self.rect.x:
            speedx = 2
        self.rect.x += speedx'''
        for i in ll_sprites:
            if sprite.collide_rect(i, self):
                self.rect.x -= speedx        
        '''if d.rect.y < self.rect.y:
            speedy = -2
        if d.rect.y > self.rect.y:
            speedy = 2
        self.rect.y += speedy'''
        for i in ll_sprites:
            if sprite.collide_rect(i, self):
                self.rect.y -= speedy

Boss_rect = [[600, 330]]                
Boss = [boss(IMG)]
class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)
    def apply(self, target):
        return  target.rect.move(self.state.topleft)
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
def camera_configure(camera, target_rect):
    l, t,_,_ = target_rect
    _, _,w, h = camera
    l, t = -l + win_width/2, -t + win_height/2
    l = min(0, l)
    l = max(-(camera.width-win_width), l)
    t = max(-(camera.height-win_height), t)
    t = min(0, t)
    return Rect(l, t, w, h)
total_level_width = 2000
total_level_height = 2000
camera = Camera(camera_configure, total_level_width, total_level_height)
f2 = font.SysFont(None,48)
text2 = "нажмите на q, что бы начать"
text = f2.render(text2, True, (255, 0, 0))
while game == False:
    timer.tick(120)
    keys =  key.get_pressed()
    if keys[K_q]:
        game = True
    for e in event.get():
        if e.type == QUIT:
            game = True
    window.fill((255, 255, 255))
    window.blit(text, (240, 250))
    display.update()
    
while game == True:
    timer.tick(120)
    for e in event.get():
        if e.type == QUIT:
            
            game = False
        
     

    window.fill((255, 255, 255))
    camera.update(d)
    for i in ll_sprites:
        if abs(i.rect.x - d.rect.x) <= win_width and abs(i.rect.y - d.rect.y) <= win_height:
            i.reset()
    for i in bullets:
        i.draw()
        i.update()
        for j in ll_sprites:
            if sprite.collide_rect(i, j):
                bullets.remove(i)
                break
        for boss1 in Boss:
            if sprite.collide_rect(i, boss1):
                boss1.check_life()
    for i in bullets1:
        
        i.draw()
        i.update()
        for j in ll_sprites:
            if sprite.collide_rect(i, j):

                bullets1.remove(i)
                break
        if sprite.collide_rect(d, i):
            d.life -= 200
            bullets1.remove(i)
        if d.life < 1:
            d.rect.x = 300
            d.rect.y = 330
            d.life = 3000
    k += 1
    d.dtp()
    
            
    d.update()
    
     
    d.reset()
    for boss1 in Boss:
        boss1.draw()
    Finish.draw()
    if sprite.collide_rect(d, Finish):
        game = 5
    for boss1 in Boss:
        boss1.update() 
    display.update()

while game == 5:
    window.blit(WIN, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            
            game = True        
    display.update() 

        
         
