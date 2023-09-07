import pygame

# Initialize Pygame and set the display mode
pygame.init()
window_size = (800, 600)
window = pygame.display.set_mode(window_size)

# Load the tile image
tile_image = pygame.image.load("img/wendy.png").convert_alpha()

# Define the tile size
tile_size = tile_image.get_size()

def get_lowest_nontransparent_pixel(image):
    height = image.get_height()
    for y in range(height-1, -1, -1):
        for x in range(image.get_width()):
            alpha = image.get_at((x, y))[3]
            if alpha > 0:
                return y
    return height

def add_shadow(image, shadow_type):
    shadow_surface = pygame.Surface(image.get_size()).convert_alpha()
    shadow_color = pygame.Color(0, 0, 0, 128)

    if shadow_type == "reflected":
        shadow_scale = (1, 0.3)
        shadow_position = (0, get_lowest_nontransparent_pixel(image))
        shadow_surface = pygame.transform.flip(shadow_surface, False, True)  # Flip the shadow vertically

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

    new_image = pygame.Surface((shadow_surface.get_width(), shadow_surface.get_height() + image.get_height())).convert_alpha()
    new_image.fill((0, 0, 0, 0))
    new_image.blit(shadow_surface, shadow_position)
    new_image.blit(image, (0, 0))
    

    return new_image

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill((255, 255, 255))

    # Create a sprite with shadow
    sprite_with_shadow = add_shadow(tile_image.copy(), "below")

    # Draw the sprite with shadow
    sprite_rect = sprite_with_shadow.get_rect()
    sprite_rect.center = (window_size[0] // 2, window_size[1] // 2)
    window.blit(sprite_with_shadow, sprite_rect)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()