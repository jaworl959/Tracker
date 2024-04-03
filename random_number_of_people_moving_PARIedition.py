#ASLIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# random number of people moving  
import pygame 
import sys 
import random 
 
# Initialize pygame 
pygame.init() 

# Load the image 
image = pygame.image.load("/home/asus/project/opal_edition2.png") 
original_width, original_height = image.get_size() 
resized_width, resized_height = original_width // 3 * 2, original_height // 3 * 2 
image = pygame.transform.scale(image, (resized_width, resized_height)) 
 
# Set up the screen 
screen = pygame.display.set_mode((resized_width, resized_height)) 
pygame.display.set_caption("Move the Square") 
 
# Set up the colors 
RED = (255, 0, 0) 
EDENEF = (237, 237, 239) 
 
# Find all #EDENEF pixels in the image 
ededef_pixels = [] 
for y in range(resized_height): 
    for x in range(resized_width): 
        if image.get_at((x, y)) == EDENEF: 
            ededef_pixels.append((x, y)) 
 
# Set up the clock 
clock = pygame.time.Clock() 
 
# Movement variables 
square_size = 5 
squares = [] 
num_squares = random.randint(5, 100)  # Choose a random number of squares between 5 and 100
for _ in range(num_squares): 
    start_x, start_y = random.choice(ededef_pixels) 
    squares.append(pygame.Rect(start_x, start_y, square_size, square_size)) 
 
# Main game loop 
while True: 
    screen.blit(image, (0, 0))  # Draw the resized image on the screen 
 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
 
    # Move the squares 
    for square in squares: 
        move_x = random.randint(-10, 10)  # Wider random movements 
        move_y = random.randint(-10, 10) 
        new_square = square.move(move_x, move_y) 
 
        # Check if the new square position is in the #ededef color 
        if image.get_at((new_square.centerx, new_square.centery)) == EDENEF: 
            square.move_ip(move_x, move_y) 
 
    # Draw the squares 
    for square in squares: 
        pygame.draw.rect(screen, RED, square)  # Draw the square with red color 
 
    # Display the number of squares moving 
    font = pygame.font.Font(None, 36) 
    text = font.render(f"Number of squares moving: {num_squares}", True, (255, 255, 255)) 
    screen.blit(text, (10, 10)) 
 
    pygame.display.flip() 
    clock.tick(20)

#------------------------------------------------------------------------------------------------
# import pygame 
# import sys 
# import random 
# import tkinter as tk

# # Initialize pygame 
# pygame.init() 

# # Load the image 
# image = pygame.image.load("/home/asus/Downloads/opal_edition.png") 
# original_width, original_height = image.get_size() 
# resized_width, resized_height = original_width // 3 * 2, original_height // 3 * 2 
# image = pygame.transform.scale(image, (resized_width, resized_height)) 

# # Set up the screen 
# screen = pygame.display.set_mode((resized_width, resized_height)) 
# pygame.display.set_caption("Move the Square") 

# # Set up the colors 
# RED = (255, 0, 0) 
# EDENEF = (237, 237, 239) 

# # Find all #EDENEF pixels in the image 
# ededef_pixels = [] 
# for y in range(resized_height): 
#     for x in range(resized_width): 
#         if image.get_at((x, y)) == EDENEF: 
#             ededef_pixels.append((x, y)) 

# # Set up the clock 
# clock = pygame.time.Clock() 

# # Movement variables 
# square_size = 5 
# squares = [] 
# num_squares = random.randint(5, 100)  # Choose a random number of squares between 5 and 10 
# for _ in range(num_squares): 
#     start_x, start_y = random.choice(ededef_pixels) 
#     squares.append(pygame.Rect(start_x, start_y, square_size, square_size)) 

# # Initialize tkinter
# root = tk.Tk()
# root.title("Map Viewer")

# # Create a text box
# text_box = tk.Text(root, height=10, width=20)
# text_box.grid(row=0, column=1, padx=10, pady=10)

# # Function to update the text box with selected red dot location
# def update_text_box(x, y):
#     text_box.delete('1.0', tk.END)
#     text_box.insert(tk.END, f"Location: ({x}, {y})")

# # Main game loop 
# while True: 
#     screen.blit(image, (0, 0))  # Draw the resized image on the screen 

#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT: 
#             pygame.quit() 
#             sys.exit() 
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:  # Left mouse button
#                 mouse_x, mouse_y = event.pos
#                 for square in squares:
#                     if square.collidepoint(mouse_x, mouse_y):
#                         update_text_box(square.x, square.y)
#                         break

#     # Move the squares 
#     for square in squares: 
#         move_x = random.randint(-10, 10)  # Wider random movements 
#         move_y = random.randint(-10, 10) 
#         new_square = square.move(move_x, move_y) 

#         # Check if the new square position is in the #ededef color 
#         if image.get_at((new_square.centerx, new_square.centery)) == EDENEF: 
#             square.move_ip(move_x, move_y) 

#     # Draw the squares 
#     for square in squares: 
#         pygame.draw.rect(screen, RED, square)  # Draw the square with red color 

#     # Display the number of squares moving 
#     font = pygame.font.Font(None, 36) 
#     text = font.render(f"Number of squares moving: {num_squares}", True, (255, 255, 255)) 
#     screen.blit(text, (10, 10)) 

#     pygame.display.flip() 
#     clock.tick(20)

#     root.update()  # Update tkinter window

# import pygame 
# import sys 
# import random 
# import tkinter as tk

# # Initialize pygame 
# pygame.init() 

# # Load the image 
# image = pygame.image.load("/home/asus/Downloads/opal_edition.png") 
# original_width, original_height = image.get_size() 
# resized_width, resized_height = original_width // 3 * 2, original_height // 3 * 2 
# image = pygame.transform.scale(image, (resized_width, resized_height)) 
 
# # Set up the screen 
# screen = pygame.display.set_mode((resized_width, resized_height)) 
# pygame.display.set_caption("Move the Square") 
 
# # Set up the colors 
# RED = (255, 0, 0) 
# EDENEF = (237, 237, 239) 
 
# # Find all #EDENEF pixels in the image 
# ededef_pixels = [] 
# for y in range(resized_height): 
#     for x in range(resized_width): 
#         if image.get_at((x, y)) == EDENEF: 
#             ededef_pixels.append((x, y)) 
 
# # Set up the clock 
# clock = pygame.time.Clock() 
 
# # Movement variables 
# square_size = 5 
# squares = [] 
# num_squares = random.randint(5, 100)  # Choose a random number of squares between 5 and 10 
# for _ in range(num_squares): 
#     start_x, start_y = random.choice(ededef_pixels) 
#     squares.append(pygame.Rect(start_x, start_y, square_size, square_size)) 

# # Default speed multiplier
# speed_multiplier = 1.0

# # Function to change speed based on slider value
# def change_speed(value):
#     global speed_multiplier
#     speed_multiplier = float(value)

# # Main game loop 
# while True: 
#     screen.blit(image, (0, 0))  # Draw the resized image on the screen 
 
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT: 
#             pygame.quit() 
#             sys.exit() 
 
#     # Move the squares 
#     for square in squares: 
#         move_x = random.randint(-10, 10) * speed_multiplier  # Adjust speed based on multiplier
#         move_y = random.randint(-10, 10) * speed_multiplier
#         new_square = square.move(move_x, move_y) 
 
#         # Check if the new square position is in the #ededef color 
#         if image.get_at((new_square.centerx, new_square.centery)) == EDENEF: 
#             square.move_ip(move_x, move_y) 
 
#     # Draw the squares 
#     for square in squares: 
#         pygame.draw.rect(screen, RED, square)  # Draw the square with red color 
 
#     # Display the number of squares moving 
#     font = pygame.font.Font(None, 36) 
#     text = font.render(f"Number of squares moving: {num_squares}", True, (255, 255, 255)) 
#     screen.blit(text, (10, 10)) 

#     pygame.display.flip() 
#     clock.tick(20)
