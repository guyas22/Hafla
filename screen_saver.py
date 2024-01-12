import pygame
import sys
import os
import random

# Initialize Pygame
pygame.init()

# Get screen dimensions
info = pygame.display.Info()
width, height = info.current_w, info.current_h

# Set up the display in fullscreen mode
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("DVD Screensaver")

# Load your custom logo
logo_path = 'idan_logo.png'  # Replace with your image file path
if not os.path.exists(logo_path):
    raise ValueError("The specified logo file does not exist")

original_logo = pygame.image.load(logo_path)

# Resize the logo to 50% of its original size
logo_size = original_logo.get_size()
resized_logo = pygame.transform.scale(original_logo, (logo_size[0] // 2, logo_size[1] // 2))

logo = resized_logo.copy()  # Copy of the resized logo for initial display
logo_rect = logo.get_rect()

# Set initial position of the logo to the center of the screen
logo_rect.x = (width - logo_rect.width) // 2
logo_rect.y = (height - logo_rect.height) // 2

# Speed and direction
speed = [2, 2]

# Function to change the color of the logo
def change_color(image, last_color, colors):
    new_color = random.choice(colors)
    while new_color == last_color:  # Ensure different color is chosen
        new_color = random.choice(colors)
    colored_logo = image.copy()
    tint = pygame.Surface(image.get_size(), pygame.SRCALPHA)
    tint.fill(new_color)
    colored_logo.blit(tint, (0, 0), special_flags=pygame.BLEND_ADD)
    return colored_logo, new_color

# Color list for changing logo colors
colors = [(255, 0, 0, 50), (0, 255, 0, 50), (0, 0, 255, 50), (255, 255, 0, 50), (255, 0, 255, 50), (0, 0, 0, 0)]  # Added Magenta and Cyan

last_color = None  # Keep track of the last color

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key is pygame.K_ESCAPE):
            running = False

    # Move the image
    logo_rect = logo_rect.move(speed)

    # Bounce off the edges and change logo color
    if logo_rect.left < 0 or logo_rect.right > width:
        speed[0] = -speed[0]
        logo, last_color = change_color(resized_logo, last_color, colors)
    if logo_rect.top < 0 or logo_rect.bottom > height:
        speed[1] = -speed[1]
        logo, last_color = change_color(resized_logo, last_color, colors)

    # Fill the screen and blit the image
    screen.fill((0, 0, 0))
    screen.blit(logo, logo_rect)

    # Update the display
    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
