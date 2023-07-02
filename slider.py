import pygame
from pygame.locals import *
import sys
def reduce_list_values(lst, x):
    return [value - x for value in lst]
class SliderSwitch:
    def __init__(self, position, width=80, height=20, items=["ON","OFF"],state=0):#draws a slider on screen 
        self.position = position
        self.width = width
        self.height = height
        self.items = items
        self.num_items = len(items)
        self.is_slider = 1

        self.switch_color = (220, 220, 220)
        self.slider_color = (94, 180, 255)
        self.dslider_color = reduce_list_values(self.slider_color,50)
        self.dswitch_color = reduce_list_values(self.switch_color,50)
        self.slider_text_color = (255, 255, 255)
        self.text_font = pygame.font.Font(None, 24)

        self.slider_rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.slider_rect2 = pygame.Rect(self.position[0]-2, self.position[1]-2, self.width+2, self.height+2)

        self.selected_item = state % self.num_items

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.slider_rect.collidepoint(mouse_pos):
                if self.is_slider:
                    self.selected_item = int((mouse_pos[0] - self.position[0]) / (self.width / self.num_items))
                else:
                    self.selected_item = 1 - self.selected_item
        return self.items[self.selected_item]

    def draw(self, screen):
        pygame.draw.rect(screen, self.switch_color, self.slider_rect2, border_radius=self.height // 2)
        #pygame.draw.rect(screen, self.dswitch_color, self.slider_rect, border_radius=self.height // 2)

        if self.is_slider:
            item_width = self.width // self.num_items
            for i in range(self.num_items):
                item_rect = pygame.Rect(self.position[0] + i * item_width, self.position[1], item_width, self.height)
                item_rect2 = pygame.Rect((self.position[0] + i * item_width)+2.5, self.position[1]+2.5, item_width-5, self.height-5)
                pygame.draw.rect(screen, self.slider_color if i == self.selected_item else self.switch_color,
                                 item_rect, border_radius=self.height // 2)
                pygame.draw.rect(screen, self.dslider_color if i == self.selected_item else self.dswitch_color,
                                 item_rect2, border_radius=self.height // 2)
                text = self.text_font.render(str(self.items[i]), True, self.slider_text_color)
                text_rect = text.get_rect(center=item_rect.center)
                screen.blit(text, text_rect)
        

