from Classes.shrubs import Shrub, shrubs_data
from Classes.flower import Flower, flowers_data
from Classes.tree import Tree, trees_data
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
        essential_tool = essential_tool_var.get()

        # Logic to find best shrubs
        shrub_results = []
        for shrub in shrubs_data:
            score = 0

            # Matching logic
            shrub_height_min, shrub_height_max = map(float, shrub.height.split(" - "))
            if shrub_height_min <= height_max and shrub_height_max >= height_min:
                score += 1

            shrub_width_min, shrub_width_max = map(float, shrub.width.split(" - "))
            if shrub_width_min <= width_max and shrub_width_max >= width_min:
                score += 1

            shrub_colors = shrub.color.split(", ")
            color_matches = sum(1 for color in selected_colors if color in shrub_colors)
            score += color_matches

            if selected_climate in shrub.climate:
                score += 1

            if shrub.average_lifespan == average_lifespan:
                score += 1

            if essential_tool in shrub.essential_tool:
                score += 1

            if score > 0:
                shrub_results.append((shrub, score))

        # Logic to find best flowers
        flower_results = []
        for flower in flowers_data:
            score = 0

            # Matching logic
            flower_height_min, flower_height_max = map(float, flower.height.split(" - "))
            if flower_height_min <= height_max and flower_height_max >= height_min:
                score += 1

            flower_width_min, flower_width_max = map(float, flower.width.split(" - "))
            if flower_width_min <= width_max and flower_width_max >= width_min:
                score += 1

            flower_colors = flower.color.split(", ")
            color_matches = sum(1 for color in selected_colors if color in flower_colors)
            score += color_matches

            if selected_climate in flower.climate:
                score += 1

            if flower.average_lifespan == average_lifespan:
                score += 1

            if essential_tool in flower.essential_tool:
                score += 1

            if score > 0:
                flower_results.append((flower, score))

        # Logic to find best trees
        tree_results = []
        for tree in trees_data:
            score = 0

            # Matching logic
            tree_height_min, tree_height_max = map(float, tree.height.split(" - "))
            if tree_height_min <= height_max and tree_height_max >= height_min:
                score += 1

            tree_width_min, tree_width_max = map(float, tree.width.split(" - "))
            if tree_width_min <= width_max and tree_width_max >= width_min:
                score += 1

            tree_colors = tree.color.split(", ")
            color_matches = sum(1 for color in selected_colors if color in tree_colors)
            score += color_matches

            if selected_climate in tree.climate:
                score += 1

            if tree.average_lifespan == average_lifespan:
                score += 1

            if essential_tool in tree.essential_tool:
                score += 1

            if score > 0:
                tree_results.append((tree, score))

        # Sorting results by score, high to low!
        shrub_results.sort(key=lambda x: x[1], reverse=True)
        flower_results.sort(key=lambda x: x[1], reverse=True)
        tree_results.sort(key=lambda x: x[1], reverse=True)

        # Get top 5 results for each plant type
        top_shrubs = shrub_results[:5]
        top_flowers = flower_results[:5]
        top_trees = tree_results[:5]

        # Display results
        result_str = "Best Shrubs:\n"
        for shrub, score in top_shrubs:
            result_str += f"{shrub.display_info()}\nScore: {score}\n\n"

        result_str += "Best Flowers:\n"
        for flower, score in top_flowers:
            result_str += f"{flower.display_info()}\nScore: {score}\n\n"

        result_str += "Best Trees:\n"
        for tree, score in top_trees:
            result_str += f"{tree.display_info()}\nScore: {score}\n\n"

        messagebox.showinfo("Best Plants", result_str)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for height, width, and lifespan ranges.")

def extract_colors(Shrubs):
    colors = set()
    for Shrub in Shrubs:
        colors.update(Shrub.color.split(", "))
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
climates = ["Temperate", "Arid", "Tropical", "Subttropical", "Cold"]
climate_menu = tk.OptionMenu(root, climate_var, *climates)
climate_menu.grid(row=3 + len(colors) // 5, column=1)

# Lifespan
tk.Label(root, text="Average Lifespan").grid(row=4 + len(colors) // 5, column=0)
average_lifespan_entry = tk.Entry(root)
average_lifespan_entry.grid(row=4 + len(colors) // 5, column=1)

# Essential Tool
tk.Label(root, text="Essential Tool").grid(row=5 + len(colors) // 5, column=0)
essential_tool_var = tk.StringVar()
essential_tools = ["Pruner", "Shears", "Spade", "Hoe", "Rake"]
essential_tool_menu = tk.OptionMenu(root, essential_tool_var, *essential_tools)
essential_tool_menu.grid(row=5 + len(colors) // 5, column=1)

# Button
find_button = tk.Button(root, text="Find My Shrub", command=find_my_shrub, bg='green', font=("Helvetica", 12, "bold"))
find_button.grid(row=6 + len(colors) // 5, column=0, columnspan=8, pady=10)

root.mainloop()
