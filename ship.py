import math
import pygame
import enemy
import collision

class Ship:
    def __init__(self,ship_img):
        #weapon stuff
        self.bullets = []
        self.rockets = []
        self.primary_ammo = 500
        self.secondary_ammo = 100
        self.bullet_speed = 20
        self.rocket_speed = 17
        #ship stuff
        self.speed = 100
        self.armor = 100
        self.life = 3
        self.scalar = 1
        self.x = 320
        self.y = 240
        self.w, self.h = ship_img.get_size()

    def increase_scalar(self):
        if self.scalar < 32 :
            self.scalar *= 2

    def decrease_scalar(self):
        if self.scalar > 1 :
            self.scalar /= 2

    def primary_fire(self,s_w):
        if self.primary_ammo > 0:
            self.bullets.insert(0,[self.x + s_w/2 - 10,self.y])
            self.primary_ammo -= 1

    def secondary_fire(self,s_w):
        if self.secondary_ammo > 0:
            self.rockets.insert(0,[self.x + 10,self.y - 10])
            self.rockets.insert(0,[self.x + self.w - 30, self.y - 10]) 
            self.secondary_ammo -= 1

    def remove_bullet(self,bullet):
        try :
            self.bullets.remove(bullet)
        except ValueError :
            pass
    def remove_rocket(self,rocket):
        try :
            self.rockets.remove(rocket)
        except ValueError :
            pass
    def update_position(self,key,time):
        #PYTHON U GOTTA IMPLEMENT SWITCH ... MUCH EASIER
        if key == "K_DOWN" :
            if self.y < 640 :
                self.y += (time/100.) * self.speed * self.scalar
        elif key == "K_UP" :
            if self.y > -10 :
                self.y -= (time/100.) * self.speed * self.scalar
        elif key == "K_LEFT" :
            if self.x > -10 :
                self.x -= (time/100.) * self.speed * self.scalar
        elif key == "K_RIGHT" :
            if self.x < 950 :
                self.x += (time/100.) * self.speed * self.scalar
         
    def test_collision(self,enemy_bullets,bullet_img,ship_img):
        b = []
        b_w,b_h = bullet_img.get_size()
        s_w,s_h = ship_img.get_size()
        for bullet in enemy_bullets :
            if collision.is_collision(self.x,self.y,s_w,s_h,bullet[0],bullet[1],b_w,b_h) == True:
                self.armor -= 10
                b.append(bullet)
        return b

    def bonus_collision(self,active_bonus,bonus_img,ship_img):
        b = []
        b_w,b_h = bonus_img.get_size()
        s_w,s_h = ship_img.get_size()
        for bonus in active_bonus:
            if collision.is_collision(self.x,self.y,s_w,s_h,bonus[0],bonus[1],b_w,b_h):
                b.append(bonus)
                self.get_bonus(bonus[2])
        return b
    
    def is_destroyed (self):
        if self.armor <= 0 :
            self.life -= 1
            return True
        return False

    def is_game_over(self):
        if self.life == 0 :
            return True
        return False

    def respawn(self):
        self.x = 320
        self.y = 240
        self.armor = 100

    def reset(self):
        self.x = 320
        self.y = 240
        self.armor = 100
        self.life = 3
        self.primary_ammo = 500
        self.secondary_ammo = 100

    def get_bonus(self,bonus):
        if bonus == 1 :
            self.secondary_ammo += 50
        elif bonus == 2 :
            self.armor += 50
        else :
            self.primary_ammo += 250
    
    def blit(self,screen,ship,bullet,rocket):
        screen.blit(ship,(self.x,self.y))
        w,h = ship.get_size()
        # blitting bullets
        for b in self.bullets :
            if b[1] < 0 :
                self.bullets.remove(b)
            else :
                b[1] -= self.bullet_speed
                screen.blit(bullet,(b[0],b[1]))
        # blitting rockets
        for r in self.rockets :
            if r[1] < 0 :
                self.rockets.remove(r)
            else :
                r[1] -= self.rocket_speed
                screen.blit(rocket,(r[0],r[1]))
                
        
    def get_position(self):
        return self.x,self.y

    
    

