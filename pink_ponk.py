from pygame import *

window = display.set_mode((700, 500))#создай окно игры
display.set_caption('Пинг понг')
background = transform.scale(image.load('background.png'), (700, 500))

clock = time.Clock()
FPS = 60

game = True

while game:
    window.blit(background, (0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False#задай фон сцены

    display.update()
    clock.tick(FPS)
