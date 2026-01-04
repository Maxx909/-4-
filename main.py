from pygame import *
from random import randint,choice

init()
window_size = (800, 600)
window = display.set_mode(window_size)
clock = time.Clock()

COLORS = [
    (100, 0, 0),
    (100, 100, 0),
    (100, 100, 100),
    (100, 0, 100),
    (0, 0, 100),
    (100, 50, 0),
    (100, 0, 200),
    (100, 200, 0),
    (100, 200, 0),
]

rect = Rect(200, 200, 100, 100)


def create_enemy():
    enemy_list = []

    for i in range(20):
        enemy = Rect(randint(100, 700), randint(-400, -40), 40, 40)
        enemy_list.append(enemy)

    return enemy_list


enemy_list = create_enemy()

x = 200
y = 200

mouse_down = False

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                mouse_down = True
        if e.type == MOUSEBUTTONUP:
            if e.button == 1:
                mouse_down = False
        if e.type == MOUSEMOTION and mouse_down:
            x, y = e.pos

    window.fill((100, 0, 0))

    if rect.collidepoint(x, y):
        rect.center = (x, y)

    draw.rect(window, (0, 100, 0), rect)
    for i in range(len(enemy_list)):
        draw.rect(window, choice(COLORS), enemy_list[i])
        enemy_list[i].y += 5
        if enemy_list[i].y >= 600:
            enemy_list[i].y = -40
        if enemy_list[i].colliderect(rect):
            enemy_list[i].y = -40

    display.update()
    clock.tick(120)