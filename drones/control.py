from pysimverse import Drone
import pygame
import time

# initialize pygame
pygame.init()

# create small control window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Drone Controller")

# connect drone
drone = Drone()
drone.connect()

# take off
drone.take_off()

speed = 20

running = True

while running:

    pygame.event.pump()

    keys = pygame.key.get_pressed()

    # movement
    if keys[pygame.K_w]:
        drone.move_forward(speed)

    if keys[pygame.K_s]:
        drone.move_backward(speed)

    if keys[pygame.K_a]:
        drone.move_left(speed)

    if keys[pygame.K_d]:
        drone.move_right(speed)

    # altitude
    if keys[pygame.K_UP]:
        drone.move_up(speed)

    if keys[pygame.K_DOWN]:
        drone.move_down(speed)

    # rotation
    if keys[pygame.K_LEFT]:
        drone.rotate_left(20)

    if keys[pygame.K_RIGHT]:
        drone.rotate_right(20)

    # quit
    if keys[pygame.K_q]:
        drone.land()
        running = False

    time.sleep(0.05)

pygame.quit()