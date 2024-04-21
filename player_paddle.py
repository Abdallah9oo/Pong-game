import pygame,sys,random
player = pygame.Rect(0,0,20,100)
player.midright = (screen_width, screen_height/2)
pygame.draw.rect(screen,'white',player)
player_speed = 0

def animate_player():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0

    if player.bottom >= screen_height:
        player.bottom = screen_height
while True:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -6
            if event.key == pygame.K_DOWN:
                player_speed = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed = 0
            if event.key == pygame.K_DOWN:
                player_speed = 0
animate_player()
