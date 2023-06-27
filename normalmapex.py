import pygame
import numpy as np
import math
import time

# Initialize Pygame
pygame.init()

def apply_normal_map(texture, normal_map, lighting_angle, section):
    #global cached_sin_angle, cached_cos_angle, previous_angle

    # Convert the lighting angle to radians
    lighting_angle_rad = math.radians(lighting_angle)
 
    # Check if the angle has changed
    #if lighting_angle_rad != previous_angle:
        # Cache the values of sin and cos
    cached_sin_angle = np.sin(lighting_angle_rad)
    cached_cos_angle = np.cos(lighting_angle_rad)
    previous_angle = lighting_angle_rad

    # Determine the section coordinates with wraparound
    height, width = texture.shape[:2]
    y_start = section[0] % height
    x_start = section[1] % width
    y_end = (y_start + 40) % height
    x_end = (x_start + 40) % width

    # Extract the wrapped section of the texture and normal map
    if y_end < y_start:
        texture_section = np.concatenate((texture[y_start:height, x_start:x_end], texture[0:y_end, x_start:x_end]), axis=0)
        normal_map_section = np.concatenate((normal_map[y_start:height, x_start:x_end], normal_map[0:y_end, x_start:x_end]), axis=0)
    elif x_end < x_start:
        texture_section = np.concatenate((texture[y_start:y_end, x_start:width], texture[y_start:y_end, 0:x_end]), axis=1)
        normal_map_section = np.concatenate((normal_map[y_start:y_end, x_start:width], normal_map[y_start:y_end, 0:x_end]), axis=1)
    else:
        texture_section = texture[y_start:y_end, x_start:x_end]
        normal_map_section = normal_map[y_start:y_end, x_start:x_end]

    # Calculate the dot product of the normal map and lighting angle using cached values
    dot_product = normal_map_section[..., 0] * cached_cos_angle + normal_map_section[..., 1] * cached_sin_angle
    dot_product = np.abs(dot_product)

    # Perform the multiplication and scaling in the same line
    result_array = np.clip(texture_section *255* dot_product[..., np.newaxis], 0, 255).astype(np.uint8)

    # Convert the result array to a Pygame surface
    result_surface = pygame.surfarray.make_surface(result_array)
    #result_surface = pygame.transform.scale2x(result_surface)
    #result_surface = pygame.transform.scale(result_surface,(840,640))

    return result_surface
# Set up the display
if __name__ == "__main__":
    display_width = 800
    display_height = 600
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Normal Mapping")

    # Load the texture and normal map images
    texture_image = pygame.transform.scale(pygame.image.load("Resources/MISC_ASSETS/Grass_color.png").convert(),(400,400))
    normal_map_image = pygame.transform.scale(pygame.image.load("Resources/MISC_ASSETS/Grass_normal.png").convert(),(400,400))

    # Get the dimensions of the texture
    tex_width, tex_height = texture_image.get_width(), texture_image.get_height()

    # Scale the normal map to match the texture dimensions
    #normal_map_image = pygame.transform.scale(normal_map_image, (tex_width, tex_height)).convert()

    # Convert the texture and normal map surfaces to NumPy arrays
    texture_array = pygame.surfarray.array3d(texture_image).astype(np.uint8) / 255.0
    normal_map_array = pygame.surfarray.array3d(normal_map_image).astype(np.uint8) / 255.0

    # Main game loop
    running = True
    t=0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate the lighting angle based on the current time
        lighting_angle = t % 360
        t = t + 1 % 360
        # Apply normal map to the texture with the lighting angle
        xtime = 0
        start_time = time.time() 
        result_surface = apply_normal_map(texture_array, normal_map_array, lighting_angle,(0,0))
        xtime =  ((time.time() - start_time) * 1000)
        execution_time = 25/(xtime )
        print(execution_time)

        # Draw the result surface on the display
        display.blit(result_surface, (0, 0))
        

        # Update the display
        pygame.display.update()

    # Quit the game
    pygame.quit()
