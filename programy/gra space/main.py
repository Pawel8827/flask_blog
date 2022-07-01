import pygame, os, sys, random

from const import *
from player import Player
from enemy import Enemy
from projectile import Projectile

class Game():
    def __init__(self):
        pygame.init()
        self.load_textures()
        self.load_sounds()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.drow_screen = pygame.Surface(DROW_SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.dt = 1
        self.font = pygame.font.Font("Mitochondria.ttf", 20)
        self.click = False
        self.game()

    def load_textures(self):
        self.textures = {}
        for img in os.listdir("img"):
            texture = pygame.image.load("img/" + img)
            self.textures[img.replace(".png", "")] = texture
            


    def load_sounds(self):
        self.sounds = {}
        for sound in os.listdir("sounds"):
            file = pygame.mixer.Sound("sounds/" + sound)
            self.sounds[sound.replace(".wav", "")] = file

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
            if event.type == self.ENEMYMOVE:
                for enemy in self.enemis:
                    enemy.move()
            if event.type == pygame.KEYUP:
                self.click = False

    def check_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: # klawisz prawy
            self.player.x += int(round(PLAYER_SPEED + self.dt))
        if keys[pygame.K_LEFT]: # klawisz lewy
            self.player.x -= int(round(PLAYER_SPEED + self.dt))
        if keys[pygame.K_SPACE] and not self.click: # klawisz strzał
            self.sounds["shot"].play()
            self.click = True
            projectile = Projectile(self.player.centerx, self.player.centery, "1")
            self.projectiles.append(projectile)

    def close(self):
        pygame.quit()
        sys.exit(0)


    def game(self):
        self.ENEMYMOVE = pygame.USEREVENT
        pygame.time.set_timer(self.ENEMYMOVE, MOVE_RATIO)
        self.enemis = []
        for y in range(3):
            for x in range(int((DROW_SCREEN_SIZE[0] - (BORDER * 2))  /40)):
                enemy = Enemy(x * 40, y * 20, y +1)
                self.enemis.append(enemy)


        self.player = Player()
        self.projectiles =[]
        while True:
            self.check_keys()
            self.check_events()
            for projectile in self.projectiles:
                projectile.move()
                if projectile.y < 0 or projectile.y >DROW_SCREEN_SIZE[1]:
                    self.projectiles.remove(projectile)

            for projectile in self.projectiles:
                if projectile.type == "2" and projectile.colliderect(self.player):
                    self.projectiles.remove(projectile)
                    self.player.hp -= 1
                    self.sounds["hit"].play()
                elif projectile.type == "1":
                    for enemy in self.enemis:
                        if projectile.colliderect(enemy):
                            self.enemis.remove(enemy)
                            self.projectiles.remove(projectile)
                            self.sounds["hit"].play()
                            break
            for enemy in self.enemis:
                if enemy.y >= 150:
                    self.end()
                if random.randint(1, ENEMY_SHOT_RATIO) == 1:
                    projectile = Projectile(enemy.centerx, enemy.centery, "2")
                    self.sounds["shot"].play()
                    self.projectiles.append(projectile)
            if self.player.hp <= 0:
                self.end("Game Over")
            if len(self.enemis) <=0:
                self.end("You win")
            self.drow()
            self.refresh_screen()
    def end(self, text):
        surf = self.font.render(text,False, (255,255,255))
        rect = surf.get_rect(center=(int(DROW_SCREEN_SIZE[0]/2), int(DROW_SCREEN_SIZE[0]/2)))
        self.drow_screen.blit(surf, rect)
        self.refresh_screen()
        timer = END_TIME
        while timer > 0:
            timer  -= self.dt
        self.close()

    def drow(self):
        self.drow_screen.blit(self.textures["background"], (0,0))
        self.drow_screen.blit(self.textures["player"], self.player)
        for enemy in self.enemis:
            self.drow_screen.blit(self.textures["enemy" + enemy.type],enemy)


        for projectile in self.projectiles:
            self.drow_screen.blit(self.textures["projectile" + projectile.type],projectile)
            


    def refresh_screen(self):
        scaled = pygame.transform.scale(self.drow_screen, SCREEN_SIZE)
        self.screen.blit(scaled,(0,0))
        pygame.display.update()
        self.dt = self.clock.tick(FREMRETE) + FREMRETE / 300 
Game()