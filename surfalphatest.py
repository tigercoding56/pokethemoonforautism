import pygame
import math
import numpy as np
import copy
def highlight_outline(surface, angle, angle_range=45):
    temp_surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
    angle_range = angle_range 
    center_x = surface.get_width() // 2
    center_y = surface.get_height() // 2

    for x in range(1, surface.get_width() - 1):
        for y in range(1, surface.get_height() - 1):
            dx = x - center_x
            dy = y - center_y
            pixel_angle = math.degrees(math.atan2(dy, dx))
            #print(pixel_angle)
            angle_diff = abs(angle -( pixel_angle%360))
            angle_diff = min(angle_diff, 360 - angle_diff)
            angle_diff = max(0,angle_diff)

            if angle_diff <= angle_range:
                neighbors = [
                    surface.get_at((x - 1, y)),
                    surface.get_at((x + 1, y)),
                    surface.get_at((x, y - 1)),
                    surface.get_at((x, y + 1))
                ]

                #if any(n != surface.get_at((x, y)) for n in neighbors):
                temp_surface.set_at((x, y), (min(angle_diff,255), 0, 0))
                temp_surface.set_at((x, y), (255, 0, 0))# Highlight the pixel with red color
            else:
                temp_surface.set_at((x, y), (0, 255, 0))
                

    return temp_surface
def highlight_outline(surface, angle, angle_range=45):
    temp_surface = 0
    temp_surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
    
    angle_range = angle_range 
    center_x = surface.get_width() // 2
    center_y = surface.get_height() // 2

    width = surface.get_width()
    height = surface.get_height()
    
    temp_surface.fill((0,0,0,1))
    
    
    # Top and bottom edges
    for x in range(width):
        for y in [0, height - 1]:
            dx = x - center_x
            dy = y - center_y
            pixel_angle = math.degrees(math.atan2(dy, dx))
            angle_diff = abs(angle - (pixel_angle % 360))
            angle_diff = min(angle_diff, 360 - angle_diff)
            angle_diff = max(0, angle_diff)

            if angle_diff <= angle_range:
                pygame.draw.circle(temp_surface, (255,255,255,int((angle_range-min(abs(angle_diff), 255))*0.06)), (x, y), int((angle_range-min(abs(angle_diff), 255))*0.04))  # Highlight the pixel with red color
            #else:
                #temp_surface.set_at((x, y), (0, 255, 0))  # Highlight the pixel with green color

    # Left and right edges (excluding corners)
    for y in range(1, height - 1):
        for x in [0, width - 1]:
            dx = x - center_x
            dy = y - center_y
            pixel_angle = math.degrees(math.atan2(dy, dx))
            angle_diff = abs(angle - (pixel_angle % 360))
            angle_diff = min(angle_diff, 360 - angle_diff)
            angle_diff = max(0, angle_diff)

            if angle_diff <= angle_range:
                #temp_surface.set_at((x, y), (min(angle_diff, 255), 0, 0))  # Highlight the pixel with red color
                pygame.draw.circle(temp_surface, (255,255,255,int((angle_range-min(abs(angle_diff), angle_range))*0.06)), (x, y), int((angle_range-min(abs(angle_diff), angle_range))*0.04))  # Highlight the pixel with red color

            #else:
                #temp_surface.set_at((x, y), (0, 255, 0))  # Highlight the pixel with green color

    return temp_surface


# Initialize Pygame
pygame.init()

# Create a Pygame surface object
surface = pygame.image.load('img/wendy.png')
#surface.fill((255, 255, 255))  # Fill the surface with a white color

# Apply the bloom effect to the surface
a = 0
  # Angle = pi/4 (45 degrees)

# Display the bloomed surface
screen = pygame.display.set_mode((400, 400))
#screen.blit(bloomed_surface, (0, 0))


# Wait for the user to close the window
done = False
while not done:
    a = (a +0.1)%360
    #surface = pygame.image.load('img/water.png')
    bloomed_surface = highlight_outline(surface, int(a),45)
    screen.blit(bloomed_surface, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True