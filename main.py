import pygame
import random

from car import Car
from dust import Dust
from wasd import Wasd
from dune import Dune
from rock import Rock

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 65)
pygame.display.set_caption("Finishline")

# set up variables for the display
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

going_forward = False
going_left = False
going_right = False
begin = False

message = "Finishline"
message2 = "Press 'W' to begin"
display_message = my_font.render(message, True, (255, 255, 255))
my_font = pygame.font.SysFont('Comic Sans', 25)
display_message2 = my_font.render(message2, True, (255, 255, 255))

# Instantiate the images
car = Car(700, 600)
d = Dust(700, 600)
wasd = Wasd(800, 400)
game_map = Dune(0, 0)

rock = Rock(random.randint(0, 1440), -200)
rock2 = Rock(random.randint(0, 1440), -150)
rock2.change_size(1.25)


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        begin = True
        going_forward = True
    else:
        going_forward = False

    if keys[pygame.K_a]:
        going_left = True
    else:
        going_left = False

    if keys[pygame.K_d]:
        going_right = True
    else:
        going_right = False

    # --- Main event loop
    # ----- NO BLIT ZONE START ----- #
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    #  ----- NO BLIT ZONE END  ----- #
    screen.fill((0, 0, 0))
    screen.blit(game_map.image, (game_map.x, game_map.y))
    screen.blit(rock.image, (rock.x, rock.y))
    screen.blit(rock2.image, (rock2.x, rock2.y))
    if begin is True:
        if going_forward:
            screen.blit(d.image, (car.x + 120 + random.randint(0, 20), car.y + 265 + random.randint(0, 20)))
            screen.blit(d.image, (car.x + random.randint(0, 20), car.y + 265 + random.randint(0, 20)))
            screen.blit(d.image, (car.x, car.y + 265 + random.randint(0, 20)))
            rock.move(rock.x, rock.y + 3)
            rock2.move(rock2.x, rock2.y + 3)
            if rock.y > 1000:
                rock.y = -200
                rock.move(random.randint(0, 1440), rock.y)
            if rock2.y > 1000:
                rock2.y = -200
                rock2.move(random.randint(0, 1440), rock2.y)
        if going_left and going_forward and car.x > 0:
            car.move(car.x - 3, car.y)
        if going_right and going_forward and car.x < 1445:
            car.move(car.x + 3, car.y)

    else:
        screen.blit(display_message, (635, 160))
        screen.blit(display_message2, (1200, 425))
        screen.blit(wasd.image, (1000, 350))

    screen.blit(car.image, (car.x, car.y))

    pygame.display.update()
    # END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
