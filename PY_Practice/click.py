import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Clickable Button Example')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Set up font
font = pygame.font.Font(None, 36)

# Button properties
button_rect = pygame.Rect(300, 200, 200, 50)
button_text = "Click Me!"

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Button Clicked!")

    # Draw background
    screen.fill(white)

    # Draw button
    pygame.draw.rect(screen, green, button_rect)

    # Render button text
    text_surface = font.render(button_text, True, black)
    text_rect = text_surface.get_rect(center=button_rect.center)
    
    # Draw text
    screen.blit(text_surface, text_rect)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)