# import pygame
# import numpy as np
# import math
# def apply_ripple_to_blits(blits_list, displacement_map, amplitude, speed):
#     # Create a surface to store the result of the blits
#     result_image = pygame.Surface(pygame.display.get_surface().get_size())
# 
#     # Perform the blit operations
#     result_image.blits(blits_list)
# 
#     # Create a copy of the result image to preserve the original
#     copied_image = result_image.copy()
# 
#     # Apply the ripple effect to the copied image
#     copied_image = apply_ripple(copied_image, displacement_map, amplitude, speed)
# 
#     # Create an updated list of blit operations
#     updated_blits_list = []
# 
#     # Iterate over the original and copied images, updating only the modified pixels
#     for y in range(result_image.get_height()):
#         for x in range(result_image.get_width()):
#             original_color = result_image.get_at((x, y))
#             copied_color = copied_image.get_at((x, y))
# 
#             # Check if the pixel was modified by the blit operations
#             if original_color != copied_color:
#                 # Calculate the position of the pixel
#                 pos = (x, y)
# 
#                 # Find the original surface and rect in the blits list
#                 for surf, rect in blits_list:
#                     #if rect.collidepoint(pos):
#                         updated_blits_list.append((surf, rect))
# 
#                 # Add the modified pixel to the updated blits list
#                 updated_blits_list.append((copied_image, pygame.Rect(pos, (1, 1))))
# 
#     return updated_blits_list
# def apply_ripple(texture, displacement_map, amplitude, speed):
#     width, height = texture.get_width(), texture.get_height()
#     displacement_width, displacement_height = displacement_map.get_width(), displacement_map.get_height()
# 
#     # Create NumPy arrays from the textures for faster pixel manipulation
#     texture_pixels = pygame.surfarray.pixels3d(texture)
#     displacement_pixels = pygame.surfarray.pixels3d(displacement_map)
# 
#     # Create a new surface to hold the result
#     result_surface = pygame.Surface((width, height))
# 
#     for y in range(height):
#         for x in range(width):
#             # Calculate the displacement amount based on the displacement map
#             displacement_x = displacement_pixels[x % displacement_width, y % displacement_height, 2] / 255.0 * amplitude
#             displacement_y = displacement_pixels[x % displacement_width, y % displacement_height, 1] / 255.0 * amplitude
# 
#             # Calculate the new coordinates based on the ripple effect
#             new_x = int(x + displacement_x * np.sin(speed * y))
#             new_y = int(y + displacement_y * np.sin(speed * x))
# 
#             # Get the pixel color from the texture at the new coordinates
#             pixel_color = texture_pixels[new_x % width, new_y % height]
# 
#             # Set the pixel color in the result surface
#             result_surface.set_at((x, y), pixel_color)
# 
#     # Release the reference to the NumPy arrays to avoid memory leaks
#     del texture_pixels
#     del displacement_pixels
# 
#     return result_surface
# def generate_texture(time,width=40, height=40):
#     SHOW_TILING = False
#     pixels = pygame.Surface((width, height))
#     TAU = 6.28318530718
#     MAX_ITER = 5
#     for y in range(height):
#         for x in range(width):
#             uv_x = (x % 40) / 40.0
#             uv_y = (y % 40) / 40.0
#             uv = [uv_x, uv_y]
#             
#             if SHOW_TILING:
#                 p = [(uv[0] * TAU * 2.0) % TAU - 250.0, (uv[1] * TAU * 2.0) % TAU - 250.0]
#             else:
#                 p = [(uv[0] * TAU) % TAU - 250.0, (uv[1] * TAU) % TAU - 250.0]
#             
#             i = p.copy()
#             c = 1.0
#             inten = 0.005
#             
#             for n in range(MAX_ITER):
#                 t = time * (1.0 - (3.5 / float(n + 1)))
#                 i = [p[0] + (math.cos(t - i[0]) + math.sin(t + i[1])),
#                      p[1] + (math.sin(t - i[1]) + math.cos(t + i[0]))]
#                 c += 1.0 / math.hypot(p[0] / (math.sin(i[0] + t) / inten),
#                                       p[1] / (math.cos(i[1] + t) / inten))
#             
#             c /= float(MAX_ITER)
#             c = 1.17 - math.pow(c, 1.4)
#             colour = [math.pow(abs(c), 8.0)]
#             colour[0] = min(max(colour[0] + 0.0, 0.1), 1.0)
#             
#             if SHOW_TILING:
#                 pixel = [2.0 / width, 2.0 / height]
#                 uv[0] *= 2.0
#                 uv[1] *= 2.0
#                 f = math.floor(time * 0.5 % 2.0)  # Flash value.
#                 first = f if uv[0] >= pixel[0] and uv[1] >= pixel[1] else 0.0  # Rule out first screen pixels and flash.
#                 uv[0] %= 1.0
#                 uv[1] %= 1.0
#                 if uv[0] >= pixel[0] and uv[1] >= pixel[1]:
#                     colour = [1.0, 1.0, 0.0]  # Yellow line
# 
#             pixels.set_at((x, y), (int(colour[0] * 25), int(colour[0] * 65), int(colour[0] * 255)))
#                 #print(colour*255)
# 
#     
#     return pygame.transform.scale2x(pixels)
# 
# 
# 
# 
# import pygame
# import numpy as np
# 
# 
# def apply_bloom(surface, intensity):
#     if surface.get_bytesize() == 1:
#         # Convert indexed surface to 24-bit RGB surface
#         surface = surface.convert(24)
# 
#     # Extract RGB channels as separate arrays
#     pixels = pygame.surfarray.array3d(surface)
#     red_channel = pixels[:, :, 0].astype(np.float32)
#     green_channel = pixels[:, :, 1].astype(np.float32)
#     blue_channel = pixels[:, :, 2].astype(np.float32)
# 
#     # Apply bloom effect by adding blurred version of the image
#     blurred_surface = pygame.Surface(surface.get_size())
#     blurred_surface.blit(surface, (0, 0))
#     pygame.transform.scale(blurred_surface, (blurred_surface.get_width() // 2, blurred_surface.get_height() // 2))
#     pygame.transform.scale(blurred_surface, surface.get_size(), surface)
# 
#     # Adjust the intensity of the bloom effect
#     red_channel += intensity * pixels[:, :, 0]
#     green_channel += intensity * pixels[:, :, 1]
#     blue_channel += intensity * pixels[:, :, 2]
# 
#     # Clamp values between 0 and 255
#     red_channel = np.clip(red_channel, 0, 255).astype(np.uint8)
#     green_channel = np.clip(green_channel, 0, 255).astype(np.uint8)
#     blue_channel = np.clip(blue_channel, 0, 255).astype(np.uint8)
# 
#     # Combine the channels and create a new surface
#     del(blurred_surface)
#     del(pixels)
#     processed_surface = np.stack((red_channel, green_channel, blue_channel), axis=2)
#     return pygame.surfarray.make_surface(processed_surface)
# 
# 
# 
# 
# 
# def apply_color_curves(surface, red_curve, green_curve, blue_curve):
#     if surface.get_bytesize() == 1:
#         # Convert indexed surface to 24-bit RGB surface
#         surface = surface.convert(24)
# 
#     # Extract RGB channels as separate arrays
#     pixels = pygame.surfarray.array3d(surface)
#     red_channel = pixels[:, :, 0].astype(np.float32)
#     green_channel = pixels[:, :, 1].astype(np.float32)
#     blue_channel = pixels[:, :, 2].astype(np.float32)
# 
#     # Apply color curves to each channel
#     red_channel = red_curve * red_channel
#     green_channel = green_curve * green_channel
#     blue_channel = blue_curve * blue_channel
# 
#     # Clamp values between 0 and 255
#     red_channel = np.clip(red_channel, 0, 255).astype(np.uint8)
#     green_channel = np.clip(green_channel, 0, 255).astype(np.uint8)
#     blue_channel = np.clip(blue_channel, 0, 255).astype(np.uint8)
# 
#     # Combine the channels and create a new surface
#     processed_surface = np.stack((red_channel, green_channel, blue_channel), axis=2)
#     return pygame.surfarray.make_surface(processed_surface)
# 
# 
# 
# def apply_outline(surface, color, thickness):
#     # Create a new surface with the outline effect
#     outline_surface = pygame.Surface(surface.get_size())
#     outline_surface.blit(surface, (0, 0))
#     pygame.draw.rect(outline_surface, color, outline_surface.get_rect(), thickness)
# 
#     # Combine the original surface and outline surface
#     processed_surface = pygame.Surface(surface.get_size())
#     processed_surface.blit(surface, (0, 0))
#     processed_surface.blit(outline_surface, (0, 0))
# 
#     return processed_surface
import pygame
import numpy as np
import math

def replace_color(texture, target_color, replacement_color):
    # Create a copy of the texture to modify
    modified_texture = texture.copy()
    modified_texture.convert_alpha()

    # Convert the target and replacement colors to Pygame Color objects
    target_color = pygame.Color(*target_color)
    replacement_color = pygame.Color(*replacement_color)
    replacement_color.a =0

    # Iterate over each pixel in the texture
    for x in range(modified_texture.get_width()):
        for y in range(modified_texture.get_height()):
            # Get the color of the current pixel
            current_color = modified_texture.get_at((x, y))
            if current_color.r < 5 and current_color.b < 5 and current_color.g < 5:
                modified_texture.set_at((x, y), replacement_color)
                

    return modified_texture



def apply_waving_effect(texture, displacement_map, amplitude, frequency, phase_shift,frame_count):
    # Get the dimensions of the texture
    tex_width, tex_height = texture.get_width(), texture.get_height()

    # Convert the texture surface to a NumPy array
    texture_array = pygame.surfarray.pixels3d(texture).astype(np.float32) / 255.0

    # Convert the displacement map surface to a NumPy array
    displacement_map_array = pygame.surfarray.array3d(displacement_map).astype(np.float32) / 255.0
    time_factor = frame_count / 120.0
    # Create the wave displacement array
    x = np.arange(tex_width) / (frequency* time_factor )+ phase_shift
    y = np.arange(tex_height) / (frequency* time_factor) + phase_shift
    xx, yy = np.meshgrid(x, y)
    wave_displacement = amplitude * np.sin(xx + yy)

    # Apply the wave displacement to the texture coordinates
    coords = np.indices((tex_height, tex_width))
    coords[0] += wave_displacement.astype(int)
    coords[1] += wave_displacement.astype(int)
    coords = np.clip(coords, 0, tex_width - 1)

    # Apply the waving effect to the texture
    result_array = texture_array[coords[0], coords[1]]

    # Convert the result array back to a Pygame surface
    result_surface = pygame.surfarray.make_surface((result_array * 255.0).astype(np.uint8))
    result_surface.set_colorkey((0, 0, 0))  # Set black as the transparent color

    return result_surface
####




##
def apply_ripple_to_blits(blits_list, displacement_map, amplitude, speed):
    result_image = pygame.Surface(pygame.display.get_surface().get_size())
    result_image.blits(blits_list)
    copied_image = result_image.copy()
    copied_image = apply_ripple(copied_image, displacement_map, amplitude, speed)
    updated_blits_list = []

    for y in range(result_image.get_height()):
        for x in range(result_image.get_width()):
            original_color = result_image.get_at((x, y))
            copied_color = copied_image.get_at((x, y))

            if original_color != copied_color:
                pos = (x, y)
                for surf, rect in blits_list:
                    updated_blits_list.append((surf, rect))
                updated_blits_list.append((copied_image, pygame.Rect(pos, (1, 1))))

    return updated_blits_list


# def apply_ripple(texture, displacement_map, amplitude, speed):
#     width, height = texture.get_width(), texture.get_height()
#     displacement_width, displacement_height = displacement_map.get_width(), displacement_map.get_height()
#     texture_pixels = pygame.surfarray.pixels3d(texture)
#     displacement_pixels = pygame.surfarray.pixels3d(displacement_map)
#     result_surface = pygame.Surface((width, height))
# 
#     for y in range(height):
#         for x in range(width):
#             displacement_x = displacement_pixels[x % displacement_width, y % displacement_height, 2] / 255.0 * amplitude
#             displacement_y = displacement_pixels[x % displacement_width, y % displacement_height, 1] / 255.0 * amplitude
#             new_x = int(x + displacement_x * np.sin(speed * y))
#             new_y = int(y + displacement_y * np.sin(speed * x))
#             pixel_color = texture_pixels[new_x % width, new_y % height]
#             result_surface.set_at((x, y), pixel_color)
# 
#     del texture_pixels
#     del displacement_pixels
# 
#     return result_surface
def apply_ripple(texture, displacement_map, amplitude, speed):
    width, height = texture.get_width(), texture.get_height()
    displacement_width, displacement_height = displacement_map.get_width(), displacement_map.get_height()

    texture_pixels = pygame.surfarray.pixels3d(texture)
    displacement_pixels = pygame.surfarray.pixels3d(displacement_map)
    result_surface = pygame.Surface((width, height))

    x_indices = np.arange(width)
    y_indices = np.arange(height)
    x, y = np.meshgrid(x_indices, y_indices, indexing='ij')

    displacement_x = displacement_pixels[x % displacement_width, y % displacement_height, 2] / 255.0 * amplitude
    displacement_y = displacement_pixels[x % displacement_width, y % displacement_height, 1] / 255.0 * amplitude

    new_x = (x + displacement_x * np.sin(speed * y)).astype(int) % width
    new_y = (y + displacement_y * np.sin(speed * x)).astype(int) % height

    pixel_colors = texture_pixels[new_x, new_y]
    result_surface_pixels = pygame.surfarray.pixels3d(result_surface)
    result_surface_pixels[:, :] = pixel_colors

    del texture_pixels
    del displacement_pixels

    return result_surface

def apply_ripple(texture, displacement_map, amplitude, speed):
    width, height = texture.get_width(), texture.get_height()
    displacement_width, displacement_height = displacement_map.get_width(), displacement_map.get_height()

    texture_array = pygame.surfarray.array3d(texture)
    displacement_array = pygame.surfarray.array3d(displacement_map)
    result_array = np.empty_like(texture_array)

    x_indices = np.arange(width)
    y_indices = np.arange(height)
    x, y = np.meshgrid(x_indices, y_indices, indexing='ij')

    displacement_x = displacement_array[x % displacement_width, y % displacement_height, 2] / 255.0 * amplitude
    displacement_y = displacement_array[x % displacement_width, y % displacement_height, 1] / 255.0 * amplitude

    new_x = (x + displacement_x * np.sin(speed * y)).astype(int) % width
    new_y = (y + displacement_y * np.sin(speed * x)).astype(int) % height

    result_array[:, :] = texture_array[new_x, new_y]

    result_surface = pygame.surfarray.make_surface(result_array)

    return result_surface

def generate_texture(time, width=40, height=40):
    SHOW_TILING = False
    pixels = pygame.Surface((width, height))
    TAU = 6.28318530718
    MAX_ITER = 5

    for y in range(height):
        for x in range(width):
            uv_x = (x % 40) / 40.0
            uv_y = (y % 40) / 40.0
            uv = [uv_x, uv_y]

            if SHOW_TILING:
                p = [(uv[0] * TAU * 2.0) % TAU - 250.0, (uv[1] * TAU * 2.0) % TAU - 250.0]
            else:
                p = [(uv[0] * TAU) % TAU - 250.0, (uv[1] * TAU) % TAU - 250.0]

            i = p.copy()
            c = 1.0
            inten = 0.005

            for n in range(MAX_ITER):
                t = time * (1.0 - (3.5 / float(n + 1)))
                i = [p[0] + (math.cos(t - i[0]) + math.sin(t + i[1])),
                     p[1] + (math.sin(t - i[1]) + math.cos(t + i[0]))]
                c += 1.0 / math.hypot(p[0] / (math.sin(i[0] + t) / inten), p[1] / (math.cos(i[1] + t) / inten))

            c /= float(MAX_ITER)
            c = 1.17 - math.pow(c, 1.4)
            colour = [math.pow(abs(c), 8.0)]
            colour[0] = min(max(colour[0] + 0.0, 0.1), 1.0)

            if SHOW_TILING:
                pixel = [2.0 / width, 2.0 / height]
                uv[0] *= 2.0
                uv[1] *= 2.0
                f = math.floor(time * 0.5 % 2.0)  # Flash value.
                first = f if uv[0] >= pixel[0] and uv[1] >= pixel[1] else 0.0  # Rule out first screen pixels and flash.
                uv[0] %= 1.0
                uv[1] %= 1.0
                if uv[0] >= pixel[0] and uv[1] >= pixel[1]:
                    colour = [1.0, 1.0, 0.0]  # Yellow line

            pixels.set_at((x, y), (int(colour[0] * 25), int(colour[0] * 65), int(colour[0] * 255)))

    return pygame.transform.scale2x(pixels)


# def apply_bloom(surface, intensity):
#     if surface.get_bytesize() == 1:
#         surface = surface.convert(24)
# 
#     pixels = pygame.surfarray.array3d(surface)
#     red_channel = pixels[:, :, 0].astype(np.float32)
#     green_channel = pixels[:, :, 1].astype(np.float32)
#     blue_channel = pixels[:, :, 2].astype(np.float32)
# 
#     blurred_surface = pygame.Surface(surface.get_size())
#     blurred_surface.blit(surface, (0, 0))
#     pygame.transform.scale(blurred_surface, (blurred_surface.get_width() // 2, blurred_surface.get_height() // 2))
#     pygame.transform.scale(blurred_surface, surface.get_size(), surface)
# 
#     red_channel += intensity * pixels[:, :, 0]
#     green_channel += intensity * pixels[:, :, 1]
#     blue_channel += intensity * pixels[:, :, 2]
# 
#     red_channel = np.clip(red_channel, 0, 255).astype(np.uint8)
#     green_channel = np.clip(green_channel, 0, 255).astype(np.uint8)
#     blue_channel = np.clip(blue_channel, 0, 255).astype(np.uint8)
# 
#     del blurred_surface
#     del pixels
#     processed_surface = np.stack((red_channel, green_channel, blue_channel), axis=2)
#     return pygame.surfarray.make_surface(processed_surface)
# 


import numpy as np

def apply_bloom(surface, intensity, threshold, radius):
    pixels = pygame.surfarray.pixels3d(surface).astype(np.float32)
    width, height = surface.get_size()

    brightness = np.mean(pixels, axis=2)

    bright_pixels = brightness > threshold

    mask = np.zeros_like(pixels, dtype=bool)
    mask[..., 0] = bright_pixels
    mask[..., 1] = bright_pixels
    mask[..., 2] = bright_pixels

    red_channel = pixels[..., 0]
    green_channel = pixels[..., 1]
    blue_channel = pixels[..., 2]

    mask_pad = np.pad(mask, ((radius, radius), (radius, radius), (0, 0)), mode='constant')
    red_channel_pad = np.pad(red_channel, radius, mode='edge')
    green_channel_pad = np.pad(green_channel, radius, mode='edge')
    blue_channel_pad = np.pad(blue_channel, radius, mode='edge')

    y_indices, x_indices = np.nonzero(mask_pad)[:2]  # Use only the first two arrays

    y_indices = np.ravel(y_indices).astype(int)  # Convert to 1D array of integers
    x_indices = np.ravel(x_indices).astype(int)  # Convert to 1D array of integers

    neighborhood_red = red_channel_pad[np.ix_(y_indices - radius, x_indices - radius)]
    neighborhood_green = green_channel_pad[np.ix_(y_indices - radius, x_indices - radius)]
    neighborhood_blue = blue_channel_pad[np.ix_(y_indices - radius, x_indices - radius)]
    red_channel[y_indices - radius, x_indices - radius] += intensity * np.mean(neighborhood_red)
    green_channel[y_indices - radius, x_indices - radius] += intensity * np.mean(neighborhood_green)
    blue_channel[y_indices - radius, x_indices - radius] += intensity * np.mean(neighborhood_blue)
    np.clip(red_channel, 0, 255, out=red_channel)
    np.clip(green_channel, 0, 255, out=green_channel)
    np.clip(blue_channel, 0, 255, out=blue_channel)

    processed_surface = np.stack((red_channel, green_channel, blue_channel), axis=2)
    return pygame.surfarray.make_surface(processed_surface.astype(np.uint8))


# def apply_color_curves(surface, red_curve, green_curve, blue_curve):
#     if surface.get_bytesize() == 1:
#         surface = surface.convert(24)
# 
#     pixels = pygame.surfarray.array3d(surface)
#     red_channel = pixels[:, :, 0].astype(np.float32)
#     green_channel = pixels[:, :, 1].astype(np.float32)
#     blue_channel = pixels[:, :, 2].astype(np.float32)
# 
#     red_channel = np.clip(red_curve * red_channel, 0, 255).astype(np.uint8)
#     green_channel = np.clip(green_curve * green_channel, 0, 255).astype(np.uint8)
#     blue_channel = np.clip(blue_curve * blue_channel, 0, 255).astype(np.uint8)
# 
#     processed_surface = np.stack((red_channel, green_channel, blue_channel), axis=2)
#     return pygame.surfarray.make_surface(processed_surface)
def apply_color_curves(surface, red_curve, green_curve, blue_curve):
    if surface.get_bytesize() == 1:
        surface = surface.convert(24)

    pixels = pygame.surfarray.pixels3d(surface)

    pixels[:, :, 0] = np.clip((red_curve * pixels[:, :, 0]).astype(np.uint8), 0, 255)
    pixels[:, :, 1] = np.clip((green_curve * pixels[:, :, 1]).astype(np.uint8), 0, 255)
    pixels[:, :, 2] = np.clip((blue_curve * pixels[:, :, 2]).astype(np.uint8), 0, 255)

    return surface

def apply_outline(surface, color, thickness):
    outline_surface = pygame.Surface(surface.get_size())
    outline_surface.blit(surface, (0, 0))
    pygame.draw.rect(outline_surface, color, outline_surface.get_rect(), thickness)

    processed_surface = pygame.Surface(surface.get_size())
    processed_surface.blit(surface, (0, 0))
    processed_surface.blit(outline_surface, (0, 0))

    return processed_surface

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



# def get_texture_slice(texture, x, y,slice_size=40):
#     x = int(x)
#     y = int(y)
#     # Get the dimensions of the source texture
#     texture_width, texture_height = texture.get_width(), texture.get_height()
# 
#     # Calculate the tile coordinates within the source texture
#     tile_x = x // texture_width
#     tile_y = y // texture_height
# 
#     # Calculate the slice coordinates within the tile
#     slice_x = x % texture_width
#     slice_y = y % texture_height
# 
#     # Create a new surface for the slice
#     slice_texture = pygame.Surface((slice_size, slice_size), pygame.SRCALPHA)
# 
#     # Iterate over each pixel in the slice
#     for slice_i in range(slice_size):
#         for slice_j in range(slice_size):
#             # Calculate the coordinates within the texture
#             texture_x = (slice_x + slice_i) % texture_width
#             texture_y = (slice_y + slice_j) % texture_height
# 
#             # Get the color of the corresponding pixel in the texture
#             pixel_color = texture.get_at((texture_x, texture_y))
# 
#             # Set the color in the slice texture
#             slice_texture.set_at((slice_i, slice_j), pixel_color)
# 
#     return slice_texture



# 
# 
def get_texture_slice(texture, x, y, slice_size=40):
    x = int(x)
    y = int(y)

    # Get the dimensions of the source texture
    texture_width, texture_height = texture.get_width(), texture.get_height()

    # Calculate the tile coordinates within the source texture
    tile_x = x // texture_width
    tile_y = y // texture_height

    # Calculate the slice coordinates within the tile
    slice_x = x % texture_width
    slice_y = y % texture_height

    # Calculate the wraparound coordinates if the slice is outside the texture boundaries
    wraparound_x = (slice_x + slice_size) % texture_width
    wraparound_y = (slice_y + slice_size) % texture_height

    # Create a new surface for the slice
    slice_texture = pygame.Surface((slice_size, slice_size), pygame.SRCALPHA)

    if wraparound_x >= slice_x and wraparound_y >= slice_y:
        # Case: No wraparound in either x or y direction
        slice_texture.blit(texture, (0, 0), pygame.Rect(slice_x, slice_y, slice_size, slice_size))
    elif wraparound_x < slice_x and wraparound_y >= slice_y:
        # Case: Wraparound in x direction
        slice_texture.blit(texture, (0, 0), pygame.Rect(slice_x, slice_y, texture_width - slice_x, slice_size))
        slice_texture.blit(texture, (texture_width - slice_x, 0), pygame.Rect(0, slice_y, slice_size - (texture_width - slice_x), slice_size))
    elif wraparound_x >= slice_x and wraparound_y < slice_y:
        # Case: Wraparound in y direction
        slice_texture.blit(texture, (0, 0), pygame.Rect(slice_x, slice_y, slice_size, texture_height - slice_y))
        slice_texture.blit(texture, (0, texture_height - slice_y), pygame.Rect(slice_x, 0, slice_size, slice_size - (texture_height - slice_y)))
    else:
        # Case: Wraparound in both x and y directions
        slice_texture.blit(texture, (0, 0), pygame.Rect(slice_x, slice_y, texture_width - slice_x, texture_height - slice_y))
        slice_texture.blit(texture, (texture_width - slice_x, 0), pygame.Rect(0, slice_y, slice_size - (texture_width - slice_x), texture_height - slice_y))
        slice_texture.blit(texture, (0, texture_height - slice_y), pygame.Rect(slice_x, 0, texture_width - slice_x, slice_size - (texture_height - slice_y)))
        slice_texture.blit(texture, (texture_width - slice_x, texture_height - slice_y), pygame.Rect(0, 0, slice_size - (texture_width - slice_x), slice_size - (texture_height - slice_y)))

    return slice_texture

def overlay_green_screen(background, foreground, green_color=(255, 255, 255,255), offset=(15, 0)):
    # Create a copy of the background surface
    overlay = background.copy()

    # Iterate over each pixel of the background surface
    for x in range(background.get_width()):
        for y in range(background.get_height()):
            # Get the color of the current pixel in the background
            bg_color = background.get_at((x, y))

            # Check if the color matches the green screen color
            if bg_color == green_color:
                # Calculate the coordinates for the current pixel in the foreground with the offset applied
                fg_x = (x + offset[0]) % foreground.get_width()
                fg_y = (y + offset[1]) % foreground.get_height()

                # Get the color of the current pixel in the foreground
                fg_pixel = foreground.get_at((fg_x, fg_y))

                # Combine the alpha value of the foreground pixel with the background color
                combined_color = (
                    fg_pixel[0],
                    fg_pixel[1],
                    fg_pixel[2],
                    bg_color[3]
                )

                # Set the color of the overlay surface to the combined color
                overlay.set_at((x, y), combined_color)

    # Return the overlay surface
    return overlay