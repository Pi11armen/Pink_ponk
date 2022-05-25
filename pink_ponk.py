from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_widht, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_widht, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):        
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):        
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

win_width = 700
win_height = 500

window = display.set_mode((700, 500))#создай окно игры
display.set_caption('Пинг понг')
background = transform.scale(image.load('papapapa.jpg'), (700, 500))

clock = time.Clock()
FPS = 60

game = True
finish = False

speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render("PLAYER 1 LOSE", True, (180, 0, 0))
font2 = font.Font(None, 35)
lose2 = font1.render("PLAYER 2 LOSE", True, (180, 0, 0))

ball = GameSprite("ball.png", 325, 200, 0, 15, 15)
racket1 = Player ("wall.png", 30, 200, 4, 50, 150)
racket2 = Player ("wall.png", 600, 200, 4, 50, 150)

while game:
    window.blit(background, (0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False#задай фон сцены

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.x > 701:
        finish = True
        window.blit(lose2, (200, 200))



    display.update()
    clock.tick(FPS)

