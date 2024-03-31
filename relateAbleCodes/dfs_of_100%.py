##kod moshkel dare
from PIL import Image, ImageDraw
import random
from PIL import Image, ImageDraw
import numpy as np
import random
import networkx as nx

##roye safhe sefid va map opal 4 ta 7 ta noghte random entekhab mikone va kotah tarin masir ro moshakhas mikone

# Create a new image with white background
image = Image.new("RGB", (100, 100), "white")
draw = ImageDraw.Draw(image)

# Randomly select the number of pixels to mark (between 4 and 7)
num_pixels = random.randint(4, 7)
#random_pixels = []
# Select random pixels and mark them in red
for _ in range(num_pixels):
    x = random.randint(0, 99)
    y = random.randint(0, 99)
    draw.point((x, y), fill="red")
   
   # random_pixels.append((x,y))

# Show the image
image.show()

# Create a new image with white background
image = Image.new("RGB", (100, 100), "white")
draw = ImageDraw.Draw(image)

# Randomly select the number of pixels to mark (between 4 and 7)
num_pixels = random.randint(4, 7)

# Store selected pixel coordinates and their heights
pixel_coords = []
for _ in range(num_pixels):
    x = random.randint(0, 99)
    y = random.randint(0, 99)
    height = random.randint(0, 255)  # assuming grayscale
    pixel_coords.append((x, y, height))

# Mark the selected pixels on the map
for x, y, _ in pixel_coords:
    draw.point((x, y), fill="red")

# Find the highest pixel and use it as the starting point
start_point = max(pixel_coords, key=lambda item: item[2])  # item[2] is the height

# Create a grid of pixel heights
height_grid = np.zeros((100, 100))
for x, y, height in pixel_coords:
    height_grid[y][x] = height

# Generate a graph with the height differences as weights
G = nx.grid_2d_graph(100, 100)
for (u, v) in G.edges():
    x1, y1 = u
    x2, y2 = v
    weight = abs(height_grid[y1][x1] - height_grid[y2][x2])
    G[u][v]['weight'] = weight

# Find the shortest path starting from the highest selected pixel
shortest_path = nx.shortest_path(G, source=(start_point[0], start_point[1]))

# Mark the shortest path on the image
for node in shortest_path:
    x, y = node
    draw.point((x, y), fill="blue")

# Show the image
image.show()

