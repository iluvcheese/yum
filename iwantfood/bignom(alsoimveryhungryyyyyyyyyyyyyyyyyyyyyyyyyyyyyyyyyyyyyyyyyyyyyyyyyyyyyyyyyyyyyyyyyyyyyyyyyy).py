import pygame
import random
pygame.init()

screen = pygame.display.set_mode([500, 500])

playing = True

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

class Hamburger():
    def __init__(self, color, pos, rad, wid=0):
        self.c = color
        self.p = pos
        self.r = rad
        self.w = wid
        self.s = screen
    def yum(self):
        pygame.draw.circle(self.s, self.c, self.p, self.r, self.w)
    def eatotherhamburgersolikehamburgereatdahamburgerbuthamburgerhasnomouthsolikeidkhowhamburgereatotherhamburgerbutlikeyethehamburgeratethehamburgerandnowthisistheeendjkitisntcuzthisistheend(self):
        self.r+=1
        pygame.draw.circle(self.s, self.c, self.p, self.r, self.w)

hamburger1 = Hamburger((r,g,b), (250, 250), 1, 0.5)



while playing:
    for piecesofpepperoni in pygame.event.get():
        if piecesofpepperoni.type == pygame.QUIT:
            playing = False
            pygame.quit()
        if piecesofpepperoni.type == pygame.MOUSEBUTTONDOWN:
            hamburger1.yum()
            pygame.display.update()
        if piecesofpepperoni.type == pygame.MOUSEBUTTONUP:
            hamburger1.eatotherhamburgersolikehamburgereatdahamburgerbuthamburgerhasnomouthsolikeidkhowhamburgereatotherhamburgerbutlikeyethehamburgeratethehamburgerandnowthisistheeendjkitisntcuzthisistheend()
            pygame.display.update()
