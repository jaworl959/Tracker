from PIL import Image
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import numpy as np
import random

#B&W MIKONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DOROST TARE
# def load_map_image(image_path):
#     img = Image.open(image_path).convert("L")  # Convert image to grayscale
#     img_array = np.array(img)
#     # Convert grayscale image to binary map (0 for white, 1 for black)
#     map_array = np.where(img_array > 128, 0, 1)
#     return map_array

def load_map_image(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    return img_array

def generate_random_circles(map_array, num_circles):
    circles = []
    height, width = map_array.shape  # Get the height and width of the map array
    for _ in range(num_circles):
        x, y = random.randint(0, height - 1), random.randint(0, width - 1)
        if map_array[x, y] == 1:
            circles.append((x, y))
    return circles

 
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

def main():
    root = tk.Tk()
    root.title("Map Viewer")
    root.geometry("800x400")

    # Load map image
    map_array = load_map_image("/home/asus/Downloads/opal_edition.png")  # Replace "your_map_image.png" with your image file path
    map_size = len(map_array)  # Adjust map size accordingly
    circles = generate_random_circles(map_array, 15)
    selected_circle_index = []

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=10)

    plot_map(ax, map_array, circles, selected_circle_index)

    info_text = tk.Text(root, height=10, width=30)
    info_text.grid(row=0, column=1, padx=10, pady=10)

    # Timer label
    timer_label = tk.Label(root, text="Time: 08:00:00", font=("Arial", 12))
    timer_label.grid(row=1, column=0, padx=10, pady=10)

    # Day label
    day_label = tk.Label(root, text="Day: Saturday", font=("Arial", 12))
    day_label.grid(row=2, column=0, padx=10, pady=10)  # Moved day label to row 2

    # Horizontal slider to adjust speed
    def change_speed(value):
        nonlocal timer_speed
        coefficient = int(value) / 1000
        timer_speed = int(1000 / coefficient)  # Update timer speed based on slider value
        speed_label.config(text=f"Speed: {coefficient:.1f}x")

    speed_scale = tk.Scale(root, from_=500, to=20000, orient=tk.HORIZONTAL, resolution=100, length=300,
                           label="Speed:", command=change_speed)
    speed_scale.set(1000)  # Default speed: 1x
    speed_scale.grid(row=3, column=0, padx=10, pady=10)  # Adjusted row to 3

    speed_label = tk.Label(root, text=f"Speed: {1000/1000:.1f}x", font=("Arial", 12))
    speed_label.grid(row=4, column=0, padx=10, pady=10)  # Adjusted row to 4

    # Function to update the timer
    def update_timer():
        nonlocal timer_value
        nonlocal current_day
        timer_value += 1
        if timer_value % (24 * 3600) == 0:
            timer_value = 8 * 3600  # Reset timer to 8:00:00
            current_day = (current_day + 1) % 7
            day_label.config(text=f"Day: {days_of_week[current_day]}")
        hours = (timer_value // 3600) % 24  # Adjust hours to cycle between 8 and 24
        minutes = (timer_value % 3600) // 60
        seconds = timer_value % 60
        timer_label.config(text=f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
        root.after(timer_speed, update_timer)  # Update after specified interval

    timer_speed = 1000  # Default speed: 1 second
    timer_value = 8 * 3600   # Initial timer value
    current_day = datetime.now().weekday()  # Get the current day of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    update_timer()  # Start the timer

    def update_info_text(event):
        nonlocal selected_circle_index
        selected_circle_index = []
        for i, circle in enumerate(circles):
            if circle[0] == int(event.ydata + 0.5) and circle[1] == int(event.xdata + 0.5):
                selected_circle_index.append(i)
        info_text.delete('1.0', tk.END)
        if selected_circle_index:
            selected_circle = circles[selected_circle_index[0]]
            info_text.insert(tk.END, f"Location: {selected_circle[0]}, {selected_circle[1]}\n")

    canvas.mpl_connect('button_press_event', update_info_text)

    # Function to move circles and update map
    import time

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


    def move_circles_and_update():
        start_time = time.time()
        nonlocal circles
        circles = move_circles(circles, map_array)
        plot_map(ax, map_array, circles, selected_circle_index)
        canvas.draw()
        elapsed_time = time.time() - start_time
        delay = max(0, timer_speed - int(elapsed_time * 1000))  # Adjust delay to maintain desired speed
        root.after(delay, move_circles_and_update)  # Update after adjusted delay

    move_circles_and_update()  # Start moving circles and updating map

    root.mainloop()

if __name__ == "__main__":
    main()
