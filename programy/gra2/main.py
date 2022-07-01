import pygame
from constans import *

pygame.display.set_caption("Pierwsza Gra")

def drow_window(pierwszy, drugi, Pierwszy_kule, Drugi_kule, Pierwszy_zycie, Drugi_zycie):
    WIN.blit(SPACE, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    Pierwszy_zycie_text = HEALTH_FONT.render("Życie: " + str(Pierwszy_zycie),1, WHITE)
    Drugi_zycie_text = HEALTH_FONT.render("Życie: " + str(Drugi_zycie),1, WHITE)
    WIN.blit(Drugi_zycie_text,(WIDTH - Drugi_zycie_text.get_width() -10 ,10))
    WIN.blit(Pierwszy_zycie_text,(10 ,10))
    WIN.blit(pierwszy_Spaceship, (pierwszy.x, pierwszy.y))
    WIN.blit(drugi_Spaceship, (drugi.x, drugi.y))
    for bullet in Pierwszy_kule:
        pygame.draw.rect(WIN,RED, bullet)
    for bullet in Drugi_kule:
        pygame.draw.rect(WIN,YELLOW, bullet)
    pygame.display.update()
      
def pierwszy_statek_ruch(keys_pressed, p_statek):
    if keys_pressed[pygame.K_a] and p_statek.x - VEL > 0: # lewo
        p_statek.x -= VEL 
    if keys_pressed[pygame.K_d] and p_statek.x + VEL + p_statek.width < BORDER.x: # prawo
        p_statek.x += VEL 
    if keys_pressed[pygame.K_w]and p_statek.y - VEL > 0: # góra
        p_statek.y -= VEL 
    if keys_pressed[pygame.K_s] and p_statek.y + VEL + p_statek.height < HEIGHT: # dół
        p_statek.y += VEL 

def drugi_statek_ruch(keys_pressed, d_statek):
    if keys_pressed[pygame.K_LEFT]and d_statek.x - VEL > BORDER.x + BORDER.width: # lewo
        d_statek.x -= VEL 
    if keys_pressed[pygame.K_RIGHT]and d_statek.x + VEL + d_statek.width < WIDTH: # prawo
        d_statek.x += VEL 
    if keys_pressed[pygame.K_UP] and d_statek.y - VEL > 0: # góra
        d_statek.y -= VEL 
    if keys_pressed[pygame.K_DOWN] and d_statek.y + VEL + d_statek.height < HEIGHT:# dół
        d_statek.y += VEL 


def wystrzal_kuli(Pierwszy_kule, Drugi_kule, pierwszy, drugi):
    for bullet in Pierwszy_kule:
        bullet.x += BULLET_VEL
        
        if drugi.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Drugi_uderzenie))
            sound_hit.play()
            Pierwszy_kule.remove(bullet)
        elif bullet.x > WIDTH:
            Pierwszy_kule.remove(bullet)   
    for bullet in Drugi_kule:
        bullet.x -= BULLET_VEL
        if pierwszy.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Pierwszy_uderzenie))
            sound_hit.play()
            Drugi_kule.remove(bullet)
        elif bullet.x < 0:
            Drugi_kule.remove(bullet)
def draw_winner(text):
    drow_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(drow_text, (WIDTH/2 - drow_text.get_width()/2, HEIGHT/2 - drow_text.get_height()/2 ))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    pierwszy = pygame.Rect(100,300,  Statki_szerokosc, Statki_wysokosc)
    drugi = pygame.Rect(1000,300,  Statki_szerokosc, Statki_wysokosc)
    Pierwszy_kule = []
    Drugi_kule = []
    Pierwszy_zycie = 10
    Drugi_zycie = 10
    clock = pygame.time.Clock()
    run =True 
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(Pierwszy_kule) < MAX_KULE:
                        sound_shot.play()
                        bullet = pygame.Rect(pierwszy.x + pierwszy.width, pierwszy.y + pierwszy.height//2 - 2, 10, 5)
                        Pierwszy_kule.append(bullet)
                        
                if event.key == pygame.K_RCTRL and len(Drugi_kule) < MAX_KULE:
                        sound_shot.play()
                        bullet = pygame.Rect(drugi.x, drugi.y + drugi.height//2 - 2, 10, 5)
                        Drugi_kule.append(bullet)
            if event.type == Pierwszy_uderzenie:
                Pierwszy_zycie -= 1

            if event.type == Drugi_uderzenie:
                 Drugi_zycie -= 1
        winner_text = ""        
        if Pierwszy_zycie <= 0:
            winner_text = "Gracz drugi wygrywa"
        if Drugi_zycie <= 0:
            winner_text = "Gracz pierwszy wygrywa"
        if winner_text != "":
            draw_winner(winner_text)
            break
        keys_pressed = pygame.key.get_pressed()
        pierwszy_statek_ruch(keys_pressed,pierwszy)
        drugi_statek_ruch(keys_pressed,drugi)
        wystrzal_kuli(Pierwszy_kule,Drugi_kule, pierwszy, drugi)
        drow_window(pierwszy, drugi, Pierwszy_kule, Drugi_kule, Pierwszy_zycie, Drugi_zycie)
        
    close()

def close():
    pygame.quit()


if __name__ == "__main__":
    main()

