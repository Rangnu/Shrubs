class ShrubPlants:
    def __init__(self, name, species, height, width, color, climate, average_lifespan, essential_tool):
        self._name = name
        self.species = species
        self._height = height
        self._width = width
        self._color = color
        self._climate = climate
        self._average_lifespan = average_lifespan
        self._essential_tool = essential_tool
    
    def display_info(self):
        return (f"ShrubPlants Info:\n"
                f"Name: {self._name}\n"
                f"Species: {self.species}\n"
                f"Height: {self._height}\n"
                f"Width: {self._width}\n"
                f"Color: {self._color}\n"
                f"Climate: {self._climate}\n"
                f"Average Lifespan: {self._average_lifespan} years\n"
                f"Essential Tool: {self._essential_tool}")
