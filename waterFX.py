
import pygame
import pygame.surfarray
import numpy as np
import math
#xit = pygame.image.load
#def load_image(filename):
   # global xit
    #print("Image loaded:", filename)
    #return xit(filename)
#pygame.image.load = load_image
ptextures = {}#optimisation to not need a rtx 4090 XYT
def surface_to_array(surface):
    width, height = surface.get_size()
    byte_string = pygame.image.tostring(surface, 'RGB')
    array_1d = np.frombuffer(byte_string, dtype=np.uint8)
    array_3d = array_1d.reshape((height, width, 3))

    return array_3d / 255.0
def surface_to_array(surface):
    array_3d = pygame.surfarray.array3d(surface).astype(np.float32)
    array_3d /= 255.0
    return array_3d
class nxtexture(): # a texture pointer class
    def __init__(self,location,a=1,rescale=1):
        global ptextures
        if not str(location) in ptextures:
            a = 1
            preimg = pygame.image.load(str(location)).convert_alpha()
            #preimg = pygame.surfarray.array3d(preimg).astype(np.uint8) / 255.0
            preimg = surface_to_array(preimg)
            ptextures[str(location)] = preimg
            del(preimg)
        self.location = str(location)
    def gt(self):
        global ptextures
        return ptextures[self.location]


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
    texture_array = surface_to_array(texture)

    # Convert the displacement map surface to a NumPy array
    displacement_map_array = surface_to_array(displacement_map)
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
def apply_normal_map2(texture, normal_map, lighting_angle):
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

def specularhigh(texture,normalmap,direction):
    color_change_surface = create_color_change_surface(apply_normal_map2(texture,normalmap,direction), texture)

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

def modify_image_color(surface, red_modifier, green_modifier, blue_modifier):
    # Convert the surface to a NumPy array
    pixels = pygame.surfarray.pixels3d(surface)

    # Modify the color channels using NumPy array operations
    pixels[..., 0] = np.minimum(pixels[..., 0] * red_modifier, 255)
    pixels[..., 1] = np.minimum(pixels[..., 1] * green_modifier, 255)
    pixels[..., 2] = np.minimum(pixels[..., 2] * blue_modifier, 255)

    # Delete the NumPy array to unlock the surface
    del pixels
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


def apply_normal_map(texture, normal_map, lighting_angle, section):
    #global cached_sin_angle, cached_cos_angle, previous_angle
    texture = nxtexture(texture).gt()
    normal_map = nxtexture(normal_map).gt()
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
    y_end = (y_start + 20) % height
    x_end = (x_start + 20) % width

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
    result_surface = pygame.transform.scale2x(result_surface)
    return result_surface


def get_texture_slice(texture, x, y, slice_size=40):
    x = int(x)
    y = int(y)

    texture_width, texture_height = texture.get_width(), texture.get_height()

    tile_x = x // texture_width
    tile_y = y // texture_height

    slice_x = x % texture_width
    slice_y = y % texture_height

    wraparound_x = (slice_x + slice_size) % texture_width
    wraparound_y = (slice_y + slice_size) % texture_height

    slice_texture = pygame.Surface((slice_size, slice_size), pygame.SRCALPHA)

    if wraparound_x >= slice_x and wraparound_y >= slice_y:
        slice_rect = pygame.Rect(slice_x, slice_y, slice_size, slice_size)
        slice_texture.blit(texture, (0, 0), slice_rect)
    else:
        subsurfaces = []

        if wraparound_x < slice_x:
            subsurfaces.append((slice_x, slice_y, texture_width - slice_x, slice_size))
            subsurfaces.append((0, slice_y, slice_size - (texture_width - slice_x), slice_size))

        if wraparound_y < slice_y:
            subsurfaces.append((slice_x, slice_y, slice_size, texture_height - slice_y))
            subsurfaces.append((slice_x, 0, slice_size, slice_size - (texture_height - slice_y)))

        if wraparound_x < slice_x and wraparound_y < slice_y:
            subsurfaces.append((slice_x, slice_y, texture_width - slice_x, texture_height - slice_y))
            subsurfaces.append((0, slice_y, slice_size - (texture_width - slice_x), texture_height - slice_y))
            subsurfaces.append((slice_x, 0, texture_width - slice_x, slice_size - (texture_height - slice_y)))
            subsurfaces.append((0, 0, slice_size - (texture_width - slice_x), slice_size - (texture_height - slice_y)))

        for subsurface in subsurfaces:
            src_x, src_y, dest_w, dest_h = subsurface
            slice_rect = pygame.Rect(src_x, src_y, dest_w, dest_h)
            dest_x = 0 if src_x != 0 else texture_width - slice_x
            dest_y = 0 if src_y != 0 else texture_height - slice_y
            slice_texture.blit(texture, (dest_x, dest_y), slice_rect)

    return slice_texture
def get_lowest_nontransparent_pixel(image):
    height = image.get_height()
    for y in range(height-1, -1, -1):
        for x in range(image.get_width()):
            alpha = image.get_at((x, y))[3]
            if alpha > 0:
                return y
    return height


def blur_surface(surface, blur_factor):
    width, height = surface.get_size()
    blurred_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    
    for x in range(width):
        for y in range(height):
            total_r, total_g, total_b, total_a = 0, 0, 0, 0
            count = 0
            
            for dx in range(-blur_factor, blur_factor + 1):
                for dy in range(-blur_factor, blur_factor + 1):
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < width and 0 <= ny < height:
                        r, g, b, a = surface.get_at((nx, ny))
                        total_r += r
                        total_g += g
                        total_b += b
                        total_a += a
                        count += 1

            blurred_surface.set_at((x, y), (
                total_r // count,
                total_g // count,
                total_b // count,
                total_a // count
            ))
    
    return blurred_surface

def add_shadow(image, shadow_type):
    shadow_surface = pygame.Surface(image.get_size()).convert_alpha()
    shadow_color = pygame.Color(0, 0, 0, 128)

    if shadow_type == "reflected":
        shadow_scale = (1, 0.3)
        sz = image.get_size()
        shadow_position = (0, int(get_lowest_nontransparent_pixel(image)-(image.get_height()/10)))
        shadow_surface = pygame.transform.flip(shadow_surface, False, True)  # Flip the shadow vertically
        #

    elif shadow_type == "below":
        shadow_scale = (1, 1)
        shadow_position = (0, image.get_height()/20)

    shadow_surface.fill((0, 0, 0, 0))
    preimg = image
    if shadow_type == "reflected":
        preimg = pygame.transform.flip(image, False, True)
    shadow_surface.blit(pygame.transform.scale(preimg, (
        int(image.get_width() * shadow_scale[0]),
        int(image.get_height() * shadow_scale[1]))), (0, 0))
    shadow_surface.fill(shadow_color, special_flags=pygame.BLEND_RGBA_MULT)
    shadow_surface = blur_surface(shadow_surface,1)
    new_image = pygame.Surface((shadow_surface.get_width(), shadow_surface.get_height() + image.get_height())).convert_alpha()
    new_image.fill((0, 0, 0, 0))
    new_image.blit(shadow_surface, shadow_position)
    new_image.blit(image, (0, 0))
    

    return new_image

def highlight_outline(surface, angle, angle_range=45):
    temp_surface = 0
    temp_surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
    
    angle_range = angle_range 
    center_x = surface.get_width() // 2
    center_y = surface.get_height() // 2

    width = surface.get_width()
    height = surface.get_height()
    
    #temp_surface.fill((0,0,0,1))
    
    
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
                xadd = (hash(str(pixel_angle)+"x")%4)-4
                yadd = (hash(str(pixel_angle)+"x")%4)-4
                #pygame.draw.circle(temp_surface, (255,255,255,int((angle_range-min(abs(angle_diff), 255))*0.04)), (x, y), int((angle_range-min(abs(angle_diff), 255))*0.06))  # Highlight the pixel with red color
                pygame.draw.circle(temp_surface, (255,255,255,int((angle_range-min(abs(angle_diff), angle_range)))), (x+xadd, y+yadd), int((angle_range-min(abs(angle_diff), angle_range))*0.09))
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
                xadd = (hash(str(pixel_angle)+"x")%4)-2
                yadd = (hash(str(pixel_angle)+"x")%4)-2
                #temp_surface.set_at((x, y), (min(angle_diff, 255), 0, 0))  # Highlight the pixel with red color
                pygame.draw.circle(temp_surface, (255,255,255,int((angle_range-min(abs(angle_diff), angle_range)))), (x+xadd, y+yadd), int((angle_range-min(abs(angle_diff), angle_range))*0.09))  # Highlight the pixel with red color

            #else:
                #temp_surface.set_at((x, y), (0, 255, 0))  # Highlight the pixel with green color

    return temp_surface

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
            #new_color = (255, 255, 255,max(min(avgc, 255),60)-60)
            new_color = (255, 255, 255, max(min(int(195 / (1 + math.exp(-0.1 * (avgc - 127)))) + 60, 255), 50))

            # Set the color of the corresponding pixel in the new surface
            new_surface.set_at((x, y), new_color)

    return new_surface
def create_color_change_surface2(surface1, surface2):
    # Check if the surfaces have the same dimensions
    if surface1.get_size() != surface2.get_size():
        raise ValueError("Surfaces must have the same dimensions")

    # Convert the surfaces to NumPy arrays
    array1 = pygame.surfarray.pixels3d(surface1)
    array2 = pygame.surfarray.pixels3d(surface2)

    # Calculate the color change between the arrays
    color_change = array2 - array1

    # Adjust the color change values
    color_change = np.clip(color_change, -60, 195) + 60

    # Create a new surface with the adjusted color change values
    new_surface = pygame.surfarray.make_surface(color_change)

    return new_surface
def create_color_change_surface(surface1, surface2):
    new_surface = create_color_change_surface2(surface1, surface2)
    new_surface = copy_alpha(surface2,new_surface)
    return new_surface



texturecache = None
normalcache = None
tnhash = "ewq"

def copy_alpha(src_surface, dest_surface):
    if not src_surface.get_masks()[3]:  # Check if source surface lacks an alpha channel
        src_surface = src_surface.convert_alpha()  # Convert source to a surface with alpha channel

    if not dest_surface.get_masks()[3]:  # Check if destination surface lacks an alpha channel
        dest_surface = dest_surface.convert_alpha()  # Convert destination to a surface with alpha channel

    dest_pixels = pygame.surfarray.pixels_alpha(dest_surface)
    src_pixels = pygame.surfarray.pixels_alpha(src_surface)
    dest_pixels[:] = src_pixels[:]

    del src_pixels
    del dest_pixels

    return dest_surface
def specular(texture,normalmap,angle):
    global texturecache , normalcache , tnhash
    pxf = 20
    txhash = str(texture) + str(normalmap)
    if not  (txhash == tnhash):
        texturecache = pygame.transform.smoothscale(texture,(20,20))
        normalcache = pygame.transform.smoothscale(normalmap,(20,20))
    return pygame.transform.smoothscale(create_color_change_surface(apply_normal_map2(texture,normalmap,angle), texture),(40,40))