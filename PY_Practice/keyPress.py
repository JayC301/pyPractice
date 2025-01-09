# import tkinter as tk

# def on_key_press(event):
#     if event.char.lower() == 'w':
#         print("Yes")

# # Create the main window
# root = tk.Tk()
# root.title("KeyPress Example")

# # Bind the on_key_press function to the key press event
# root.bind("<Key>", on_key_press)

# # Run the Tkinter event loop
# root.mainloop()

# ------------------------------------------------------------------------------------
# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up display
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Pygame KeyPress Example')

# # Colors
# white = (255, 255, 255)

# # Set up font
# font = pygame.font.Font(None, 36)

# # Main game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#         # Check for key press event
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_w:
#                 print("Pygame Yes")

#     # Draw background
#     screen.fill(white)

#     # Update display
#     pygame.display.flip()

#     # Cap the frame rate
#     pygame.time.Clock().tick(60)


import msvcrt

print("Press any key to continue...")
msvcrt.getch()
print("Continuing...")
