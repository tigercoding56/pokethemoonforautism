import pygame
import numpy as np
import math
# Initialize Pygame


pygame.init()
def apply_normal_map(texture, normal_map, lighting_angle):
    # Convert the lighting angle to radians
    lighting_angle = math.radians(lighting_angle)

    # Get the dimensions of the texture
    tex_width, tex_height = texture.get_width(), texture.get_height()

    # Tile the normal map to match the texture dimensions
    normal_map = pygame.transform.scale(normal_map, (tex_width, tex_height))

    # Convert the texture surface to a NumPy array
    texture_array = pygame.surfarray.array3d(texture).astype(np.float32) / 255.0

    # Convert the normal map surface to a NumPy array
    normal_map_array = pygame.surfarray.array3d(normal_map).astype(np.float32) / 255.0

    # Calculate the lighting vector components
    lighting_x = np.cos(lighting_angle)
    lighting_y = np.sin(lighting_angle)

    # Create the lighting angle array with the same shape as the texture
    lighting_angle_array = np.zeros_like(texture_array)
    lighting_angle_array[:, :, 0] = lighting_x
    lighting_angle_array[:, :, 1] = lighting_y

    # Calculate the dot product of the normal map and lighting angle
    dot_product = np.sum(normal_map_array * lighting_angle_array, axis=2)
    dot_product = np.maximum(dot_product, 0)

    # Apply the dot product to the texture color for each RGB channel
    result_array = np.clip(texture_array * dot_product[:, :, np.newaxis], 0, 1)

    # Convert the result array back to a Pygame surface
    result_surface = pygame.surfarray.make_surface((result_array * 255.0).astype(np.uint8))

    return result_surface




# Set up the display
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Normal Mapping")

# Load the texture and normal map images
texture_image = pygame.image.load("img/wendy.png")
normal_map_image = pygame.image.load("normaltest.png")
lighting_angle = 45
x = pygame.time.get_ticks()
result_surface = apply_normal_map(texture_image, normal_map_image, lighting_angle)
o = pygame.time.get_ticks()
print(o-x)
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply normal map to the texture with a lighting angle
      # Adjust the lighting angle as desired
    lighting_angle = (lighting_angle + 1)%360
    result_surface = apply_normal_map(texture_image, normal_map_image, lighting_angle)
    # Draw the result surface on the display
    display.blit(result_surface, (0, 0))

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()