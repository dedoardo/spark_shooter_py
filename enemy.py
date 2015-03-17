import math
import pygame
import random
import collision

class EnemyShips:
    def __init__(self):
        #ships
        self.active_ships = []
        self.destroyed_ships = 0
        self.speed = 150
        #weapon stuff
        self.bullets = []
        self.bullet_speed = 80

    def get_new_ship(self,x,y):
        self.active_ships.insert(0,[x,y,100])
        print "new ship spawned at ",x,y

    def remove_bullet(self,i):
        try :
            self.bullets.remove(i)
        except ValueError:
            pass
    def is_destroyed(self):
        for ship in self.active_ships:
            if ship[2] <= 0 :
                self.active_ships.remove(ship)
                self.destroyed_ships += 1
    
    def get_bullet_distance(self,time):
        r = random.randrange(1,15)
        distance = (time/1000.) * self.bullet_speed * r
        return distance
    
    def get_ship_distance(self,time):
        distance = (time/1000.) * self.speed 
        return distance   
    
    def fire(self):
        for ship in self.active_ships :
            self.bullets.insert(0,[ship[0],ship[1]])

    def respawn(self):
        self.bullets = []
        self.active_ships = []

    def reset(self):
        self.bullets = []
        self.active_ships = []
        self.destroyed_ships = 0
    
    def test_collision(self,player_bullets,player_rockets,bullet_img,rocket_img,alien_img,player_x,player_y,player_ship):
        b = []
        r = []
        c = 0
        b_w,b_h = bullet_img.get_size()
        r_w,r_h = rocket_img.get_size()
        a_w,a_h = alien_img.get_size()
        p_w,p_h = player_ship.get_size()
        # testing rocket collision
        for rocket in player_rockets :
            for ship in self.active_ships:
                if collision.is_collision(ship[0],ship[1],a_w,a_h,rocket[0],rocket[1],r_w,r_h) == True:
                    r.append(rocket)
                    self.active_ships.remove(ship)
                    self.destroyed_ships += 1

        # testing bullet collision
        for bullet in player_bullets :
            for ship in self.active_ships:
                if collision.is_collision(ship[0],ship[1],a_w,a_h,bullet[0],bullet[1],b_w,b_h) == True:
                    b.append(bullet)
                    ship[2] -= 30
        # testing secondary weapon collision
        for bullet in self.bullets :
            for rocket in player_rockets:
                if collision.is_collision(bullet[0],bullet[1],b_w,b_h,rocket[0],rocket[1],r_w,r_h):
                    try :
                        self.bullets.remove(bullet)
                    except ValueError:
                        pass
                    b.append(bullet)
                    
        # testing player ship collision

        for ship in self.active_ships :
            if collision.is_collision(ship[0],ship[1],a_w,a_h,player_x,player_y,p_w,p_h) == True:
                self.active_ships.remove(ship)
                c += 1

        return b,r,c
        
    def blit(self,screen,alien_img,bullet_img,time,player_x):
        # blitting bullets
        for bullet in self.bullets :
            if bullet[1] > 710 :
                self.bullets.remove(bullet)
            else :
               b_distance = self.get_bullet_distance(time)
               bullet[1] += b_distance
               screen.blit(bullet_img,(bullet[0],bullet[1]))

        # blitting ship
        for ship in self.active_ships :
            if ship[1] > 710 :
                self.active_ships.remove(ship)
            else :
                s_distance = self.get_ship_distance(time)
                ship[1] += s_distance
                if ship[0] > player_x :
                    ship[0] -= s_distance
                else :
                    ship[0] += s_distance
                screen.blit(alien_img,(ship[0],ship[1]))
        
