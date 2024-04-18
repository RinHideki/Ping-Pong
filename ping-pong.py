from pygame import *
from random import randint

#создание окна

main_window = display.set_mode((800,600))
main_window.fill((255, 255, 255))
clock = time.Clock()
display.set_caption('Ping-Pong')

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
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y <= 0:
            self.speed_y *= -1

        if self.rect.y >= 550:
            self.speed_y *= -1

        if self.rect.x <= 50:
            self.rect.x = 300
            self.rect.y = 350
            
        if self.rect.x >= 750:
            self.rect.x = 300
            self.rect.y = 350 

        if sprite.collide_rect(player2, ball):
            self.rect.x *= -1
            

       

#мячик

ball = Ball('bally.png', 300, 350, 51, 50, 5)    

#класс Игрок

class Players(GameSprite):
    def opana(self):
        keys_pressed = key.get_pressed()
        # if e.type == KEYDOWN:
        if key_pressed[K_w] and self.rect.y < 10:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y > 590:
                self.rect.y += self.speed

    def obana(self):
        keys_pressed = key.get_pressed()
        #if e.type == KEYDOWN:
        if key_pressed[K_UP] and self.rect.y < 10:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y > 590:
            self.rect.y += self.speed

#игроки

player1 = Players('rocketka2.png', 20, 230, 20, 150, 3)
player2 = Players('rocketka1.png', 770, 230, 20, 150, 3)
game = True

while game:
    main_window.fill((255, 255, 255))
    for e in event.get():
        if e.type == QUIT: game = False
    ball.active()
    ball.reset()
    player1.opana()
    player1.reset()
    player2.obana()
    player2.reset()



    clock.tick(60)
    display.update()

