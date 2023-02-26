from pygame import *
from random import randint



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, lenght_x, lenght_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (lenght_x, lenght_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 345:
            self.rect.y += self.speed
    
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('pixil-frame-0.png'), (700, 500))


racket_1 = Player('racket.png', 30, randint(100, 300), 5, 50, 150)
racket_2 = Player('racket.png', 620, randint(100, 300), 5, 50, 150)
ball = GameSprite('tenis_ball.png', 350, 250, randint(3, 5), 50, 50)

game = True
finish = False
FPS = 60
clock = time.Clock()

font.init()
text = font.SysFont('Time New Roman', 50)

text_win = text.render('FIRST PLAYER WIN', True, (0, 0, 255))
text_lose = text.render('SECOND PLAYER WIN', True, (0, 0, 255))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        racket_1.update()
        racket_1.reset()
        racket_2.update2()
        racket_2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket_2, ball) or sprite.collide_rect(ball, racket_1):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(text_lose, (200, 200))
        if ball.rect.x > 700:
            finish = True
            window.blit(text_win, (200, 200))
    display.update()
    clock.tick(FPS)