import pygame 
import math
pygame.init()

#Window Properties
WIDTH, HEIGHT = (800, 800)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")
WHITE = (255, 255, 255)

#Planet definitions
class Planet:
    AU = (149.6e6 * 1000)
    G = (6.67428e-11)
    SCALE = 250 / AU  # 1AU = 100pixels
    TIMESTEP = 3600 * 24 # 1 day

    def __init__(self, x, y, radius, colour, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

#Opens Window
def main():
    run = True
    #to be defined for loop
    clock = pygame.time.Clock()

    while run:
        #updates per second
        clock.tick(60)
        #WIN.fill(WHITE)
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
main()