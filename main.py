from pygame import *
from button import Button
from sprite import Player, GameSprite, Wall
from random import randint
from time import sleep

tiles = 2 
scroll = 0

window = display.set_mode((700,500))
bg = transform.scale(image.load("bg.png"), (700,500))
bg_width = bg.get_width()
bg_height = bg.get_height()
game = True
run = False
clock = time.Clock()

btn1 = Button('start_btn.png', 300,100, 100, 50)
btn2 = Button('exit_btn.png', 300,250, 100, 50)

player = Player('player.png', 50, 75, 100, 200)
player2 = Player('player2.png', 50, 75, 550, 200)
ball = GameSprite('ball.png',50, 50, 300, 200)
left = GameSprite('left.png',70, 120, 0, 190)
right = GameSprite('right.png',70, 120, 630, 190)
speed = 0

font.init()
font1 = font.SysFont("Arial", 40)

dx = 3
dy = -3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = not run
            
  
    if run:
        window.blit(bg, (0,0))
        player.draw(window)
        player2.draw(window)
        player2.move2()
        player.move1()
        ball.rect.x+= dx
        ball.rect.y+= dy
        if ball.rect.x <= 5 or ball.rect.x >= 680:
            dx *= -1
        if ball.rect.y <= 5 or ball.rect.y >= 480:
            dy *= -1
        ball.draw(window)
        left.draw(window)
        right.draw(window)
        if ball.rect.colliderect(player.rect) or ball.rect.colliderect(player2.rect):
            dx *= -1
        if ball.rect.colliderect(left.rect) or ball.rect.colliderect(right.rect):
            img = font1.render("GOAL!", True, (255,255,255))
            window.blit(img, (300,200))
            display.update()
            sleep(1)
            ball.rect.x = 340
            ball.rect.y = 340

    else:
        window.blit(bg, (0,0))
        if btn1.draw(window):
            run = True
        if btn2.draw(window):
            game = False
    
   
    display.update()
    clock.tick(60)