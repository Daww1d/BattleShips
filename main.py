import pygame

pygame.init()

# CONSTANTS

WIDTH = 1200
HEIGHT = 800
FPS = 60


# CLASSES
class UI:
    def __init__(self):
        self.mainMenu = False

    def drawMenu(self):
        pygame.draw.rect(screen, "black", [100, 100, 300, 300], 0, 5)

    def drawMain(self):
        menuBtn = pygame.draw.rect(screen, "grey", [495, 10, 210, 50], 0, 5)
        pygame.draw.rect(screen, "dark grey", [495, 10, 210, 50], 5, 5)
        text = font.render("Main Menu", True, "white")
        screen.blit(text, (510, 20))
        if menuBtn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            UI.mainMenu = True
        else:
            UI.mainMenu = False
        return UI.mainMenu

class Button:
    pass


screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Menu")
timer = pygame.time.Clock()
font = pygame.font.Font("assets\mainFont.TTF", 24)


run = True

UI = UI()
# GAME LOOP

while run:
    screen.fill("light blue")
    timer.tick(FPS)
    if UI.mainMenu:
        UI.drawMenu()
    else:
        UI.mainMenu = UI.drawMain()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
