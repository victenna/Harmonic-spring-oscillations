import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the drawing window
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
grey = (200, 200, 200)

# Variables
t = 0
spring_positions = [250, 400, 550]  # X positions for the three springs
num_springs = len(spring_positions)

# Different speeds for each spring
spring_speeds = [1, 2, 3]  # You can adjust these values for different speeds

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(grey)

    # Draw the horizontal plate
    pygame.draw.line(screen, black, (200, 50), (650, 50), 20)

    # Calculate vertical oscillation for each spring
    for i in range(num_springs):
        delta = 40 * math.sin(math.radians(t * spring_speeds[i]))  # Different speed for each spring
        delta1 = math.sin(math.radians(t * spring_speeds[i]))  # Different speed for each spring

        # Draw the spring
        spring_x = spring_positions[i]
        pygame.draw.rect(screen, black, (spring_x - 20, 300 * (1 - delta1) + 42, 40, 60))

        # Draw the spring coils
        for j in range(10):
            pygame.draw.ellipse(screen, black, pygame.Rect(spring_x - 20, j * 30 * (1 - delta1) + 50, 40, 40 - delta), 5)

    t += 5  # Increment time

    # Update the display
    pygame.display.flip()
    clock.tick(30)  # Frame rate limit

# Quit Pygame
pygame.quit()
sys.exit()