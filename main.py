from Topic_Shrubs_UNRA import Shrub, shrubs_data
import tkinter as tk
from tkinter import messagebox

def find_my_shrub():
    height = height_entry.get()
    width = width_entry.get()
    color = color_entry.get()
    climate = climate_entry.get()
    average_lifespan = average_lifespan_entry.get()
    essential_tool = essential_tool_entry.get()

    shrub = Shrub(name, species, height, width, color, climate, average_lifespan, essential_tool)
    shrub_info = shrub.display_info()

    messagebox.showinfo("Shrub Information", shrub_info)

    

root = tk.Tk()
root.title("Your Own Shrub Finder")

tk.Label(root, text="Height").grid(row=2, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1)

tk.Label(root, text="Width").grid(row=3, column=0)
width_entry = tk.Entry(root)
width_entry.grid(row=3, column=1)

tk.Label(root, text="Color").grid(row=4, column=0)
color_entry = tk.Entry(root)
color_entry.grid(row=4, column=1)

tk.Label(root, text="Climate").grid(row=5, column=0)
climate_entry = tk.Entry(root)
climate_entry.grid(row=5, column=1)

tk.Label(root, text="Average Lifespan").grid(row=6, column=0)
average_lifespan_entry = tk.Entry(root)
average_lifespan_entry.grid(row=6, column=1)

tk.Label(root, text="Essential Tool").grid(row=7, column=0)
essential_tool_entry = tk.Entry(root)
essential_tool_entry.grid(row=7, column=1)

# Button
find_button = tk.Button(root, text="Find My Shrub", command=find_my_shrub)
find_button.grid(row=8, column=0, columnspan=2)

root.mainloop()