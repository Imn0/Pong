import pygame
from sys import exit

def display_score(points_player_score, points_ai_score):
    points_player = game_font.render(f'{points_player_score}', False, 'white')
    points_ai = game_font.render(f'{points_ai_score}', False, 'white')
    screen.blit(points_player, (200,10))
    screen.blit(points_ai, (950,10))
    
pygame.init()
pygame.display.set_caption('pong')
game_font = pygame.font.Font('font/Pixeltype.ttf', 150)
screen = pygame.display.set_mode((1200,700))  #  w,h
clock = pygame.time.Clock()

background_surface = pygame.Surface((1200,700))

ball_surface = pygame.Surface((20,20))
ball_surface.fill('white')
ball_x_pos = 600.0
ball_y_pos = 350.0
ball_rect = ball_surface.get_rect(center = (ball_x_pos,ball_y_pos))


ai_off_surface = game_font.render('ai is off', False, 'red')

player_surface = pygame.Surface((20,150))
player_rect = player_surface.get_rect(center = (60,350))
player_surface.fill('white')

ai_status = True
ai_surface = pygame.Surface((20,150))
ai_rect = player_surface.get_rect(center = (1200-60,350))
ai_surface.fill('white')

ball_x_speed = 7.0
ball_y_speed = 7.0
points_player_score = 0
points_ai_score = 0

while True:
    screen.blit(background_surface,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEDOWN:
                if ai_status:
                    ai_status = False
                else:
                    ai_status = True
        
   
    #ball movement 
    ball_rect.x += ball_x_speed
    ball_rect.y += ball_y_speed
    if ball_rect.bottom >= 700:
        ball_y_speed = -ball_y_speed
    if ball_rect.top <= 0: 
        ball_y_speed = -ball_y_speed
    if ball_rect.right >= 1200:
        ball_rect.x = 1200 - ball_rect.x + 200
        points_player_score += 1
    if ball_rect.left <= 0: 
        ball_rect.x = 1200 - ball_rect.x - 200
        points_ai_score += 1

    if not ai_status:
        screen.blit(ai_off_surface, (600,20))

    screen.blit(ball_surface, ball_rect)
    display_score(points_player_score,points_ai_score)
    screen.blit(player_surface,player_rect)
    screen.blit(ai_surface,ai_rect)

    #key player input
    keys = pygame.key.get_pressed()
    #ai 
    if ball_rect.y < ai_rect.y and ball_rect.x > 600 and ai_status:
        ai_rect.y -= 7
    if ball_rect.y > ai_rect.y and ball_rect.x > 600 and ai_status:
        ai_rect.y += 7
    if ai_rect.top <= 0:
        ai_rect.y = 0
    if ai_rect.bottom >= 700:
        ai_rect.y = 700 - 150




    if keys[pygame.K_SPACE] or keys[pygame.K_UP] :
        player_rect.y -= 10
    if keys[pygame.K_LCTRL] or keys[pygame.K_DOWN]:
        player_rect.y += 10

    #prevent player from going overboard
    if player_rect.top <= 0:
        player_rect.y = 0
    if player_rect.bottom >= 700:
        player_rect.y = 700 - 150

    #ball colison
    if player_rect.colliderect(ball_rect):
        ball_rect.x += 3
        ball_x_speed = -ball_x_speed
    if ai_rect.colliderect(ball_rect):
        ball_rect.x -= 3
        ball_x_speed = -ball_x_speed



    pygame.display.update()
    clock.tick(60)