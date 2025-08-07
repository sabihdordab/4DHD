import pygame
import sys
import os
import ast
import time
from model.character import FemaleBody, MaleBody , MonsterBody

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 40

CHARACTER_DISPLAY_WIDTH = 400  
CHARACTER_DISPLAY_HEIGHT = 500
CHARACTER_OFFSET_X = 0  
CHARACTER_OFFSET_Y = 50

ORIGINAL_DESIGN_SIZE = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Choose Character")

font = pygame.font.Font("assets/game.ttf", 15)
music = pygame.mixer.Sound("assets/30 Singularity.mp3")

COLOR_PALETTE = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 0, 255), 
    (0, 255, 0),
    (255, 192, 203),
    (255, 255, 0), 
    (0, 255, 255),
    (119, 190, 240), 
    (75, 53, 42),                     
    (255, 45, 209),   
    (128, 128, 128),  
    (255, 255, 255), 
    (72, 61, 139),
    (255, 20, 147),    
    (138, 43, 226),    
    (255, 215, 0),    
    (255, 69, 0),      
    (255, 105, 180),   
    (0, 250, 154),     
    (75, 0, 130),      
    (0, 191, 255),     
    (127, 255, 212),
    (139, 69, 19),    
    (119, 136, 153),
    (192, 192, 192),  
    (255, 140, 0),    
    (0, 206, 209),    
    (50, 50, 50),
    (255, 0, 255),
    (0, 255, 127),   
    (50, 205, 50),
    (255, 71, 87),    
    (72, 219, 251),   
    (29, 38, 125),    
    (128, 0, 128),    
]

SKIN_PALETTE = [
    (255, 255, 255),(255, 224, 189), (255, 220, 220),(255, 214, 186), 
    (0, 0, 0),(171, 136, 109),(245, 238, 230),(243, 215, 202)
]

BACKGROUND_PALETTE = [
    (255, 255, 255),  
    (240, 248, 255),  # Alice Blue
    (245, 245, 220),  # Beige
    (0, 0, 0),       
    (25, 25, 112),    # Midnight Blue
    (123, 104, 238),  # Medium Slate Blue
    (255, 192, 203),  # Pink
    (255, 182, 193),  # Light Pink
    (255, 160, 122),  # Light Salmon
    (152, 251, 152),  # Pale Green
    (173, 216, 230),  # Light Blue
    (135, 206, 235),  # Sky Blue
    (255, 255, 224),  # Light Yellow
    (255, 239, 213),  # Papaya Whip
    (221, 160, 221),  # Plum
    (216, 191, 216),  # Thistle
    (211, 211, 211),  # Light Gray
    (169, 169, 169),  # Dark Gray
    (255, 0, 0),
    (0, 0, 255), 
    (0, 255, 0),
    (255, 255, 0), 
    (0, 255, 255),
    (119, 190, 240), 
    (75, 53, 42),                     
    (255, 45, 209),   
    (128, 128, 128),  
    (72, 61, 139),
    (255, 20, 147),    
    (138, 43, 226),    
    (255, 215, 0),    
    (255, 69, 0),      
    (255, 105, 180),   
    (0, 250, 154),     
    (75, 0, 130),      
    (0, 191, 255),     
    (127, 255, 212),
    (119, 136, 153),
    (192, 192, 192),  
    (255, 140, 0),    
    (0, 206, 209),    
    (50, 50, 50),
    (255, 0, 255),
]

def adjust_style_coordinates(model, offset_x=CHARACTER_OFFSET_X, offset_y=CHARACTER_OFFSET_Y):
    adjusted_model = []
    for polygon, color in model:
        adjusted_polygon = []
        for x, y in polygon:
            new_x = x + offset_x
            new_y = y + offset_y
            adjusted_polygon.append((new_x, new_y))
        adjusted_model.append((adjusted_polygon, color))
    return adjusted_model

def draw_button(text, x, y, w, h, color=(0, 255, 0)):
    pygame.draw.rect(screen, color, (x, y, w, h))
    pygame.draw.rect(screen, BLACK, (x, y, w, h), 2)
    txt = font.render(text, True, BLACK)
    txt_rect = txt.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(txt, txt_rect)
    return pygame.Rect(x, y, w, h)

def draw_color_palette(x, y, selected_color=None, palette=None):
    color_rects = []
    cols = 4
    color_size = 30
    spacing = 5
    colors = palette if palette else COLOR_PALETTE
    for i, color in enumerate(colors):
        row = i // cols
        col = i % cols
        rect_x = x + col * (color_size + spacing)
        rect_y = y + row * (color_size + spacing)
        rect = pygame.Rect(rect_x, rect_y, color_size, color_size)
        pygame.draw.rect(screen, color, rect)
        border_width = 3 if color == selected_color else 1
        pygame.draw.rect(screen, BLACK, rect, border_width)
        color_rects.append((rect, color))
    return color_rects

def select_skin_color():
    selected_color = SKIN_PALETTE[0]
    running = True
    clock = pygame.time.Clock()
    while running:
        screen.fill(WHITE)
        txt = font.render("Choose Skin Color", True, BLACK)
        screen.blit(txt, (150, 30))
        color_rects = draw_color_palette(50, 80, selected_color, SKIN_PALETTE)
        pygame.draw.rect(screen, selected_color, (200, 200, 100, 100))
        pygame.draw.rect(screen, BLACK, (200, 200, 100, 100),2)
        txt2 = font.render("Select", True, BLACK)
        screen.blit(txt2, (225, 310))
        pygame.display.update()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for rect, color in color_rects:
                    if rect.collidepoint(mx, my):
                        selected_color = color
                if 200 <= mx <= 300 and 200 <= my <= 300:
                    running = False
    return selected_color

def draw_polygons_with_color(surface, model, color_override=None):
    for poly, original_color in model:
          color = original_color if original_color else color_override
          pygame.draw.polygon(surface, color, poly)
          pygame.draw.polygon(surface, BLACK, poly,2)

def draw_character_preview(surface, body_factory, selections, x_offset=0, y_offset=0):
    character = body_factory(surface)
    character.draw()

    if selections.get('shirt'):
        adjusted_shirt = adjust_style_coordinates(selections['shirt']['original_model'], 
                                                x_offset, y_offset)
        draw_polygons_with_color(surface, adjusted_shirt, selections['shirt']['color'])

    if selections.get('hair'):
        adjusted_hair = adjust_style_coordinates(selections['hair']['original_model'], 
                                               x_offset, y_offset)
        draw_polygons_with_color(surface, adjusted_hair, selections['hair']['color'])

    if selections.get('eye'):
        adjusted_eye = adjust_style_coordinates(selections['eye']['original_model'], 
                                              x_offset, y_offset)
        draw_polygons_with_color(surface, adjusted_eye, selections['eye']['color'])

    if selections.get('tail'):
        adjusted_tail = adjust_style_coordinates(selections['tail']['original_model'], 
                                                x_offset, y_offset)
        draw_polygons_with_color(surface, adjusted_tail, selections['tail']['color'])
    
    if selections.get('pants'):
        adjusted_pants = adjust_style_coordinates(selections['pants']['original_model'], 
                                                x_offset, y_offset)
        draw_polygons_with_color(surface, adjusted_pants, selections['pants']['color'])

    if selections.get('sucks'):
        adjusted_sucks = adjust_style_coordinates(selections['sucks']['original_model'], 
                                                x_offset, y_offset)
        draw_polygons_with_color(surface, adjusted_sucks, selections['sucks']['color'])

    if selections.get('shoes'):
        adjusted_shoes = adjust_style_coordinates(selections['shoes']['original_model'], 
                                                x_offset, y_offset)
        draw_polygons_with_color(surface, adjusted_shoes, selections['shoes']['color'])

    if selections.get('wings'):
        adjusted_wings = adjust_style_coordinates(selections['wings']['original_model'], 
                                                x_offset, y_offset)
        draw_polygons_with_color(surface, adjusted_wings, selections['wings']['color'])

    if selections.get('horn'):
        adjusted_horns = adjust_style_coordinates(selections['horn']['original_model'], 
                                                x_offset, y_offset)
        draw_polygons_with_color(surface, adjusted_horns, selections['horn']['color'])

    if selections.get('gun'):
        adjusted_gun = adjust_style_coordinates(selections['gun']['original_model'], 
                                                x_offset, y_offset)
        draw_polygons_with_color(surface, adjusted_gun, selections['gun']['color'])


def select_background_color(body_factory, selections):
    selected_color = BACKGROUND_PALETTE[0]  
    running = True
    clock = pygame.time.Clock()
    
    while running:
        screen.fill(selected_color)
        
        character_surface = pygame.Surface((CHARACTER_DISPLAY_WIDTH, CHARACTER_DISPLAY_HEIGHT), 
                                         pygame.SRCALPHA)
        draw_character_preview(character_surface, body_factory, selections)
        screen.blit(character_surface, (50, 50))
        
        title_color = WHITE if sum(selected_color) < 400 else BLACK
        title_text = font.render("Choose Background Color", True, title_color)
        screen.blit(title_text, (500, 30))
        
        color_rects = draw_color_palette(450, 50, selected_color, BACKGROUND_PALETTE)
        
        
        select_btn_color = (0, 255, 0) if sum(selected_color) > 400 else (0, 200, 0)
        select_btn = draw_button("Select Background", 500, 450, 150, 40, select_btn_color)
        
        pygame.display.update()
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                
                for rect, color in color_rects:
                    if rect.collidepoint(mx, my):
                        selected_color = color
                        break
                
                if select_btn.collidepoint(mx, my):
                    running = False
    
    return selected_color

def load_models(gender, category):
    path = os.path.join("model", "style", gender, f"{category}.txt")
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        return ast.literal_eval(f.read())

def select_base_body():
    body_classes = [FemaleBody, MaleBody, MonsterBody]  
    body_names = ["Female", "Male", "Monster"]  
    current_index = 0
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        character_surface = pygame.Surface((CHARACTER_DISPLAY_WIDTH, CHARACTER_DISPLAY_HEIGHT), pygame.SRCALPHA)
        character = body_classes[current_index](character_surface)
        character.draw()
        screen.blit(character_surface, (CHARACTER_OFFSET_X, CHARACTER_OFFSET_Y))

        if current_index > 0:
            draw_button("<- Prev", 50, HEIGHT - 60, BUTTON_WIDTH, BUTTON_HEIGHT)
        if current_index < len(body_classes) - 1:
            draw_button("Next ->", WIDTH - 150, HEIGHT - 60, BUTTON_WIDTH, BUTTON_HEIGHT)

        draw_button("Select", WIDTH//2 - 50, HEIGHT - 60, BUTTON_WIDTH, BUTTON_HEIGHT,color=(255, 255, 0))

        txt = font.render(f"Body Type: {body_names[current_index]}", True, BLACK)
        screen.blit(txt, (450, 20))
        
        pos_text = font.render(f"Character Position: ({CHARACTER_OFFSET_X}, {CHARACTER_OFFSET_Y})", True, BLACK)
        screen.blit(pos_text, (450, 45))

        pygame.display.update()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if 50 <= mx <= 50 + BUTTON_WIDTH and HEIGHT - 60 <= my <= HEIGHT - 20:
                    if current_index > 0:
                        current_index -= 1

                elif WIDTH - 150 <= mx <= WIDTH - 50 and HEIGHT - 60 <= my <= HEIGHT - 20:
                    if current_index < len(body_classes) - 1:
                        current_index += 1

                elif WIDTH//2 - 50 <= mx <= WIDTH//2 + 50 and HEIGHT - 60 <= my <= HEIGHT - 20:
                    if body_classes[current_index] == MonsterBody:
                        gender = "monster"
                    else:
                        gender = "female" if body_classes[current_index] == FemaleBody else "male"
                    return body_classes[current_index], gender

def select_model_with_preview(BodyFactory, gender, models, title, current_selections):
    current_index = 0
    selected_color = COLOR_PALETTE[0]
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)

        character_surface = pygame.Surface((CHARACTER_DISPLAY_WIDTH, CHARACTER_DISPLAY_HEIGHT), pygame.SRCALPHA)
        character = BodyFactory(character_surface)
        character.draw()
        screen.blit(character_surface, (CHARACTER_OFFSET_X, CHARACTER_OFFSET_Y))

        if current_selections.get('shirt'):
            adjusted_shirt = adjust_style_coordinates(current_selections['shirt']['original_model'])
            draw_polygons_with_color(screen, adjusted_shirt, current_selections['shirt']['color'])

        if current_selections.get('hair'):
            adjusted_hair = adjust_style_coordinates(current_selections['hair']['original_model'])
            draw_polygons_with_color(screen, adjusted_hair, current_selections['hair']['color'])

        if current_selections.get('tail'):
            adjusted_tail = adjust_style_coordinates(current_selections['tail']['original_model'])
            draw_polygons_with_color(screen, adjusted_tail, current_selections['tail']['color'])

        if current_selections.get('pants'):
            adjusted_pants = adjust_style_coordinates(current_selections['pants']['original_model'])
            draw_polygons_with_color(screen, adjusted_pants, current_selections['pants']['color'])

        if current_selections.get('sucks'):
            adjusted_sucks = adjust_style_coordinates(current_selections['sucks']['original_model'])
            draw_polygons_with_color(screen, adjusted_sucks, current_selections['sucks']['color'])

        if current_selections.get('shoes'):
            adjusted_shoes = adjust_style_coordinates(current_selections['shoes']['original_model'])
            draw_polygons_with_color(screen, adjusted_shoes, current_selections['shoes']['color'])

        if current_selections.get('wings'):
            adjusted_wings = adjust_style_coordinates(current_selections['wings']['original_model'])
            draw_polygons_with_color(screen, adjusted_wings, current_selections['wings']['color'])

        if current_selections.get('eye'):
            adjusted_eye = adjust_style_coordinates(current_selections['eye']['original_model'])
            draw_polygons_with_color(screen, adjusted_eye, current_selections['eye']['color'])

        if current_selections.get('horn'):
            adjusted_horns = adjust_style_coordinates(current_selections['horn']['original_model'])
            draw_polygons_with_color(screen, adjusted_horns, current_selections['horn']['color'])

        if current_selections.get('gun'):
            adjusted_gun = adjust_style_coordinates(current_selections['gun']['original_model'])
            draw_polygons_with_color(screen, adjusted_gun, current_selections['gun']['color'])

        if current_index < len(models):
            adjusted_current = adjust_style_coordinates(models[current_index])
            draw_polygons_with_color(screen, adjusted_current, selected_color)
                
        color_rects = draw_color_palette(450, 55, selected_color)
        
        title_text = font.render(f"Choose {title}", True, BLACK)
        screen.blit(title_text, (450, 20))
        
        if models:
            style_info = font.render(f"Style {current_index} of {len(models)-1}", True, BLACK)
            screen.blit(style_info, (450, 390))
        
        prev_btn = None
        next_btn = None
        select_btn = None
        skip_btn = None
        
        if current_index > 0:
            prev_btn = draw_button("<- Prev Style", 450, HEIGHT - 120, 120, BUTTON_HEIGHT)
        if current_index < len(models) - 1:
            next_btn = draw_button("Next Style ->", 580, HEIGHT - 120, 120, BUTTON_HEIGHT)
        
        select_btn = draw_button("Select", 450, HEIGHT - 70, BUTTON_WIDTH, BUTTON_HEIGHT,color=(255, 255, 0))
        skip_btn = draw_button("Reset", 565, 11, BUTTON_WIDTH, BUTTON_HEIGHT,color=(255,0,0))

        pygame.display.update()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                
                for rect, color in color_rects:
                    if rect.collidepoint(mx, my):
                        selected_color = color
                        break
                
                if prev_btn and prev_btn.collidepoint(mx, my):
                    if current_index > 0:
                        current_index -= 1
                
                elif next_btn and next_btn.collidepoint(mx, my):
                    if current_index < len(models) - 1:
                        current_index += 1
                
                elif select_btn and select_btn.collidepoint(mx, my):
                    if models and current_index < len(models):
                        return {
                            'original_model': models[current_index],
                            'color': selected_color
                        }
                    return None
                
                elif skip_btn and skip_btn.collidepoint(mx, my):
                    raise ResetException
def show_final_character(BodyFactory, selections, background_color):
    win = pygame.display.set_mode((500, 500))
    surface = pygame.Surface((500, 500))
    pygame.display.set_caption("Your Final Character")
    
    character = BodyFactory(surface)
    clock = pygame.time.Clock()

    while True:
        surface.fill(background_color)
        character.draw()

        if selections.get('shirt'):
            draw_polygons_with_color(surface, selections['shirt']['original_model'], 
                                     selections['shirt']['color'])
        if selections.get('hair'):
            draw_polygons_with_color(surface, selections['hair']['original_model'], 
                                     selections['hair']['color'])
        if selections.get('tail'):
            draw_polygons_with_color(surface, selections['tail']['original_model'], 
                                     selections['tail']['color'])
        if selections.get('pants'):
            draw_polygons_with_color(surface, selections['pants']['original_model'], 
                                     selections['pants']['color'])
        if selections.get('sucks'):
            draw_polygons_with_color(surface, selections['sucks']['original_model'], 
                                     selections['sucks']['color'])
        if selections.get('shoes'):
            draw_polygons_with_color(surface, selections['shoes']['original_model'], 
                                     selections['shoes']['color'])
        if selections.get('wings'):
            draw_polygons_with_color(surface, selections['wings']['original_model'],
                                     selections['wings']['color'])
        if selections.get('eye'):
            draw_polygons_with_color(surface, selections['eye']['original_model'], 
                                     selections['eye']['color'])
            
        if selections.get('horn'):
            draw_polygons_with_color(surface, selections['horn']['original_model'],
                                     selections['horn']['color'])
            
        if selections.get('gun'):
            draw_polygons_with_color(surface, selections['gun']['original_model'],
                                     selections['gun']['color'])


        win.blit(surface, (0, 0))
        
        save_button = draw_button("Save", 200, 450, BUTTON_WIDTH, BUTTON_HEIGHT, color=(0, 255, 0))
        reset_button = draw_button("Reset", 350, 450, BUTTON_WIDTH, BUTTON_HEIGHT, color=(255, 0, 0))

        pygame.display.update()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                
                if save_button.collidepoint(mx, my):
                    pygame.image.save(surface, f"screen/final_character{ time.time()}.png")
                    print("Character saved as 'final_character.png'")
                
                elif reset_button.collidepoint(mx, my):
                    raise ResetException


class ResetException(Exception):
    pass

def main():
    while True: 
        music.play()
        try:
            base_class, gender = select_base_body()
            skin_color = select_skin_color()  
            selections = {}

            def body_factory(surface):
                return base_class(surface, skin_color=skin_color)
            
            shirt_models = load_models(gender, "shirt")
            if shirt_models:
                selected_shirt = select_model_with_preview(body_factory, gender, shirt_models, "Shirt", selections)
                if selected_shirt:
                    selections['shirt'] = selected_shirt

            hair_models = load_models(gender, "hair")
            if hair_models:
                selected_hair = select_model_with_preview(body_factory, gender, hair_models, "Hair", selections)
                if selected_hair:
                    selections['hair'] = selected_hair
            
            tail_models = load_models(gender, "tail")
            if tail_models:
                selected_tail = select_model_with_preview(body_factory, gender, tail_models, "Tail", selections)
                if selected_tail:
                    selections['tail'] = selected_tail

            pants_models = load_models(gender, "pants")
            if pants_models:
                selected_pants = select_model_with_preview(body_factory, gender, pants_models, "Pants", selections)
                if selected_pants:
                    selections['pants'] = selected_pants

            sucks_models = load_models(gender, "sucks")
            if sucks_models:
                selected_sucks = select_model_with_preview(body_factory, gender, sucks_models, "Sucks", selections)
                if selected_sucks:
                    selections['sucks'] = selected_sucks

            shoes_models = load_models(gender, "shoes")
            if shoes_models:
                selected_shoes = select_model_with_preview(body_factory, gender, shoes_models, "Shoes", selections)
                if selected_shoes:
                    selections['shoes'] = selected_shoes

            wings_models = load_models(gender, "wings")
            if wings_models:
                selected_wings = select_model_with_preview(body_factory, gender, wings_models, "Wings", selections)
                if selected_wings:
                    selections['wings'] = selected_wings

            eye_models = load_models(gender, "eye")
            if eye_models:
                selected_eye = select_model_with_preview(body_factory, gender, eye_models, "Eye", selections)
                if selected_eye:
                    selections['eye'] = selected_eye
            
            horn_models = load_models(gender, "horn")
            if horn_models:
                selected_horn = select_model_with_preview(body_factory, gender, horn_models, "Horn", selections)
                if selected_horn:
                    selections['horn'] = selected_horn

            gun_models = load_models(gender, "gun")
            if gun_models:
                selected_gun = select_model_with_preview(body_factory, gender, gun_models, "Gun", selections)
                if selected_gun:
                    selections['gun'] = selected_gun

            background_color = select_background_color(body_factory, selections)
            
            show_final_character(body_factory, selections, background_color)
            break
            
        except ResetException:
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Choose Character")
            continue


if __name__ == "__main__":
    main()
