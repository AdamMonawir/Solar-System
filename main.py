import pygame 
import math
pygame.init()

#Window Properties
WIDTH, HEIGHT = (800, 800)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")
#Colours
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#Planet definitions
class Planet:
    AU = (149.6e6 * 1000)
    G = (6.67428e-11)
    SCALE = 250 / AU  # 1AU = 100pixels
    TIMESTEP = 3600 * 24 # 1 day

    #Variables for each planet
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

    #Draw the planets
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.colour, (x, y), self.radius)

#Opens Window
def main():
    run = True
    #to be defined for loop
    clock = pygame.time.Clock()

    #Making Planets
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    #planets to be drawn
    planets = [sun]

    while run:
        #updates per second
        clock.tick(60)
        #WIN.fill(WHITE)

        #Will close when x is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #Will draw planets
        for planet in planets:
            planet.draw(WIN)
        
        pygame.display.update()
    pygame.quit()
main()