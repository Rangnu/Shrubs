#UN RA / group 4
class Shrub :
    def __init__(self, name, species, height, width, color, climate):
        self.name = name
        self.species = species
        self.height = height
        self.width = width
        self.color = color
        self.climate = climate

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")
        print(f"Height : {self.height}")
        print(f"Width : {self.width}")
        print(f"Color : {self.color}")
        print(f"Climate : {self.climate}")