import os
import pygame
import time
import random

# FPS is used for the frames per second, walkspeed for the walk speed
FPS = 60
walkspeed = 5
city = 1

# these are all colors with their respective names and codes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# width and height of window, WIN is window, and Run 2 is the name of the window
width, height = 1350, 750
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Run 2: Jormungandr")

knight_idle_right = pygame.image.load(os.path.join('Sprites', 'knight_idle_right.png'))
knight_run_idle_right = pygame.image.load(os.path.join('Sprites', 'knight_run_idle_right.png'))
knight_run_left_leg_right = pygame.image.load(os.path.join('Sprites', 'knight_run_left_leg_right.png'))
knight_run_right_leg_right = pygame.image.load(os.path.join('Sprites', 'knight_run_right_leg_right.png'))
knight_idle_left = pygame.image.load(os.path.join('Sprites', 'knight_idle_left.png'))
knight_run_idle_left = pygame.image.load(os.path.join('Sprites', 'knight_run_idle_left.png'))
knight_run_left_leg_left = pygame.image.load(os.path.join('Sprites', 'knight_run_left_leg_left.png'))
knight_run_right_leg_left = pygame.image.load(os.path.join('Sprites', 'knight_run_right_leg_left.png'))
nakof_wild = pygame.transform.scale(pygame.image.load(os.path.join('Backdrops', 'nakof_wild_backdrop.png')), (width, height))

knight_run_right = [knight_run_idle_right, knight_run_left_leg_right, knight_run_idle_right, knight_run_right_leg_right]
knight_run_left = [knight_run_idle_left, knight_run_left_leg_left, knight_run_idle_left, knight_run_right_leg_left]
draw_number = 0
frames_before_knight_drawn = 0

def draw_window(knight):
    global draw_number
    global frames_before_knight_drawn
    global city
    keys_pressed = pygame.key.get_pressed()

    if city == 1:
        WIN.blit(nakof_wild, (0, 0))
    elif city == 1.1:
        WIN.fill(WHITE)
    elif city == 1.2:
        WIN.fill(BLACK)

    if keys_pressed[pygame.K_RIGHT]:
        WIN.blit(knight_run_right[draw_number], (knight.x, knight.y)) #this whole part is for what the sprite looks like while you run
        frames_before_knight_drawn += 1
        if frames_before_knight_drawn >= 10:
            frames_before_knight_drawn = 0
            draw_number += 1
        if draw_number >= len(knight_run_right):
            draw_number = 0
        #this part is to change what the backdrop/city/location should be
        if knight.x + walkspeed + 64 > width and city == 1:
            city = 1.1
            knight.x = 50
        elif knight.x + walkspeed + 64 > width and city == 1.1:
            city = 1.2
            knight.x = 50

    elif keys_pressed[pygame.K_LEFT]:
        WIN.blit(knight_run_left[draw_number], (knight.x, knight.y))
        frames_before_knight_drawn += 1
        if frames_before_knight_drawn >= 10:
            frames_before_knight_drawn = 0
            draw_number += 1
        if draw_number >= len(knight_run_left):
            draw_number = 0
        #this part is to change what the backdrop/city/location should be
        if knight.x - walkspeed < 32 and city == 1.1:
            city = 1
            knight.x = 1300
        elif knight.x - walkspeed < 32 and city == 1.2:
            city = 1.1
            knight.x = 1300
    else:
        WIN.blit(knight_idle_right, (knight.x, knight.y))

    pygame.display.update()

def main():
    global knight_idle_right
    knight = pygame.Rect(50, 656, 20, 62)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT] and knight.x + walkspeed + 64 < width:
            knight_idle_right = pygame.image.load(os.path.join('Sprites', 'knight_idle_right.png'))
            knight.x += walkspeed
        if keys_pressed[pygame.K_LEFT] and knight.x - walkspeed > 32:
            knight_idle_right = pygame.image.load(os.path.join('Sprites', 'knight_idle_left.png'))
            knight.x -= walkspeed

        draw_window(knight)

    pygame.quit()


if __name__ == "__main__":
    main()
