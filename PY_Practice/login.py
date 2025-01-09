# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up display
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Simple Pygame Example')

# # Colors
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)

# # Set up rectangle
# rect_width, rect_height = 50, 50
# rect_x, rect_y = (width - rect_width) // 2, (height - rect_height) // 2
# rect_speed = 5

# # Main game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and rect_x > 0:
#         rect_x -= rect_speed
#     if keys[pygame.K_RIGHT] and rect_x < width - rect_width:
#         rect_x += rect_speed
#     if keys[pygame.K_UP] and rect_y > 0:
#         rect_y -= rect_speed
#     if keys[pygame.K_DOWN] and rect_y < height - rect_height:
#         rect_y += rect_speed

#     # Draw background
#     screen.fill(white)

#     # Draw rectangle
#     pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))

#     # Update display
#     pygame.display.flip()

#     # Cap the frame rate
#     pygame.time.Clock().tick(60)

import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    # You can replace the condition with your actual login validation logic
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Interface")

# Create labels
label_username = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")

# Create entry widgets
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

# Create login button
login_button = tk.Button(root, text="Login", command=validate_login)

# Set up layout using grid
label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
entry_username.grid(row=0, column=1, padx=10, pady=10)
label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
entry_password.grid(row=1, column=1, padx=10, pady=10)
login_button.grid(row=2, column=1, pady=20)

# Run the Tkinter event loop
root.mainloop()