import pygame
import time

def draw_interface(screen,font,primary_ammo,secondary_ammo,life,armor,x,y,destroyed_ships):
    # coordinates :
    c_t = "Coordinates X : %r , Y : %r" % (int(x),int(y))
    c_text = font.render(c_t,True,(0,255,0))
    # ammo
    a_t = "Primary weapon : %r  Secondary weapon : %r" % (primary_ammo,secondary_ammo)
    a_text = font.render(a_t,True,(0,255,0))
    # ship stats
    s_t = "Life remainings : %r Armor : %r" % (life,armor)
    s_text = font.render(s_t,True,(0,255,0))
    # destroye ships
    d_t = "Destroyed ships : %r " % destroyed_ships
    d_text = font.render(d_t,True,(0,255,0))
    # blitting everython
    screen.blit(c_text,(0,0))
    screen.blit(a_text,(0,700 - a_text.get_height()))
    screen.blit(s_text,(1024 - s_text.get_width(),0))
    screen.blit(d_text,(1024 - d_text.get_width(),700 - d_text.get_height()))
    
def new_life(screen,font,life,ships_destroyed):
    i = 0
    while i < 5 :    
        t1 = "You got killed!"
        t2 = "%r life remaining"%(life)
        t3 = "You have destroyed %r ships by far" %(ships_destroyed)
        t4 = "New life will start in %r seconds..." %(5-i)

        text1 = font.render(t1,True,(0,0,255))
        text2 = font.render(t2,True,(0,0,255))
        text3 = font.render(t3,True,(0,0,255))
        text4 = font.render(t4,True,(0,0,255))

        screen.fill((0,0,0))
        screen.blit(text1,( 512 - text1.get_width() / 2, 100))
        screen.blit(text2,( 512 - text2.get_width() / 2, 100 + text1.get_height()))
        screen.blit(text3,( 512 - text3.get_width() / 2, 100 + text2.get_height() * 2))
        screen.blit(text4,( 512 - text4.get_width() / 2, 100 + text3.get_height() * 3))
        pygame.display.update()
        i += 1

        time.sleep(1)

def get_message(n):
    if n < 100 :
        message = " You definitely suck!"
    elif n < 150 :
        message = " You are quite good"
    elif n < 200 :
        message = " Good result!"
    else :
        message = " You are a fucking programer! Gratz"
    return message

def game_over(screen,font,ships_destroyed):
    message = get_message(ships_destroyed)
    t1 = "Game Over"
    t2 = "You have destroyed %r ships" %(ships_destroyed)
    t3 = message
    print message
    t4 = "Press Enter to play a new game"
    text1 = font.render(t1,True,(255,0,0))
    text2 = font.render(t2,True,(0,0,255))
    text3 = font.render(t3,True,(0,0,255))
    text4 = font.render(t4,True,(0,0,255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RETURN]:
            break
                
        screen.fill((0,0,0))
        screen.blit(text1,(512 - text1.get_width() / 2, 100))
        screen.blit(text2,(512 - text2.get_width() / 2, 100 + text1.get_height() + 50))
        screen.blit(text3,(512 - text3.get_width() / 2, 100 + text2.get_height() *2 + 50))
        screen.blit(text4,(512 - text4.get_width() / 2, 100 + text3.get_height() * 3 + 50))
        pygame.display.update()
    
        

def pause():
    t = True
    while t:
        e = pygame.event.wait()
        if e.key == pygame.K_p:
            break
                
    
