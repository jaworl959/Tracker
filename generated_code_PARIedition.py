# import tkinter as tk
# from tkinter import ttk
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import numpy as np
# import random
# from datetime import datetime, timedelta

# def generate_random_map(size):
#     return [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

# def plot_map(ax, map_array):
#     ax.clear()
#     ax.imshow(map_array, cmap='binary', interpolation='nearest')
#     ax.set_xlim(0, len(map_array[0]) - 1)
#     ax.set_ylim(0, len(map_array) - 1)
#     ax.axis('off')
#     ax.invert_yaxis()

# def main():
#     root = tk.Tk()
#     root.title("Map Viewer")
#     root.geometry("600x400")

#     map_size = 10
#     map_array = generate_random_map(map_size)

#     fig, ax = plt.subplots()
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas_widget = canvas.get_tk_widget()
#     canvas_widget.grid(row=0, column=0, padx=10, pady=10)

#     plot_map(ax, map_array)

#     info_text = tk.Text(root, height=10, width=30)
#     info_text.grid(row=0, column=1, padx=10, pady=10)

#     def move_circles_and_update():
#         plot_map(ax, map_array)
#         canvas.draw()
#         root.after(3000, move_circles_and_update)

#     move_circles_and_update()

#     root.mainloop()

# if __name__ == "__main__":
#     main()



# import tkinter as tk
# from tkinter import ttk
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import numpy as np
# from PIL import Image, ImageTk

# def load_special_image(image_path):
#     image = Image.open(image_path)
#     return np.array(image)

# def plot_map(ax, map_array):
#     ax.clear()
#     ax.imshow(map_array)
#     ax.axis('off')

# def main():
#     root = tk.Tk()
#     root.title("Map Viewer")
#     root.geometry("600x400")

#     # Load special image
#     special_image_path = "/home/asus/project/opal_edition.png"
#     special_image_array = load_special_image(special_image_path)

#     fig, ax = plt.subplots()
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas_widget = canvas.get_tk_widget()
#     canvas_widget.grid(row=0, column=0, padx=10, pady=10)

#     plot_map(ax, special_image_array)

#     root.mainloop()

# if __name__ == "__main__":
#     main()




# import tkinter as tk
# from tkinter import ttk
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import numpy as np
# from PIL import Image, ImageTk

# def load_special_image(image_path):
#     image = Image.open(image_path)
#     return np.array(image)

# def plot_map(ax, map_array):
#     ax.clear()
#     ax.imshow(map_array)
#     ax.axis('off')

# def main():
#     root = tk.Tk()
#     root.title("Map Viewer")
#     root.geometry("800x400")  # Adjusted geometry to accommodate the box on the right side

#     # Load special image
#     special_image_path = "/home/asus/project/opal_edition.png"
#     special_image_array = load_special_image(special_image_path)

#     fig, ax = plt.subplots()
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas_widget = canvas.get_tk_widget()
#     canvas_widget.grid(row=0, column=0, padx=10, pady=10)

#     plot_map(ax, special_image_array)

#     # Create the box on the right side
#     info_text = tk.Text(root, height=10, width=30)
#     info_text.grid(row=0, column=1, padx=10, pady=10)

#     root.mainloop()

# if __name__ == "__main__":
#     main()




import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk

def load_special_image(image_path):
    image = Image.open(image_path)
    return np.array(image)

def plot_map(ax, map_array):
    ax.clear()
    ax.imshow(map_array)
    ax.axis('off')

def main():
    root = tk.Tk()
    root.title("Map Viewer")
    root.geometry("800x400")  # Adjusted geometry to accommodate the box on the right side

    # Load special image
    special_image_path = "/home/asus/project/opal_edition2.png"
    special_image_array = load_special_image(special_image_path)

    fig, ax = plt.subplots(figsize=(8, 8))  # Adjust the figsize parameter to make the image larger
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=10)

    plot_map(ax, special_image_array)

    # Create the box on the right side
    info_text = tk.Text(root, height=10, width=30)
    info_text.grid(row=0, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
