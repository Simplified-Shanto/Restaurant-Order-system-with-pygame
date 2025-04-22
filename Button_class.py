import pygame, sys
counter = 0
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
                        print("click") 
                        self.pressed = False
                        self.active_elevation = self.elevation
                        return 1
                        
        else:
             self.top_color = '#475F77'
             self.active_elevation = self.elevation
             result = 0
        return 0
             
                    

            

        





pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)


button1 = Button('Click',100, 40, (200, 250), 10 )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('#DCDDD8')
    button1.draw()

    counter+= button1.check_click()
    print(counter)

    pygame.display.update()
    clock.tick(60)