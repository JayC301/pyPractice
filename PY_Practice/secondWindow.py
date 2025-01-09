# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up main display
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Main Window')

# # Colors
# white = (255, 255, 255)
# black = (0, 0, 0)
# green = (0, 255, 0)
# red = (255, 0, 0)

# # Set up font
# font = pygame.font.Font(None, 36)

# # Button properties for the main window
# button_rect = pygame.Rect(300, 200, 200, 50)
# button_text = "Open Jump-out Window"

# # Set up the jump-out window
# jump_out_width, jump_out_height = 400, 300
# jump_out_screen = pygame.display.set_mode((jump_out_width, jump_out_height))
# pygame.display.set_caption('Jump-out Window')

# # Button properties for the jump-out window
# jump_out_button_rect = pygame.Rect(150, 100, 200, 50)
# jump_out_button_text = "Close"

# # Main game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#         # Check for mouse click on the main window button
#         if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
#             print("Opening Jump-out Window")

#             # Show the jump-out window
#             jump_out_running = True
#             while jump_out_running:
#                 for jump_out_event in pygame.event.get():
#                     if jump_out_event.type == pygame.QUIT:
#                         jump_out_running = False

#                     # Check for mouse click on the jump-out window button
#                     if (
#                         jump_out_event.type == pygame.MOUSEBUTTONDOWN
#                         and jump_out_button_rect.collidepoint(jump_out_event.pos)
#                     ):
#                         print("Closing Jump-out Window")
#                         jump_out_running = False

#                 # Draw jump-out window background
#                 jump_out_screen.fill(white)

#                 # Draw jump-out window button
#                 pygame.draw.rect(jump_out_screen, red, jump_out_button_rect)

#                 # Render jump-out window button text
#                 text_surface = font.render(jump_out_button_text, True, black)
#                 text_rect = text_surface.get_rect(center=jump_out_button_rect.center)
#                 jump_out_screen.blit(text_surface, text_rect)

#                 # Update jump-out window display
#                 pygame.display.flip()

#                 # Cap the frame rate
#                 pygame.time.Clock().tick(60)

#     # Draw main window background
#     screen.fill(white)

#     # Draw main window button
#     pygame.draw.rect(screen, green, button_rect)

#     # Render main window button text
#     text_surface = font.render(button_text, True, black)
#     text_rect = text_surface.get_rect(center=button_rect.center)
#     screen.blit(text_surface, text_rect)

#     # Update main window display
#     pygame.display.flip()

#     # Cap the frame rate
#     pygame.time.Clock().tick(60)


# -------------------------------------------------second tkinter window from pygame button
import pygame
import tkinter as tk
from tkinter import messagebox

# Initialize Pygame
pygame.init()

# Set up Pygame display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame and Tkinter Example')

# Colors
white = (255, 255, 255)
green = (0, 255, 0)

# Set up font
font = pygame.font.Font(None, 36)

# Button properties
button_rect = pygame.Rect(300, 200, 200, 50)
button_text = "Open Tkinter Window"

# Function to open Tkinter window
def open_tkinter_window():
    tkinter_window = tk.Tk()
    tkinter_window.title("Tkinter Window")
    tkinter_window.geometry("500x1000")
    label = tk.Label(tkinter_window, text="Hello from Tkinter!")
    label.pack(padx=20, pady=20)
    tkinter_window.mainloop()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Check for mouse click on the Pygame button
        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            open_tkinter_window()

    # Draw background
    screen.fill(white)

    # Draw Pygame button
    pygame.draw.rect(screen, green, button_rect)

    # Render Pygame button text
    text_surface = font.render(button_text, True, white)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    # Update Pygame display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
        # Handle Tkinter events
