from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img_name, width, height, x, y):
        self.image = transform.scale(image.load(img_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

  

    def move1(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            
            self.rect.y -= 5
        if keys[K_DOWN]:
            self.rect.y += 5

    def move2(self):
        keys = key.get_pressed()
        if keys[K_w]:
            
            self.rect.y -= 5
        if keys[K_s]:
            self.rect.y += 5            

    

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10: 
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10


    def fire(self):
        pass

class Enemy(GameSprite):
    def move(self):
        pass

class Wall():
    def __init__(self, width,height, x,y, color=(255,255,255), transperancy=255):
        self.wall = Surface((width,height))
        self.wall.set_alpha(transperancy)
        self.wall.fill(color)
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.wall, (self.rect.x, self.rect.y))
