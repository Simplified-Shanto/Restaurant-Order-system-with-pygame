import os
import pygame, sys
from random import randint

# Let's see whether this change is updated in github automatically. 

screen = pygame.display.set_mode((800, 400))
pygame.init()
os.chdir(r"D:\[03] Codes\[08] Python codes\[01] Pygame projects\[01] Restaurant App Project")
pygame.display.set_caption('Neverland Restaurant') #The title of the pygame window
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)



'''
Available food items: 
1. Water
2. Soda
3. Salad
4. Fried_Chicken
5. Rice
6. Vegetable
7. Chicken 
8. Mutton
'''

class Button:
    def __init__(self, text, width, height, pos, border_radius):
        # core attributes
        self.pressed = False
        self.elevation = 6
        self.active_elevation = self.elevation
        self.original_y_pos = pos[1]

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, self.elevation))
        self.bottom_color = '#354B5E'
        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        # text
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect =  self.text_surf.get_rect(center = self.top_rect.center)
        self.border_radius = border_radius
    def draw(self):
        # elevation  logic
        self.top_rect.y = self.original_y_pos - self.active_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop 
        self.bottom_rect.height = self.top_rect.height + self.active_elevation
        
        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius= self.border_radius)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius= self.border_radius)
       
        screen.blit(self.text_surf, self.text_rect)
        #self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        result = 0
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if  pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
                    self.pressed = True
                    self.active_elevation = 0
                    

            else:
                   if self.pressed == True:
                        self.pressed = False
                        self.active_elevation = self.elevation
                        return 1
                        
        else:
             self.top_color = '#475F77'
             self.active_elevation = self.elevation
             result = 0
        return 0
    
# This dictionary stores all the placed orders
order_dict = {

}

class food_item():
    def __init__(self, x_pos, y_pos, name, available_quantity):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = name
        self.available_quantity = available_quantity
        self.ordered_quantity = 0
        self.decrement_button = Button('-',25, 20, (x_pos + 69, y_pos +155 ), 3 )
        self.increment_button = Button('+',25, 20, (x_pos + 5, y_pos+155), 3 )

        match self.name:
            case 'Fish':
                self.image = pygame.image.load('graphics/fish.jpg').convert_alpha()
                self.image = pygame.transform.rotozoom(self.image, 0, 0.225)
                self.price = 15
            case 'Salad':
                self.image = pygame.image.load('graphics/salad.png').convert_alpha()
                self.image = pygame.transform.rotozoom(self.image, 0, 0.13)
                self.price = 5
            case 'Rice':
                self.image = pygame.image.load('graphics/rice.png').convert_alpha()
                self.image = pygame.transform.rotozoom(self.image, 0, 0.13)
                self.price = 6
            case 'Water':
                self.image = pygame.image.load('graphics/water.png').convert_alpha()
                self.image = pygame.transform.rotozoom(self.image, 0, 0.22)
                self.price = 2
            case 'Soda':
                self.image = pygame.image.load('graphics/soda.jpg').convert_alpha()
                self.image = pygame.transform.rotozoom(self.image, 0, 0.13)
                self.price = 6
            
            case 'Bread':
                self.image = pygame.image.load('graphics/bread.jpg').convert_alpha()
                self.image = pygame.transform.rotozoom(self.image, 0, 0.13)
                self.price = 6
            case 'Mutton':
                self.image = pygame.image.load('graphics/mutton.jpg').convert_alpha()
                self.image = pygame.transform.rotozoom(self.image, 0, 0.08)
                self.price = 20
            
            case 'Chicken':
                self.image = pygame.image.load('graphics/chicken.png').convert_alpha()
                self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
                self.price = 18


    def draw_food_tile(self):
        pygame.draw.rect(screen, '#00b2c3', (self.x_pos, self.y_pos, 100, 180), border_radius= 4)
        pygame.draw.rect(screen, (255, 255, 255), (self.x_pos + 35, self.y_pos + 148, 30, 25) ,border_radius = 3)
        screen.blit(self.image, (self.x_pos + 10, self.y_pos + 10))
        font = pygame.font.SysFont("comicsansms", 15)
        text = font.render(f"{self.name} : ${self.price}", True, (0, 0, 0))
        text_rect = text.get_rect(midbottom = (self.x_pos + 50, self.y_pos + 115))
        screen.blit(text, text_rect)

        # Ordered quantity text

        text = font.render(f"{self.ordered_quantity}", True, (0, 0, 0))
        text_rect = text.get_rect(center = (self.x_pos + 35 + 15, self.y_pos + 148 + 12))
        screen.blit(text, text_rect)

        self.increment_button.draw()
        self.decrement_button.draw()
        self.ordered_quantity += self.increment_button.check_click()


        self.ordered_quantity -= self.decrement_button.check_click()
        self.ordered_quantity = max(self.ordered_quantity, 0)

        order_dict[(self.name, self.price)] = self.ordered_quantity
        
fish = food_item(10, 10,'Fish', 10)






bg_surf = pygame.image.load('graphics/background.jpeg').convert()
bg_surf = pygame.transform.rotozoom(bg_surf, 0, 0.8)


item_name_list = ['Fish', 'Mutton','Chicken', 'Rice', 'Salad', 'Water', 'Bread', 'Soda']
item_list = []
item_x = 10
item_y = 10
for x in item_name_list:
    item_list.append(food_item(item_x, item_y, x, randint(5, 20)))
    item_x+=110
    if(x == 'Rice'):
        item_y = 210
        item_x = 10




order_confirm_button = Button('Confirm Order',200, 30, (540 , 350 ), 5 )
order_again_button = Button('Order Again',200, 30, (290 , 250 ), 5 )

order_confirmed = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surf, (0, 0))
    
    for x in item_list:
        x.draw_food_tile()


    # Order details
    pygame.draw.rect(screen, 'khaki2', (500, 10, 280, 380), border_radius = 5)
    
    font = pygame.font.Font(None, 30)
    text = font.render("Your order: ", True, (0, 0, 0))
    text_rect = text.get_rect(topleft = (520, 40))
    screen.blit(text, text_rect)

    font = pygame.font.Font(None, 20)
    text = font.render("Item    Quantity   Unit Price   Subtotal", True, (0, 0, 0))
    text_rect = text.get_rect(topleft = (520, 80))
    screen.blit(text, text_rect)

    pygame.draw.line(screen, 'Black', (530, 300), (750, 300), 2)

    order_confirm_button.draw()
    if order_confirm_button.check_click():
        order_confirmed = True

 
    
    total_price = 0
    list_y = 100
    for x in order_dict:
        if order_dict[x]:
            text = text = font.render(f"{x[0]}         {order_dict[x]}                ${x[1]}              ${order_dict[x]*x[1]}", True, (0, 0, 0))
            total_price+=order_dict[x]*x[1]
            text_rect = text.get_rect(topleft = (520, list_y))
            list_y+=20
            screen.blit(text, text_rect)

    font = pygame.font.Font(None, 30)
    text = font.render(f"Total = ${total_price}", True, (0, 0, 0))
    text_rect = text.get_rect(topright = (680, 310))
    screen.blit(text, text_rect)
    
    if order_confirmed:
        pygame.draw.rect(screen, 'yellowgreen', (100, 50, 600, 300), border_radius = 20)
        font = pygame.font.Font(None, 60)
        text = font.render("Thank you for your order:)", True, (0, 255, 0))
        text_rect = text.get_rect(center = (400, 150))
        screen.blit(text, text_rect)

        # Re order mechanism
        order_again_button.draw()
        if order_again_button.check_click():
            for x in item_list:
                x.ordered_quantity = 0
            for x in order_dict:
                order_dict[x] = 0
            order_confirmed = False
            

        
        
    pygame.display.update()
    clock.tick(60)
