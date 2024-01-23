import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sand Simulation")

# Colors
SAND_COLOR = (237, 201, 175)  # A sand-like color
VOID_COLOR = (0, 0, 0)  # Black background

# Sand particles list
sand_particles = []

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add a new sand particle at a random position at the top
    sand_particles.append([random.randint(0, WIDTH), 0])

    # Update sand particles
    for particle in sand_particles:
        particle[1] += 1  # Move down due to gravity
        if particle[1] >= HEIGHT:
            sand_particles.remove(particle)  # Remove particle if it reaches the bottom

    # Drawing
    screen.fill(VOID_COLOR)
    for particle in sand_particles:
        pygame.draw.circle(screen, SAND_COLOR, particle, 2)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
