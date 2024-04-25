from pygame import *
from random import randint

#создание окна

main_window = display.set_mode((800,600))
main_window.fill((255, 255, 255))
clock = time.Clock()
display.set_caption('Ping-Pong')
font.init()
mixer.init()
mixer.music.load('water.ogg')
mixer.music.play()

#класс GameSprite


class GameSprite(sprite.Sprite):
    def __init__(self, p_image, x, y, s_x, s_y, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(p_image), (s_x, s_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        main_window.blit(self.image, (self.rect.x, self.rect.y))

#класс Мячик

class Ball(GameSprite):
    def __init__(self, p_image, x, y, s_x, s_y, speed):
        super().__init__(p_image, x, y, s_x, s_y, speed)
        self.speed_x = self.speed
        self.speed_y = self.speed
            
    def active(self): 
        global player2
        global player1
        global w1
        global w2
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y <= 0:
            self.speed_y *= -1

        if self.rect.y >= 550:
            self.speed_y *= -1
        if sprite.collide_rect(player1, self):
            self.speed_x *= -1
        if sprite.collide_rect(player2, self):
            self.speed_x*= -1

        if self.rect.x <= 0:
            w2 += 1
            self.rect.x = 300
            self.rect.y = 350
            
        if self.rect.x >= 800:
            w1 += 1
            self.rect.x = 300
            self.rect.y = 350 
        
            

       

#мячик

ball = Ball('bally.png', 300, 350, 51, 50, 5)    

#класс Игрок

class Players(GameSprite):
    def opana(self):
        key_pressed = key.get_pressed()
        # if e.type == KEYDOWN:
        if key_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 590:
                self.rect.y += self.speed

    def obana(self):
        key_pressed = key.get_pressed()
        #if e.type == KEYDOWN:
        if key_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 590:
            self.rect.y += self.speed

#игроки

player2 = Players('rocketka2.png', 20, 230, 20, 150, 6)
player1 = Players('rocketka1.png', 760, 230, 20, 150, 6)
game = True

font1 = font.SysFont('Arial', 30)
win1 = font1.render('Красный харош, чёрный не оч', True, (255,0,0))
win2 = font1.render('Чёрный красава, красный фу', True, (0,0,0))

pw1 = font1.render('Счёт:', True, (0,0,0))
pw2 = font1.render('Счёт:', True, (255,0,0))
w1 = 0
w2 = 0
p1 = font1.render(str(w1), True, (0,0,0))
p2 = font1.render(str(w2), True, (255,0,0))
finish = False
while game:
    if not finish:
        main_window.fill((255, 255, 255))

        main_window.blit(pw1, (10,10))

        main_window.blit(pw2, (650,10))

        p1 = font1.render(str(w1), True, (0,0,0))
        p2 = font1.render(str(w2), True, (255,0,0))

        main_window.blit(p1, (100,10))

        main_window.blit(p2, (750, 10))
        if w2 == 10:
            main_window.blit(win1, (200, 300))
            finish = True
        if w1 == 10:
            main_window.blit(win2, (200, 300))
            finish = True
        
        ball.active()
        ball.reset()
        player1.obana()
        player1.reset()
        player2.opana()
        player2.reset()

    for e in event.get():
        if e.type == QUIT: game = False
    

    clock.tick(60)
    display.update()


