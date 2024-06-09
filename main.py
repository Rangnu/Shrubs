from Topic_Shrubs_UNRA import Shrub, shrubs_data
import tkinter as tk
from tkinter import messagebox

def find_my_shrub():
    # for user inputs!
    try:
        height_min = float(height_min_entry.get())
        height_max = float(height_max_entry.get())
        width_min = float(width_min_entry.get())
        width_max = float(width_max_entry.get())
        selected_colors = [color_var.get() for color_var in color_vars if color_var.get()]
        selected_climate = climate_var.get()
        average_lifespan = int(average_lifespan_entry.get())
        essential_tool = essential_tool_entry.get()

        results = []

        # matching logics
        for shrub in shrubs_data:
            score = 0

            # height
            shrub_height_min, shrub_height_max = map(float, shrub.height.split("m - "))
            if shrub_height_min <= height_max and shrub_height_max >= height_min:
                score += 1

            # width
            shrub_width_min, shrub_width_max = map(float, shrub.width.split("m - "))
            if shrub_width_min <= width_max and shrub_width_max >= width_min:
                score += 1

            # color
            shrub_colors = shrub.color.split(", ")
            color_matches = sum(1.5 for color in selected_colors if color in shrub_colors)
            score += color_matches

            # climate
            if selected_climate in shrub.climate:
                score += 1

            # lifespan
            if shrub.average_lifespan == average_lifespan:
                score += 1

            # essential tool
            if essential_tool in shrub.essential_tool:
                score += 1

            if score > 0:
                results.append((shrub, score))

        results.sort(key=lambda x: x[1], reverse=True)

        # output
        output = ""
        for shrub, score in results[:5]:
            output += f"{shrub.display_info()}\nScore: {score}\n\n"

        messagebox.showinfo("Top 5 Matching Shrubs", output)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for height, width, and lifespan ranges.")

def extract_colors(shrubs):
    colors = set()
    for shrub in shrubs:
        colors.update(shrub.color.split(", "))
    return colors

root = tk.Tk()
root.title("Your Own Shrub Finder")

# Height input box
tk.Label(root, text="Height Range (m) ->").grid(row=0, column=0)
tk.Label(root, text="Min").grid(row=0, column=1)
height_min_entry = tk.Entry(root)
height_min_entry.grid(row=0, column=2)
tk.Label(root, text="Max").grid(row=0, column=3)
height_max_entry = tk.Entry(root)
height_max_entry.grid(row=0, column=4)

# Width input box
tk.Label(root, text="Width Range (m) ->").grid(row=1, column=0)
tk.Label(root, text="Min").grid(row=1, column=1)
width_min_entry = tk.Entry(root)
width_min_entry.grid(row=1, column=2)
tk.Label(root, text="Max").grid(row=1, column=3)
width_max_entry = tk.Entry(root)
width_max_entry.grid(row=1, column=4)

# Colors
tk.Label(root, text="Colors").grid(row=2, column=0)
colors = extract_colors(shrubs_data)
color_vars = []
for i, color in enumerate(colors):
    var = tk.StringVar()
    chk = tk.Checkbutton(root, text=color, variable=var, onvalue=color, offvalue="")
    chk.grid(row=2 + i // 5, column=1 + i % 5)
    color_vars.append(var)

# Climate selecting
tk.Label(root, text="Climate").grid(row=3 + len(colors) // 5, column=0)
climate_var = tk.StringVar(value="Temperate")
climates = ["Temperate", "Arid", "Tropical", "Subtropical", "Cold"]
climate_menu = tk.OptionMenu(root, climate_var, *climates)
climate_menu.grid(row=3 + len(colors) // 5, column=1)

# Lifespan
tk.Label(root, text="Average Lifespan").grid(row=4 + len(colors) // 5, column=0)
average_lifespan_entry = tk.Entry(root)
average_lifespan_entry.grid(row=4 + len(colors) // 5, column=1)

# Essential Tool
tk.Label(root, text="Essential Tool").grid(row=5 + len(colors) // 5, column=0)
essential_tool_entry = tk.Entry(root)
essential_tool_entry.grid(row=5 + len(colors) // 5, column=1)

# Button
find_button = tk.Button(root, text="Find My Shrub", command=find_my_shrub, bg='green', font=("Helvetica", 12, "bold"))
find_button.grid(row=6 + len(colors) // 5, column=0, columnspan=8, pady=10)

root.mainloop()
