from pygame import *
from random import randint

#создание окна

main_window = display.set_mode((800,600))
main_window.fill((255, 255, 255))
clock = time.Clock()
display.set_caption('Ping-Pong')

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
    def speeeeed(self):
        self.rect.x += self.speed
        self.rect.y -= self.speed
            
    def active(self):
        if self.rect.x <= 50:
            self.rect.x = 400
            self.rect.y = 350
            self.speeeeed()
        if self.rect.x >= 550:
            self.rect.x = 400
            self.rect.y = 350 
            self.speeeeed()

        if self.rect.y >= 50:
            self.speed_y *= -1

        if self.rect.y <= 550:
            self.speed_y *= -1

#мячик

ball = Ball('bally.png', 400, 350, 51, 50, 5)    

ball.speeeeed()


game = True

while game:
    for e in event.get():
        if e.type == QUIT: game = False
    ball.speeeeed()
    ball.active()
    ball.reset()




    clock.tick(60)
    display.update()

