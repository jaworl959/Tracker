import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import random
from datetime import datetime
import pygame
from PIL import Image, ImageTk
import sys

def generate_random_map(size):
    return [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

def plot_map(ax, map_array, circles, selected_circle_index):
    ax.clear()
    ax.imshow(map_array, cmap='binary', interpolation='nearest')
    ax.set_xlim(0, len(map_array[0]) - 1)
    ax.set_ylim(0, len(map_array) - 1)
    ax.axis('off')
    ax.invert_yaxis()
    for i, circle in enumerate(circles):
        color = 'r' if i in selected_circle_index else 'b'
        ax.plot(circle[1], circle[0], 'o', color=color)

def generate_random_circles(map_array, num_circles):
    circles = []
    for _ in range(num_circles):
        x, y = random.randint(0, len(map_array)-1), random.randint(0, len(map_array[0])-1)
        if map_array[x][y] == 1:
            circles.append((x, y))
    return circles

def move_circles(circles, map_array):
    new_circles = []
    for circle in circles:
        x, y = circle
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        new_x, new_y = x, y
        while (new_x == x and new_y == y) or not (0 <= new_x < len(map_array) and 0 <= new_y < len(map_array[0])) or \
                map_array[new_x][new_y] == 0:
            direction = random.choice(directions)
            new_x, new_y = x + direction[0], y + direction[1]
        new_circles.append((new_x, new_y))
    return new_circles

def main():
    root = tk.Tk()
    root.title("Map Viewer")
    root.geometry("800x400")
    root.configure(bg="lightblue")

    # Your code for generating map and setting up matplotlib canvas

    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Load the image
    image = pygame.image.load("/home/asus/project/opal_edition2.png")
    original_width, original_height = image.get_size()
    resized_width, resized_height = original_width // 3 * 2, original_height // 3 * 2
    image = pygame.transform.scale(image, (resized_width, resized_height))

    # Set up the screen
    pygame_screen = pygame.Surface((resized_width, resized_height))

    # Set up the colors
    RED = (255, 0, 0)
    EDENEF = (237, 237, 239)

    # Find all #EDENEF pixels in the image
    ededef_pixels = []
    for y in range(resized_height):
        for x in range(resized_width):
            if image.get_at((x, y)) == EDENEF:
                ededef_pixels.append((x, y))

    # Movement variables
    square_size = 5
    squares = []
    num_squares = random.randint(5, 100)  # Choose a random number of squares between 5 and 100
    for _ in range(num_squares):
        start_x, start_y = random.choice(ededef_pixels)
        squares.append(pygame.Rect(start_x, start_y, square_size, square_size))

    # Create info_text widget
    info_text = tk.Text(root, height=10, width=30)
    info_text.grid(row=0, column=1, padx=10, pady=10)

    def draw_squares(screen):
        for square in squares:
            pygame.draw.rect(screen, RED, square)  # Draw the square with red color

    # Pygame loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button clicked
                    # Check if any square is clicked and display its coordinates
                    mouse_pos = pygame.mouse.get_pos()
                    for square in squares:
                        if square.collidepoint(mouse_pos):
                            info_text.insert(tk.END, f"Clicked Square: {square.topleft}\n")

        # Move the squares
        for square in squares:
            move_x = random.randint(-10, 10)  # Wider random movements
            move_y = random.randint(-10, 10)
            new_square = square.move(move_x, move_y)

            new_square.centerx = np.clip(new_square.centerx, 0, resized_width - 1)
            new_square.centery = np.clip(new_square.centery, 0, resized_height - 1)

            # Check if the new square position is in the #ededef color
            if image.get_at((new_square.centerx, new_square.centery)) == EDENEF:
                square.move_ip(move_x, move_y)

        # Clear the Pygame screen
        pygame_screen.fill((0, 0, 0))

        # Draw the image
        pygame_screen.blit(image, (0, 0))

        # Draw the squares
        draw_squares(pygame_screen)

        # Convert the Pygame surface to a PIL Image
        pygame_image = pygame.surfarray.array3d(pygame_screen)
        pygame_image = np.swapaxes(pygame_image, 0, 1)
        pygame_image = np.flip(pygame_image, 0)
        pil_image = Image.fromarray(pygame_image)

        # Convert the PIL Image to a Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(pil_image)

        # Display the image on a Tkinter Label
        label = tk.Label(root, image=tk_image)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Update the Tkinter window
        root.update()

        # Control the frame rate
        clock.tick(20)

    pygame.quit()
    root.mainloop()

if __name__ == "__main__":
    main()
