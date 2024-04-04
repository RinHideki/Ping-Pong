from pygame import *


#создание окна

main_window = display.set_mode((800,800))
main_window.fill((255, 255, 255))
clock = time.Clock()
display.set_caption('Ping-Pong')




game = True

while game:



    for e in event.get():
        if e.type == QUIT: game = False
    clock.tick(60)
    display.update()
