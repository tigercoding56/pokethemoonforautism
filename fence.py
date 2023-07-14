import pygame
def generate_fence_texture(base_texture, left, up, right, down):
    fence_texture = pygame.Surface((40, 40), pygame.SRCALPHA)

    # Load the base texture
    base_image = pygame.image.load(base_texture).convert_alpha()

    # Fence colors
    fence_color = (0, 0, 0)  # Black color for fences
    post_color = (0, 0, 0, 0)  # Transparent color for fence posts

    # Fence dimensions
    fence_width = 8
    fence_height = 40
    post_radius = 4

    # Draw fences based on the given integers
    if left == 1:
        pygame.draw.rect(fence_texture, fence_color, (0, 0, fence_width, fence_height))
        fence_texture.blit(base_image, (0, 0), area=(0, 0, fence_width, fence_height))
    elif left == 2:
        pygame.draw.rect(fence_texture, fence_color, (0, 0, fence_width, fence_height))
        pygame.draw.circle(fence_texture, post_color, (fence_width // 2, fence_height // 2), post_radius)
        fence_texture.blit(base_image, (fence_width, 0), area=(0, 0, fence_width, fence_height))

    if up == 1:
        pygame.draw.rect(fence_texture, fence_color, (0, 0, fence_height, fence_width))
        fence_texture.blit(base_image, (0, 0), area=(0, 0, fence_height, fence_width))
    elif up == 2:
        pygame.draw.rect(fence_texture, fence_color, (0, 0, fence_height, fence_width))
        pygame.draw.circle(fence_texture, post_color, (fence_height // 2, fence_width // 2), post_radius)
        fence_texture.blit(base_image, (0, fence_width), area=(0, 0, fence_height, fence_width))

    if right == 1:
        pygame.draw.rect(fence_texture, fence_color, (40 - fence_width, 0, fence_width, fence_height))
        fence_texture.blit(base_image, (40 - fence_width, 0), area=(0, 0, fence_width, fence_height))
    elif right == 2:
        pygame.draw.rect(fence_texture, fence_color, (40 - fence_width, 0, fence_width, fence_height))
        pygame.draw.circle(fence_texture, post_color, (40 - fence_width // 2, fence_height // 2), post_radius)
        fence_texture.blit(base_image, (40 - 2 * fence_width, 0), area=(0, 0, fence_width, fence_height))

    if down == 1:
        pygame.draw.rect(fence_texture, fence_color, (0, 40 - fence_width, fence_height, fence_width))
        fence_texture.blit(base_image, (0, 40 - fence_width), area=(0, 0, fence_height, fence_width))
    elif down == 2:
        pygame.draw.rect(fence_texture, fence_color, (0, 40 - fence_width, fence_height, fence_width))
        pygame.draw.circle(fence_texture, post_color, (fence_height // 2, 40 - fence_width // 2), post_radius)
        fence_texture.blit(base_image, (0, 40 - 2 * fence_width), area=(0, 0, fence_height, fence_width))

    return fence_texture


# Example usage
pygame.init()
screen = pygame.display.set_mode((200, 200))
base_texture_path = 'img/path.png'  # Replace with the path to your base texture
fence_texture = generate_fence_texture(base_texture_path, 1, 1, 1, 1)  # Example values, modify as needed

# Display the generated fence texture

screen.blit(fence_texture, (80, 80))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()