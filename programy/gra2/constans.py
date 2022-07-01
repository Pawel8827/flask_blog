
import pygame, os
pygame.font.init()
pygame.mixer.init()

WIDTH = 1200
HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
Statki_szerokosc = 100
Statki_wysokosc = 80
VEL = 5
BULLET_VEL = 7
BORDER = pygame.Rect(WIDTH//2 - 5,0,10, HEIGHT)
FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
MAX_KULE = 3
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
Pierwszy_uderzenie = pygame.USEREVENT + 1
Drugi_uderzenie = pygame.USEREVENT + 2
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('img','Space.png')), (WIDTH, HEIGHT))
y_spaceship_image = pygame.image.load(os.path.join('img', 'pierwszy_statek.png'))
pierwszy_Spaceship = pygame.transform.scale(y_spaceship_image, (Statki_szerokosc, Statki_wysokosc))
r_spaceship_image = pygame.image.load(os.path.join('img', 'drugi_statek.png'))
drugi_Spaceship = pygame.transform.scale(r_spaceship_image, (Statki_szerokosc, Statki_wysokosc))
sound_hit = pygame.mixer.Sound(os.path.join('sounds/hit.wav'))
sound_shot = pygame.mixer.Sound(os.path.join('sounds/shot.wav'))