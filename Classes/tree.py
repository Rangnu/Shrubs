from .ShrubPlant import ShrubPlants

class Tree(ShrubPlants):
    def __init__(self, name, species, MinHeight, MaxHeight, MinWidth, MaxWidth, color, climate, average_lifespan, essential_tool):
        super().__init__(name, species, MinHeight, MaxHeight, MinWidth, MaxWidth, color, climate, average_lifespan, essential_tool)

    def describe(self):
        return f"★{self._name} is a tree.★"

    def care_instructions(self):
        return f"'{self._name}' require strong tools like: {self._essential_tool}"

trees_data = [
    Tree("Oak", "Oak Tree", "15m", "20m", "10m", "15m", "Green", "Temperate", 100, "Spade"),
    Tree("Pine", "Pine Tree", "20m", "30m", "8m", "12m", "Green", "Cold", 50, "Rake"),
    Tree("Maple", "Maple Tree", "10m", "25m", "5m", "10m", "Green", "Temperate", 150, "Pruning Shears"),
    Tree("Birch", "Birch Tree", "15m", "20m", "4m", "6m", "White", "Temperate", 80, "Lopper"),
    Tree("Willow", "Willow Tree", "10m", "15m", "8m", "12m", "Green", "Temperate", 70, "Pruning Saw"),
    Tree("Fir", "Fir Tree", "25m", "30m", "6m", "10m", "Green", "Cold", 200, "Axe"),
    Tree("Ash", "Ash Tree", "15m", "25m", "10m", "15m", "Green", "Temperate", 120, "Chainsaw"),
    Tree("Cherry", "Cherry Tree", "6m", "10m", "4m", "6m", "Pink", "Temperate", 40, "Garden Trowel"),
    Tree("Cedar", "Cedar Tree", "20m", "25m", "8m", "12m", "Green", "Temperate", 300, "Handsaw"),
    Tree("Redwood", "Redwood Tree", "50m", "85m", "5m", "7m", "Reddish-Brown", "Temperate", 2000, "Chainsaw"),
    Tree("Magnolia", "Magnolia Tree", "6m", "10m", "3m", "5m", "White", "Temperate", 80, "Pruning Shears"),
    Tree("Poplar", "Poplar Tree", "15m", "30m", "5m", "10m", "Green", "Temperate", 100, "Hedge Shears"),
    Tree("Spruce", "Spruce Tree", "20m", "25m", "5m", "8m", "Green", "Cold", 150, "Lopper"),
    Tree("Dogwood", "Dogwood Tree", "5m", "8m", "3m", "5m", "White", "Temperate", 50, "Pruning Saw"),
    Tree("Hemlock", "Hemlock Tree", "10m", "20m", "5m", "8m", "Green", "Cold", 200, "Axe"),
    Tree("Juniper", "Juniper Tree", "1m", "4m", "1m", "2m", "Green", "Temperate", 100, "Pruning Shears"),
    Tree("Linden", "Linden Tree", "20m", "30m", "10m", "15m", "Green", "Temperate", 300, "Pruning Saw"),
    Tree("Mimosa", "Mimosa Tree", "5m", "8m", "4m", "6m", "Pink", "Temperate", 50, "Pruning Shears"),
    Tree("Cypress", "Cypress Tree", "20m", "25m", "5m", "10m", "Green", "Temperate", 200, "Hedge Shears"),
    Tree("Beech", "Beech Tree", "20m", "30m", "10m", "15m", "Green", "Temperate", 200, "Chainsaw"),
    Tree("Yew", "Yew Tree", "5m", "10m", "3m", "5m", "Green", "Temperate", 500, "Pruning Saw"),
    Tree("Ginkgo", "Ginkgo Tree", "20m", "30m", "8m", "10m", "Green", "Temperate", 1000, "Handsaw"),
    Tree("Locust", "Locust Tree", "10m", "20m", "5m", "10m", "Green", "Temperate", 150, "Axe"),
    Tree("Sycamore", "Sycamore Tree", "20m", "25m", "8m", "12m", "Green", "Temperate", 250, "Pruning Shears"),
    Tree("Walnut", "Walnut Tree", "15m", "25m", "10m", "15m", "Green", "Temperate", 150, "Chainsaw"),
    Tree("Hickory", "Hickory Tree", "15m", "25m", "8m", "12m", "Green", "Temperate", 200, "Axe"),
    Tree("Chestnut", "Chestnut Tree", "20m", "30m", "10m", "15m", "Green", "Temperate", 300, "Chainsaw"),
]
