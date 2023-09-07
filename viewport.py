import pygame
import numpy as np

class Viewport():
    def __init__(self, x, y, image, screen):
        self.rect = [screen.get_width(), screen.get_height()]
        self.pb = pygame.surface.Surface(self.rect)
        self.xyt = [0, 0]
        self.nxtd = pygame.surfarray.array2d(self.pb)
        self.sc(x,y)
    def draw(self, screen):
        #pygame.surfarray.bli
        pygame.surfarray.blit_array(screen,self.nxtd)

    def sc(self, x, y):
        x = int(x) % 41
        y = int(y) % 41
        sdx = x - self.xyt[0]
        sdy = y - self.xyt[1]
        self.xyt[1] = y
        self.xyt[0]=x
        self.pb.scroll(sdx, sdy)
        self.nxtd = pygame.surfarray.array2d(self.pb)

    def setimage(self, image):
        self.pb.fill((0, 0, 0))
        self.pb.blit(image, self.xyt)
        #self.xyt = [0, 0]

if __name__ == '__main__':
# Initialize Pygame
    pygame.init()

    # Set up the screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Viewport Example")

    # Load the image
    image_path = "image.png"
    image = pygame.image.load(image_path)

    # Create an instance of the Viewport class
    viewport = Viewport(0, 0, image, screen)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the viewport position
        viewport.sc(1, 1)

        # Set the image in the viewport
        viewport.setimage(image)
        x=0
        while True:
           x=(x+1)%40
           viewport.sc(x, 1)
           viewport.draw(screen, 0, 0)
           pygame.display.flip()
        # Clear the screen
        #screen.fill((0, 0, 0))

        # Draw the viewport onto the screen
        

        # Update the display
        

    # Quit the game
    pygame.quit()
