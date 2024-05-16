#UN RA / group 4
class Shrub :
    def __init__(self, name, species, height, width, color, climate, average_lifespan, essential_tool):
        self.name = name
        self.species = species
        self.height = height
        self.width = width
        self.color = color
        self.climate = climate
        self.average_lifespan = average_lifespan
        self.essential_tool = essential_tool
        

    def display_info(self):
        info = [
            f"Name : {self.name}",
            f"Species : {self.species}",
            f"Height : {self.height}",
            f"Width : {self.width}",
            f"Color : {self.color}",
            f"Climate : {self.climate}",
            f"Average Lifespan : {self.average_lifespan}",
            f"Essential Tool : {self.essential_tool}"
       ]
        
    print("\n".join(info))