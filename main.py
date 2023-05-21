from pygame import *
from button import Button
from sprite import Player, GameSprite, Wall
from random import randint


tiles = 2 
scroll = 0

window = display.set_mode((700,500))
bg = transform.scale(image.load("bg.png"), (700,500))
bg_width = bg.get_width()
bg_height = bg.get_height()
game = True
run = False
clock = time.Clock()

btn1 = Button('start_btn.png', 100,100, 100, 50)
btn2 = Button('exit_btn.png', 300,100, 100, 50)

player = Player('player.png', 50, 75, 100, 200)
player2 = Player('player2.png', 50, 75, 400, 200)
ball = GameSprite('ball.png',50, 50, 300, 200)

speed = 0


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
        ball.draw(window)
        
       
    else:
        window.fill((0,0,0))
        if btn1.draw(window):
            run = True
        if btn2.draw(window):
            game = False
    
   
    display.update()
    clock.tick(60)