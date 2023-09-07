import pygame , math
import numpy as np
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
    lighting_angle_array = np.array([lighting_x, lighting_y])
    lighting_angle_array = np.transpose(lighting_angle_array, (1, 2, 0))

    # Calculate the dot product of the normal map and lighting angle
    dot_product = np.sum(normal_map_array * lighting_angle_array, axis=2)
    dot_product = np.maximum(dot_product, 0)

    # Apply the dot product to the texture color for each RGB channel
    result_array = np.clip(texture_array * dot_product[:, :, np.newaxis], 0, 1)

    # Convert the result array back to a Pygame surface
    result_surface = pygame.surfarray.make_surface((result_array * 255.0).astype(np.uint8))

    return result_surface
def create_color_change_surface(surface1, surface2):
    # Check if the surfaces have the same dimensions
    if surface1.get_size() != surface2.get_size():
        raise ValueError("Surfaces must have the same dimensions")

    # Create a new surface with the same dimensions as the input surfaces
    new_surface = pygame.Surface(surface1.get_size()).convert_alpha()

    # Iterate over each pixel in the surfaces
    for x in range(surface1.get_width()):
        for y in range(surface1.get_height()):
            # Get the color values of the pixels in surface1 and surface2
            color1 = surface1.get_at((x, y))
            color2 = surface2.get_at((x, y))

            # Calculate the color change between the pixels
            red_change = color2.r - color1.r
            green_change = color2.g - color1.g
            blue_change = color2.b - color1.b
            avgc = int((red_change + green_change + blue_change )/4)
            if avgc > 60:
                avgc = avgc +60
            # Set negative color changes to 0

            # Create a new color with the color change values
            new_color = (255, 255, 255,max(min(avgc, 255),60)-60)

            # Set the color of the corresponding pixel in the new surface
            new_surface.set_at((x, y), new_color)

    return new_surface
def specular(texture,normalmap,angle):
    return create_color_change_surface(apply_normal_map(texture,normalmap,angle), texture)
pygame.init()
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Color Change Demo")

# Create two test surfaces with different colors
surface1 = pygame.image.load("img/wendy.png")
surface3 = pygame.image.load("normaltest.png")
# Create a surface with color change
color_change_surface = create_color_change_surface(apply_normal_map(surface1,surface3,45), surface1)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit the surfaces onto the screen
    #screen.blit(surface1, (50, 50))
    #screen.blit(surface2, (250, 50))
    screen.blit(color_change_surface, (150, 250))

    # Update the display
    pygame.display.flip()