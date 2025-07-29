import pygame
import random

# Initialize pygame
pygame.init()

# Get the screen resolution
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Create a full-screen window
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)

# Function to draw random squares at random positions
def draw_random_square():
    size = random.randint(20, 100)  # Random square size
    x = random.randint(0, screen_width - size)
    y = random.randint(0, screen_height - size)
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )  # Random RGB color

    # Draw the square
    pygame.draw.rect(screen, color, (x, y, size, size))

# Initialize the screen with a black background
screen.fill((0, 0, 0))

# Update the screen immediately
pygame.display.flip()

# Set the running flag
running = True

# Loop that draws squares as fast as possible without clearing the screen
while running:
    # Draw a new square at a random position
    draw_random_square()

    # Update the display
    pygame.display.flip()

    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame when done
pygame.quit()
