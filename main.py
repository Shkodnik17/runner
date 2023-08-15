import pgzrun
import time



WIDTH = 600
HEIGHT = 350
alien = Actor('alien')
alien.pos = 100, 245
fon = Actor('fon')
box = Actor('box')
over_game = Actor('go')
box.pos = 601, 265
bee  = Actor('bee')
bee.pos = 950, 150
game_over  = 0
score =  0



def draw():
    fon.draw()
    alien.draw()
    box.draw()
    bee.draw()
    # screen.draw.text(count, center=(150, 100), color="white", fontsize = 56)
    screen.draw.text("Счет: {}".format(score), topleft=(10, 10), color="black")
    #screen.draw.text('Ваш счет ', center=(150, 100), color="white", fontsize=56)
    if game_over == 1:
        over_game.draw()
        screen.draw.text('Нажмите "Q" чтобы перезапустить', topleft=(120, 210), color="black", fontname ='font', fontsize = 20)






def update(dt):
    global game_over
    global score
    # движение коробки
    if box.x > -21:
        box.angle = box.angle + 5
        box.x = box.x - 3
    else:
        box.x = WIDTH
        score = score + 1
    # движение пчелки
    if bee.x > -21:
        bee.x = bee.x - 3
    else:
        bee.x = WIDTH
        score = score + 1
    #  управление
    if keyboard.a and alien.x > 20:
        
        alien.x = alien.x - 5
    if keyboard.d and alien.x < 580:

        alien.x = alien.x + 5
    if keyboard.LSHIFT and  keyboard.d:
        alien.image = 'duck'
        alien.x = alien.x + 3
    if alien.colliderect(box) or alien.colliderect(bee):
        game_over = 1

    if keyboard.k_1:
        alien.image = 'redalien'
    if keyboard.k_2:
        alien.image = 'bluealien'
    if keyboard.k_3:
        alien.image = 'alien'
    if game_over == 1 and keyboard.q:
        game_over = game_over - 1
        score = 0
        alien.pos = 100, 245
        box.pos = 601, 265
        bee.pos = 950, 150






def on_key_down(key):
    if keyboard.space and alien.y < 250:
        alien.y = 120
        animate(alien, tween='linear', duration=1.5, y=245)













pgzrun.go()


