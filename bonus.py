import pygame
import random
import interface
class Bonus:
    def __init__(self):
        self.bonus1_img = pygame.image.load("images/bonus_1.png").convert()
        self.bonus1_img.set_colorkey((0,0,0))
        self.bonus2_img = pygame.image.load("images/bonus_2.png").convert()
        self.bonus2_img.set_colorkey((0,0,0))
        self.bonus3_img = pygame.image.load("images/bonus_3.png").convert()
        self.bonus3_img.set_colorkey((0,0,0))
        self.active_bonus = []

    def new_bonus(self):
        r = random.randrange(1,4)
        r_x = random.randrange(0,1024)
        r_y = random.randrange(200,700)
        self.active_bonus.insert(0,[r_x,r_y,r])

    def blit_bonus(self,screen):
        for bonus in self.active_bonus:
            if bonus[2] == 1 :
                screen.blit(self.bonus1_img,(bonus[0],bonus[1]))
            elif bonus[2] == 2 :
                screen.blit(self.bonus2_img,(bonus[0],bonus[1]))
            else :
                screen.blit(self.bonus3_img,(bonus[0],bonus[1]))
        



        
        
