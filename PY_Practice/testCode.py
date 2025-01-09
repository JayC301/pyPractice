import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Menu Example')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Set up font
font = pygame.font.Font(None, 36)

# Define menu items
menu_items = ["Start Game", "Options", "Exit"]
selected_item = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item = (selected_item - 1) % len(menu_items)
            elif event.key == pygame.K_DOWN:
                selected_item = (selected_item + 1) % len(menu_items)
            elif event.key == pygame.K_RETURN:
                # Execute the selected menu item
                if menu_items[selected_item] == "Start Game":
                    print("Starting the game!")
                    # Add your game logic here
                elif menu_items[selected_item] == "Options":
                    print("Opening options menu!")
                    # Add your options menu logic here
                elif menu_items[selected_item] == "Exit":
                    pygame.quit()
                    sys.exit()

    # Draw background
    screen.fill(white)

    # Draw menu items
    for i, item in enumerate(menu_items):
        color = green if i == selected_item else black
        text_surface = font.render(item, True, color)
        text_rect = text_surface.get_rect(center=(width // 2, height // 2 + i * 40))
        screen.blit(text_surface, text_rect)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)