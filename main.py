from tkinter import Tk, Label, Entry, OptionMenu, Checkbutton, Button, StringVar, messagebox
from Classes.shrubs import Shrub, shrubs_data
from Classes.flower import Flower, flowers_data
from Classes.tree import Tree, trees_data
from Classes.ShrubPlant import ShrubPlants

def calculate_score(plant, MinHeight, MaxHeight, MinWidth, MaxWidth, selected_colors, selected_climate, average_lifespan, essential_tool):
    score = 0
    
    # Convert input values to float
    MinHeight = float(MinHeight)
    MaxHeight = float(MaxHeight)
    MinWidth = float(MinWidth)
    MaxWidth = float(MaxWidth)
    
    # Strip 'm' and convert height and width attributes to float
    plant_min_height = float(plant._min_height.rstrip('m'))
    plant_max_height = float(plant._max_height.rstrip('m'))
    plant_min_width = float(plant._min_width.rstrip('m'))
    plant_max_width = float(plant._max_width.rstrip('m'))
    
    # Matching logic for height
    if MinHeight >= plant_min_height and MaxHeight <= plant_max_height:
        score += 1
    
    # Matching logic for width
    if MinHeight >= plant_min_height and MaxHeight <= plant_max_height:
        score += 1
    
    # Matching logic for color
    plant_colors = plant._color.split(", ")
    color_matches = sum(1 for color in selected_colors if color in plant_colors)
    score += color_matches
    
    # Matching logic for climate
    if average_lifespan <= plant._average_lifespan:
        score += 1
    
    # Matching logic for average lifespan
    if int(plant._average_lifespan) <= average_lifespan:
        score += 1
    
    # Matching logic for essential tool
    if essential_tool in plant._essential_tool:
        score += 1
    
    return score

def find_top_ShrubPlants(all_data, MinHeight, MaxHeight, MinWidth, MaxWidth, selected_colors, selected_climate, average_lifespan, essential_tool):
    results = []
    
    # Iterate over each plant in all data
    for plant in all_data:
        score = calculate_score(plant, MinHeight, MaxHeight, MinWidth, MaxWidth, selected_colors, selected_climate, average_lifespan, essential_tool)
        results.append((plant, score))
    
    # Sorting results by score, high to low
    results.sort(key=lambda x: x[1], reverse=True)
    
    # Get top 5 results
    top_ShrubPlants = results[:5]
    
    return top_ShrubPlants

def extract_colors(all_data):
    colors = set()
    for plant in all_data:
        colors.update(plant._color.split(", "))
    return colors

def find_top_plants():
    # Print the values retrieved from the entry fields
    print("Height Min:", MinHeight_entry.get())
    print("Height Max:", MaxHeight_entry.get())
    print("Width Min:", MinWidth_entry.get())
    print("Width Max:", MaxWidth_entry.get())
    print("Average Lifespan:", average_lifespan_entry.get())
    selected_colors = [color_var.get() for color_var in color_vars if color_var.get()]
    print("Selected Colors:", selected_colors)
    selected_climate = climate_var.get()
    print("Selected Climate:", selected_climate)
    essential_tool = essential_tool_var.get()
    print("Essential Tool:", essential_tool)

    try:
        # Retrieve user inputs
        MinHeight = float(MinHeight_entry.get())
        MaxHeight = float(MaxHeight_entry.get())
        MinWidth = float(MinWidth_entry.get())
        MaxWidth = float(MaxWidth_entry.get())
        selected_colors = [color_var.get() for color_var in color_vars if color_var.get()]
        selected_climate = climate_var.get()
        average_lifespan = int(average_lifespan_entry.get())
        essential_tool = essential_tool_var.get()
        
        # Combine all data
        all_data = shrubs_data + flowers_data + trees_data
        
        # Call find_top_ShrubPlants with combined data
        top_plants = find_top_ShrubPlants(all_data, MinHeight, MaxHeight, MinWidth, MaxWidth, selected_colors, selected_climate, average_lifespan, essential_tool)
        
        # Display results
        result_str = "Top 5 Best ShrubPlants:\n"
        for plant, score in top_plants:
            result_str += f"{plant.display_info()}\nScore: {score}\n\n"
        
        messagebox.showinfo("Top 5 Best ShrubPlants", result_str)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for height, width, and lifespan ranges.")
        
if __name__ == '__main__':
    root = Tk()
    root.title("Your Own Shrub Finder")

    # Height input box
    Label(root, text="Height Range (m) ->").grid(row=0, column=0)
    Label(root, text="Min").grid(row=0, column=1)
    MinHeight_entry = Entry(root)
    MinHeight_entry.grid(row=0, column=2)
    Label(root, text="Max").grid(row=0, column=3)
    MaxHeight_entry = Entry(root)
    MaxHeight_entry.grid(row=0, column=4)

    # Width input box
    Label(root, text="Width Range (m) ->").grid(row=1, column=0)
    Label(root, text="Min").grid(row=1, column=1)
    MinWidth_entry = Entry(root)
    MinWidth_entry.grid(row=1, column=2)
    Label(root, text="Max").grid(row=1, column=3)
    MaxWidth_entry = Entry(root)
    MaxWidth_entry.grid(row=1, column=4)

    # Colors
    Label(root, text="Colors").grid(row=2, column=0)
    # Combine all data for color extraction
    all_data = shrubs_data + flowers_data + trees_data
    colors = extract_colors(all_data)
    color_vars = []
    for i, color in enumerate(colors):
        var = StringVar()
        chk = Checkbutton(root, text=color, variable=var, onvalue=color, offvalue="")
        chk.grid(row=2 + i // 5, column=1 + i % 5)
        color_vars.append(var)

    # Climate selecting
    Label(root, text="Climate").grid(row=3 + len(colors) // 5, column=0)
    climate_var = StringVar(value="Temperate")
    climates = ["Temperate", "Arid", "Tropical", "Subtropical", "Cold"]
    climate_menu = OptionMenu(root, climate_var, *climates)
    climate_menu.grid(row=3 + len(colors) // 5, column=1)

    # Lifespan
    Label(root, text="Average Lifespan").grid(row=4 + len(colors) // 5, column=0)
    average_lifespan_entry = Entry(root)
    average_lifespan_entry.grid(row=4 + len(colors) // 5, column=1)

    # Essential Tool
    Label(root, text="Essential Tool").grid(row=5 + len(colors) // 5, column=0)
    essential_tool_var = StringVar()
    essential_tools = ["Pruner", "Shears", "Spade", "Hoe", "Rake"]
    essential_tool_menu = OptionMenu(root, essential_tool_var, *essential_tools)
    essential_tool_menu.grid(row=5 + len(colors) // 5, column=1)

    # Button
    find_button = Button(root, text="Find My Shrub", command=find_top_plants, bg='green', font=("Helvetica", 12, "bold"))
    find_button.grid(row=6 + len(colors) // 5, column=0, columnspan=8, pady=10)

    root.mainloop()
