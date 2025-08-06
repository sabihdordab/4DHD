import pygame
import math

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Layered Cartoon Body")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_rotated_rect(surface, color, rect, angle, width=0):
    shape_surf = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, (0, 0, rect[2], rect[3]), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    rotated_rect = rotated_surf.get_rect(center=(rect[0]+rect[2]//2, rect[1]+rect[3]//2))
    surface.blit(rotated_surf, rotated_rect.topleft)

class Layer:
    def __init__(self, name, draw_fn, visible=True):
        self.name = name
        self.draw_fn = draw_fn
        self.visible = visible

    def draw(self, surface):
        if self.visible and self.draw_fn:
            self.draw_fn(surface)

class LayeredBody:
    def __init__(self, surface, x=250, y=100, color=BLACK, skin_color=WHITE):
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.skin_color = skin_color
        self.layers = []
        self.hair_style = "short"
        self.create_layers()

    def create_layers(self):
        self.layers.append(Layer("legs_lower", self.draw_legs_lower))
        self.layers.append(Layer("legs_upper", self.draw_legs_upper))
        self.layers.append(Layer("ass_arc", self.draw_ass))
        self.layers.append(Layer("stomach", self.draw_stomach))
        self.layers.append(Layer("chest", self.draw_chest))
        self.layers.append(Layer("neck", self.draw_neck))
        self.layers.append(Layer("head", self.draw_head))
        self.layers.append(Layer("left_arm", self.draw_left_arm))
        self.layers.append(Layer("right_arm", self.draw_right_arm))

    def draw(self):
        for layer in self.layers:
            layer.draw(self.surface)

    def draw_head(self, surface):
        pygame.draw.circle(surface, self.skin_color, (self.x, self.y), 40)
        pygame.draw.circle(surface, self.color, (self.x, self.y), 40, 2)

    def draw_neck(self, surface):
        pygame.draw.rect(surface, self.skin_color, (self.x - 10, self.y + 40, 20, 20))
        pygame.draw.rect(surface, self.color, (self.x - 10, self.y + 40, 20, 20), 2)

    def draw_chest(self, surface):
        pygame.draw.rect(surface, self.skin_color, (self.x - 30, self.y + 60, 60, 60))
        pygame.draw.rect(surface, self.color, (self.x - 30, self.y + 60, 60, 60), 2)

    def draw_stomach(self, surface):
        pygame.draw.rect(surface, self.skin_color, (self.x - 15, self.y + 120, 30, 40))
        pygame.draw.rect(surface, self.color, (self.x - 15, self.y + 120, 30, 40), 2)

    def draw_ass(self, surface):
        pygame.draw.arc(surface, self.color, pygame.Rect(self.x - 25, self.y + 160, 50, 40),
                        math.radians(0), math.radians(180), 2)

    def draw_left_arm(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x - 60, self.y + 50, 20, 60), -40)
        draw_rotated_rect(surface, self.color, (self.x - 60, self.y + 50, 20, 60), -40, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x - 100, self.y + 95, 20, 60), -45)
        draw_rotated_rect(surface, self.color, (self.x - 100, self.y + 95, 20, 60), -45, 2)
        pygame.draw.circle(surface, self.skin_color, (self.x - 120, self.y + 155), 12)
        pygame.draw.circle(surface, self.color, (self.x - 120, self.y + 155), 12, 2)

    def draw_right_arm(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x + 40, self.y + 50, 20, 60), 40)
        draw_rotated_rect(surface, self.color, (self.x + 40, self.y + 50, 20, 60), 40, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x + 80, self.y + 95, 20, 60), 45)
        draw_rotated_rect(surface, self.color, (self.x + 80, self.y + 95, 20, 60), 45, 2)
        pygame.draw.circle(surface, self.skin_color, (self.x + 120, self.y + 155), 12)
        pygame.draw.circle(surface, self.color, (self.x + 120, self.y + 155), 12, 2)

    def draw_legs_upper(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x - 32, self.y + 180, 25, 80), -10)
        draw_rotated_rect(surface, self.color, (self.x - 32, self.y + 180, 25, 80), -10, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x + 6, self.y + 180, 25, 80), 10)
        draw_rotated_rect(surface, self.color, (self.x + 6, self.y + 180, 25, 80), 10, 2)

    def draw_legs_lower(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x - 45, self.y + 260, 30, 80), -7)
        draw_rotated_rect(surface, self.color, (self.x - 45, self.y + 260, 30, 80), -7, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x + 16, self.y + 260, 30, 80), 7)
        draw_rotated_rect(surface, self.color, (self.x + 16, self.y + 260, 30, 80), 7, 2)

class MaleBody(LayeredBody):
    def draw_head(self, surface):
        pygame.draw.circle(surface, self.skin_color, (self.x, self.y), 44)
        pygame.draw.circle(surface, self.color, (self.x, self.y), 44, 2)

    def draw_neck(self, surface):
        pygame.draw.rect(surface, self.skin_color, (self.x - 12, self.y + 44, 24, 20))
        pygame.draw.rect(surface, self.color, (self.x - 12, self.y + 44, 24, 20), 2)

    def draw_chest(self, surface):
        pygame.draw.rect(surface, self.skin_color, (self.x - 35, self.y + 64, 70, 65))
        pygame.draw.rect(surface, self.color, (self.x - 35, self.y + 64, 70, 65), 2)

    def draw_stomach(self, surface):
        pygame.draw.rect(surface, self.skin_color, (self.x - 18, self.y + 129, 36, 45))
        pygame.draw.rect(surface, self.color, (self.x - 18, self.y + 129, 36, 45), 2)

    def draw_left_arm(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x - 65, self.y + 52, 24, 70), -40)
        draw_rotated_rect(surface, self.color, (self.x - 65, self.y + 52, 24, 70), -40, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x - 108, self.y + 102, 24, 70), -45)
        draw_rotated_rect(surface, self.color, (self.x - 108, self.y + 102, 24, 70), -45, 2)
        pygame.draw.circle(surface, self.skin_color, (self.x - 130, self.y + 170), 12)
        pygame.draw.circle(surface, self.color, (self.x - 130, self.y + 170), 12, 2)

    def draw_right_arm(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x + 42, self.y + 52, 24, 70), 40)
        draw_rotated_rect(surface, self.color, (self.x + 42, self.y + 52, 24, 70), 40, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x + 85, self.y + 102, 24, 70), 45)
        draw_rotated_rect(surface, self.color, (self.x + 85, self.y + 102, 24, 70), 45, 2)
        pygame.draw.circle(surface, self.skin_color, (self.x + 130, self.y + 170), 12)
        pygame.draw.circle(surface, self.color, (self.x + 130, self.y + 170), 12, 2)

    def draw_legs_upper(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x - 36, self.y + 185, 28, 90), -10)
        draw_rotated_rect(surface, self.color, (self.x - 36, self.y + 185, 28, 90), -10, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x + 6, self.y + 185, 28, 90), 10)
        draw_rotated_rect(surface, self.color, (self.x + 6, self.y + 185, 28, 90), 10, 2)

    def draw_legs_lower(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x - 50, self.y + 275, 32, 85), -7)
        draw_rotated_rect(surface, self.color, (self.x - 50, self.y + 275, 32, 85), -7, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x + 20, self.y + 275, 32, 85), 7)
        draw_rotated_rect(surface, self.color, (self.x + 20, self.y + 275, 32, 85), 7, 2)
    
    def draw_ass(self, surface):
        pygame.draw.arc(surface, self.color, pygame.Rect(self.x - 25, self.y + 170, 50, 30), math.radians(0), math.radians(180), 2)

class FemaleBody(LayeredBody):
    def draw_hair(self, surface):
        pass

class MonsterBody(LayeredBody):
    def create_layers(self):
        self.layers.append(Layer("legs_lower", self.draw_legs_lower))
        self.layers.append(Layer("legs_upper", self.draw_legs_upper))
        self.layers.append(Layer("ass_arc", self.draw_ass))
        self.layers.append(Layer("stomach", self.draw_stomach))
        self.layers.append(Layer("chest", self.draw_chest))
        self.layers.append(Layer("neck", self.draw_neck))
        self.layers.append(Layer("head", self.draw_head))
        self.layers.append(Layer("arm1", self.draw_arm1))  
        self.layers.append(Layer("arm2", self.draw_arm2))  
        self.layers.append(Layer("arm3", self.draw_arm3))  
        self.layers.append(Layer("arm4", self.draw_arm4)) 
        self.layers.append(Layer("arm5", self.draw_arm5))  
        self.layers.append(Layer("arm6", self.draw_arm6))  

    
    def draw_arm1(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x - 70, self.y + 50, 20, 60), -30)
        draw_rotated_rect(surface, self.color, (self.x - 70, self.y + 50, 20, 60), -30, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x - 110, self.y + 80, 20, 60), -60)
        draw_rotated_rect(surface, self.color, (self.x - 110, self.y + 80, 20, 60), -60, 2)
        pygame.draw.circle(surface, self.skin_color, (self.x - 130, self.y + 130), 12)
        pygame.draw.circle(surface, self.color, (self.x - 130, self.y + 130), 12, 2)
    
    def draw_arm2(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x - 60, self.y + 70, 20, 60), 0)
        draw_rotated_rect(surface, self.color, (self.x - 60, self.y + 70, 20, 60), 0, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x - 60, self.y + 130, 20, 60), 0)
        draw_rotated_rect(surface, self.color, (self.x - 60, self.y + 130, 20, 60), 0, 2)
        pygame.draw.circle(surface, self.skin_color, (self.x - 50, self.y + 195), 12)
        pygame.draw.circle(surface, self.color, (self.x - 50, self.y + 195), 12, 2)
    
    def draw_arm3(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x - 50, self.y + 90, 20, 60), 30)
        draw_rotated_rect(surface, self.color, (self.x - 50, self.y + 90, 20, 60), 30, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x - 20, self.y + 140, 20, 60), 60)
        draw_rotated_rect(surface, self.color, (self.x - 20, self.y + 140, 20, 60), 60, 2)
        pygame.draw.circle(surface, self.skin_color, (self.x + 10, self.y + 190), 12)
        pygame.draw.circle(surface, self.color, (self.x + 10, self.y + 190), 12, 2)
    
    def draw_arm4(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x + 50, self.y + 50, 20, 60), 30)
        draw_rotated_rect(surface, self.color, (self.x + 50, self.y + 50, 20, 60), 30, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x + 90, self.y + 80, 20, 60), 60)
        draw_rotated_rect(surface, self.color, (self.x + 90, self.y + 80, 20, 60), 60, 2)
        pygame.draw.circle(surface, self.skin_color, (self.x + 130, self.y + 130), 12)
        pygame.draw.circle(surface, self.color, (self.x + 130, self.y + 130), 12, 2)
    
    def draw_arm5(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x + 40, self.y + 70, 20, 60), 0)
        draw_rotated_rect(surface, self.color, (self.x + 40, self.y + 70, 20, 60), 0, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x + 40, self.y + 130, 20, 60), 0)
        draw_rotated_rect(surface, self.color, (self.x + 40, self.y + 130, 20, 60), 0, 2)
        pygame.draw.circle(surface, self.skin_color, (self.x + 50, self.y + 195), 12)
        pygame.draw.circle(surface, self.color, (self.x + 50, self.y + 195), 12, 2)
    
    def draw_arm6(self, surface):
        draw_rotated_rect(surface, self.skin_color, (self.x + 30, self.y + 90, 20, 60), -30)
        draw_rotated_rect(surface, self.color, (self.x + 30, self.y + 90, 20, 60), -30, 2)
        draw_rotated_rect(surface, self.skin_color, (self.x, self.y + 140, 20, 60), -60)
        draw_rotated_rect(surface, self.color, (self.x, self.y + 140, 20, 60), -60, 2)
        pygame.draw.circle(surface, self.skin_color, (self.x - 10, self.y + 190), 12)
        pygame.draw.circle(surface, self.color, (self.x - 10, self.y + 190), 12, 2)
