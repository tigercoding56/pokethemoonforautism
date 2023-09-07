import random
import pygame
import os

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SIZE = 64
GRID_SIZE = 4
NUM_FRAMES = 3

# Directory paths
base_directory = "img/spritesheet/Bases"
hair_directory = "img/spritesheet/Hair"
pants_directory = "img/spritesheet/Pants"
shoes_directory = "img/spritesheet/Shoes"
eye_color_directory = "img/spritesheet/EyeColor"
shirts_directory = "img/spritesheet/Shirts"
glasses_directory = "img/spritesheet/Glasses/"
cap_directory = "img/spritesheet/TruckerHat/"
hairband_directory = "img/spritesheet/HairBand/"
earingdir = "img/spritesheet/Earrings//"

class Sprite:
    def get_subimage(self,image, x, y, width=40, height=40):
        x = x*40
        y = (y-1)*40
        rect = pygame.Rect(x,y, width, height)
        subimage = image.subsurface(rect)
        return subimage
    def __init__(self, seed,gender="none"):
        self.seed = seed
        self.x = 0
        self.Spritesheet = self.generate_sprite(gender)
        self.sprites = [self.get_subimage(self.Spritesheet,1,5-i) for i in range(1,5)]

    def get_random_frame(self):
        random.seed(self.seed*self.x)
        self.x = self.x +1
        return random.randint(0, NUM_FRAMES - 1)

    def blit_sprite(self, sprite_sheet, sprite, x, y):
        sprite_sheet.blit(sprite, (0,  0))

    def get_random_file(self, directory,gender=".png"):
        random.seed(self.seed*self.x)
        self.x = self.x +1
        files = os.listdir(directory)
        files = [item for item in files if gender in item]
        file_path = os.path.join(directory, random.choice(files))
        sprite = pygame.image.load(file_path)
        return sprite

    def generate_sprite(self,gender="none"):
        # Initialize pygame
        pygame.init()
        sprite_sheet = pygame.Surface((120, 160), pygame.SRCALPHA)

        # Randomly select sprites
        random.seed(self.seed)
        glasses = 0
        cap = 0
        earring = 0
        hairband = 0
        if gender == "none":
            if random.randint(0,1) == 1:
                gender = "Guy"
                
            else:
                gender = "Girl"
                if random.randint(1,5) == 2:
                    hairband = 1
                    hairband_sprite = self.get_random_file(hairband_directory)
                if random.randint(1,5) == 2:
                    earring = 1
                    earring_sprite = self.get_random_file(earingdir)
            if random.randint(1,5) == 2:
                glasses = 1
                glasses_sprite = self.get_random_file(glasses_directory)
            if random.randint(1,5) == 2:
                cap = 1
                cap_sprite = self.get_random_file(cap_directory)
        base_sprite = self.get_random_file(base_directory,gender)
        hair_sprite = self.get_random_file(hair_directory,gender)
        eye_color_sprite = self.get_random_file(eye_color_directory)
        shirts_sprite = self.get_random_file(shirts_directory,gender)
        pants_sprite = self.get_random_file(pants_directory)
        shoes_sprite = self.get_random_file(shoes_directory)

        # Blit sprites on the sprite sheet
        self.blit_sprite(sprite_sheet, base_sprite, 0, 0)
        self.blit_sprite(sprite_sheet, eye_color_sprite, 0, 0)
        self.blit_sprite(sprite_sheet, hair_sprite, 0, 0)
        self.blit_sprite(sprite_sheet, shirts_sprite, 0, 0)
        self.blit_sprite(sprite_sheet, pants_sprite, 0, 0)
        self.blit_sprite(sprite_sheet, shoes_sprite, 0, 0)
        if earring:
            self.blit_sprite(sprite_sheet, earring_sprite, 0, 0)
        if cap:
            self.blit_sprite(sprite_sheet, cap_sprite, 0, 0)
        if hairband:
            self.blit_sprite(sprite_sheet, hairband_sprite, 0, 0)
        if glasses:
            self.blit_sprite(sprite_sheet, glasses_sprite, 0, 0)
        

        return sprite_sheet

if __name__ == "__main__":
    t=0
    seed = 4  # Example seed value
    sprite = Sprite(seed)

    # Display the generated sprite
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    seed = seed +1
                    sprite = Sprite(seed)
                if event.key == pygame.K_LEFT:
                    seed = seed -1
                    sprite = Sprite(seed)
                if event.key == pygame.K_SPACE:
                    print(seed)

        screen.fill((255, 255, 255))  # Fill with white color
        t = (t +0.1)%4
        #print(t)
        screen.blit(sprite.sprites[int(t)], (0, 0))

        pygame.display.flip()
        clock.tick(60)