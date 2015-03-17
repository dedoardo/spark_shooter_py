import time as ti
import pygame
import ship
import interface
import random
import enemy
import bonus
pygame.init()

#variables initialized
global clock
clock = pygame.time.Clock()
t = 0
time = 0
p_x = 240
p_y = 320
t_begin = ti.time()


# screen initialized
screen = pygame.display.set_mode((1024,700),0,32)
font = pygame.font.SysFont("arial",20)
life_font = pygame.font.SysFont("Comic Sans MS", 40)
game_over_font = pygame.font.SysFont("Courier New",35)

# all images initialized
background_img = pygame.image.load('images/bg.jpg').convert()
b_w,b_h = background_img.get_size()
bullet_img = pygame.image.load('images/b_1.png').convert()
bullet_img.set_colorkey((0,0,0))
ship_img = pygame.image.load('images/ship.gif').convert()
rocket_img = pygame.image.load('images/0.png').convert()
rocket_img.set_colorkey((0,0,0))
alien_img = pygame.image.load('images/alien.png').convert()
alien_img.set_colorkey((255,255,255))
enemy_bullet_img = pygame.image.load('images/e_b.png').convert()
enemy_bullet_img.set_colorkey((0,0,0))

# classes initialized
my_ship = ship.Ship(ship_img)
enemy_ships = enemy.EnemyShips()
my_bonus = bonus.Bonus()


while True:
    t_now = ti.time() - t_begin
    t = clock.tick(60)
    s_c = "Speed : %r FPS" % str(int(clock.get_fps()))
    pygame.display.set_caption(s_c)
    screen.fill((0,0,0))
    screen.blit(background_img,(0,0))
    s_w,s_h = ship_img.get_size()
    # Handling all commands
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                my_ship.increase_scalar()
            if event.key == pygame.K_s:
                my_ship.decrease_scalar()
            if event.key == pygame.K_SPACE:
                my_ship.primary_fire(s_w)
            if event.key == pygame.K_TAB :
                my_ship.secondary_fire(s_h)
            if event.key == pygame.K_p:
                p = True
                while True :
                    e = pygame.event.wait()
                    if event.type == pygame.KEYDOWN:
                        p = not p
                
    # Handling movement keys
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_DOWN]:
        my_ship.update_position("K_DOWN",t)
    elif key_pressed[pygame.K_UP]:
        my_ship.update_position("K_UP",t)
    if key_pressed[pygame.K_LEFT]:
        my_ship.update_position("K_LEFT",t)
    elif key_pressed[pygame.K_RIGHT]:
        my_ship.update_position("K_RIGHT",t)

    time += clock.tick(60)
    t = clock.tick(60)
    second = t/1000.

    x,y = my_ship.get_position()
    
    ### ENEMY SHIP

    # Spawning 5 monster per time - getting random numbers
    if len(enemy_ships.active_ships) < 15 :
        r_x = random.randrange(0,1024)
        r_y = random.randrange(-350,-25)
        enemy_ships.get_new_ship(r_x,r_y)

    # Firing each 1.5 seconds
    if time >= 800 :
        time = 0
        enemy_ships.fire()
   
    # Blitting
    enemy_ships.blit(screen,alien_img,enemy_bullet_img,t,x)
    # Testing collision
    # Player Ship
    b = my_ship.test_collision(enemy_ships.bullets,bullet_img,ship_img)
    if len(b) > 0 :
        for i in b :
            enemy_ships.remove_bullet(i)


    # Alien Ships
    b,r,c = enemy_ships.test_collision(my_ship.bullets,my_ship.rockets,bullet_img,rocket_img,alien_img,x,y,ship_img)
    if len(b) > 0 :
        for i in b :
            my_ship.remove_bullet(i)

    if len(r) > 0 :
        for i in r :
            my_ship.remove_rocket(i)
    my_ship.armor -= c * 25

    # Game Over or New Life
    
    if my_ship.is_destroyed():
        if my_ship.is_game_over():
            interface.game_over(screen,game_over_font,enemy_ships.destroyed_ships)
            my_ship.reset()
            enemy_ships.reset()
            my_bonus.active_bonus = []
        else:
            my_ship.respawn()
            interface.new_life(screen,life_font,my_ship.life,enemy_ships.destroyed_ships)
            enemy_ships.respawn()
            my_bonus.active_bonus = []
        continue

    # Bonus
    if t_now >= 15 :
        my_bonus.new_bonus()
        t_begin = ti.time()

    #testing bonus collision
    b = my_ship.bonus_collision(my_bonus.active_bonus,my_bonus.bonus1_img,ship_img)
    for i in b :
        my_bonus.active_bonus.remove(i)
    my_bonus.blit_bonus(screen)
        
    
    
    enemy_ships.is_destroyed()
    my_ship.blit(screen,ship_img,bullet_img,rocket_img)
    interface.draw_interface(screen,font,my_ship.primary_ammo,my_ship.secondary_ammo,my_ship.life,my_ship.armor,x,y,enemy_ships.destroyed_ships)
    pygame.display.update()
