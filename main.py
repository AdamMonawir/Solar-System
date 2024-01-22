import pygame
import math

pygame.init()

#Window Properties
WIDTH, HEIGHT = (800, 800)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

#Colours
WHITE = (255, 255, 255)
ORANGE = (255, 204, 0)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

#Fonts
FONT = pygame.font.SysFont("comicsans", 16)


#Planet definitions
class Planet:
  AU = (149.6e6 * 1000)
  G = (6.67428e-11)
  SCALE = 75 / AU  # 1AU = 100pixels if 250
  TIMESTEP = 3600 * 24  # 1 day

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

  #Draw the planets and orbits and distances
  def draw(self, win):
    # Inital Position
    x = self.x * self.SCALE + WIDTH / 2
    y = self.y * self.SCALE + HEIGHT / 2

    #Orbits
    if len(self.orbit) > 2:
      updated_points = []
      for point in self.orbit:
        x, y = point
        x = x * self.SCALE + WIDTH / 2
        y = y * self.SCALE + HEIGHT / 2
        updated_points.append((x, y))
      pygame.draw.lines(win, self.colour, False, updated_points, 2)

    #Planet
    pygame.draw.circle(win, self.colour, (x, y), self.radius)

    #Distances
    if not self.sun:
      distance_text = FONT.render(f"{round(self.distance_to_sun / 1000, 1)}km", 1, WHITE)
      win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))

  #Calculating attraction
  def attraction(self, other):
    other_x, other_y = other.x, other.y
    distance_x = other_x - self.x
    distance_y = other_y - self.y
    distance = math.sqrt(distance_x**2 + distance_y**2)

    #checking if sun
    if other.sun:
      self.distance_to_sun = distance

    #Calculating forces
    force = self.G * self.mass * other.mass / distance**2
    theta = math.atan2(distance_y, distance_x)
    force_x = math.cos(theta) * force
    force_y = math.sin(theta) * force
    return force_x, force_y

  #Calculating and moving by velocity
  def update_position(self, planets):
    total_fx = total_fy = 0
    for planet in planets:
      if self == planet:
        continue

      #force calculation
      fx, fy = self.attraction(planet)
      total_fx += fx
      total_fy += fy

    #Velocity calculation
    self.x_vel += total_fx / self.mass * self.TIMESTEP
    self.y_vel += total_fy / self.mass * self.TIMESTEP

    #Placement Calculations
    self.x += self.x_vel * self.TIMESTEP
    self.y += self.y_vel * self.TIMESTEP
    self.orbit.append((self.x, self.y))


#Opens Window
def main():
  run = True
  #to be defined for loop
  clock = pygame.time.Clock()

  #Making Planets
  sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
  sun.sun = True
  mercury = Planet(-0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
  mercury.y_vel = 47.4 * 1000
  venus = Planet(-0.723 * Planet.AU, 0, 14, ORANGE, 4.8685 * 10**24)
  venus.y_vel = 35.02 * 1000
  earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
  earth.y_vel = 29.783 * 1000
  earth.x_vel = 0 * 1000
  moon = Planet(-1.002593 * Planet.AU, 0, 4, WHITE, 4 * 10**22)
  moon.y_vel = 29.022 * 1000 # 1.022 * 1000 earth is zero
  moon.x_vel = 0 * 1000
  mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
  mars.y_vel = 24.077 * 1000
  jupiter = Planet(-5.203 * Planet.AU, 0, 20, DARK_GREY, 1.898 * 10**27)
  jupiter.y_vel = 13.07 * 1000

  #planets to be drawn
  planets = [sun, mercury, venus, earth, mars, jupiter]

  while run:
    #updates per second
    clock.tick(60)
    WIN.fill((0, 0, 0))

    #Will close when x is pressed
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    #Will draw planets
    for planet in planets:
      planet.update_position(planets)
      planet.draw(WIN)

    pygame.display.update()
  pygame.quit()


main()
