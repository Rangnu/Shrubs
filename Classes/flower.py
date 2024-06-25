from .ShrubPlant import ShrubPlants

class Flower(ShrubPlants):
    def __init__(self, name, species, MinHeight, MaxHeight, MinWidth, MaxWidth, color, climate, average_lifespan, essential_tool):
        super().__init__(name, species, MinHeight, MaxHeight, MinWidth, MaxWidth, color, climate, average_lifespan, essential_tool)

    def describe(self):
        return f"★{self._name} is a flower.★"

    def care_instructions(self):
        return f"'{self._name}' need delicate handling with tools like: {self._essential_tool}"

flowers_data = [
    Flower("Rose", "Rose", "0.5m", "1m", "0.5m", "1m", "Red", "Temperate", 2, "Pruner"),
    Flower("Tulip", "Tulip", "0.3m", "0.6m", "0.3m", "0.6m", "Yellow", "Temperate", 1, "Shears"),
    Flower("Daisy", "Daisy", "0.1m", "0.3m", "0.1m", "0.3m", "White", "Temperate", 3, "Garden Trowel"),
    Flower("Lily", "Lily", "0.5m", "1m", "0.2m", "0.4m", "White", "Temperate", 2, "Watering Can"),
    Flower("Sunflower", "Sunflower", "1m", "3m", "0.5m", "1m", "Yellow", "Temperate", 3, "Hoe"),
    Flower("Orchid", "Orchid", "0.2m", "1m", "0.1m", "0.5m", "Various", "Tropical", 5, "Misting Bottle"),
    Flower("Lavender", "Lavender", "0.3m", "0.6m", "0.3m", "0.5m", "Purple", "Temperate", 4, "Pruning Shears"),
    Flower("Peony", "Peony", "0.5m", "1m", "0.5m", "1m", "Pink", "Temperate", 5, "Shears"),
    Flower("Hibiscus", "Hibiscus", "1m", "3m", "0.5m", "1m", "Red", "Tropical", 4, "Pruning Shears"),
    Flower("Carnation", "Carnation", "0.3m", "0.6m", "0.1m", "0.2m", "Red", "Temperate", 2, "Pruner"),
    Flower("Chrysanthemum", "Chrysanthemum", "0.3m", "0.6m", "0.3m", "0.6m", "Yellow", "Temperate", 3, "Shears"),
    Flower("Gerbera", "Gerbera", "0.2m", "0.5m", "0.1m", "0.3m", "Various", "Temperate", 2, "Watering Can"),
    Flower("Magnolia", "Magnolia", "2m", "5m", "2m", "5m", "White", "Temperate", 100, "Pruning Shears"),
    Flower("Daffodil", "Daffodil", "0.2m", "0.5m", "0.1m", "0.2m", "Yellow", "Temperate", 2, "Trowel"),
    Flower("Hyacinth", "Hyacinth", "0.2m", "0.5m", "0.1m", "0.2m", "Purple", "Temperate", 3, "Garden Trowel"),
    Flower("Anemone", "Anemone", "0.1m", "0.3m", "0.1m", "0.3m", "Various", "Temperate", 3, "Pruner"),
    Flower("Crocus", "Crocus", "0.1m", "0.2m", "0.1m", "0.2m", "Purple", "Temperate", 2, "Trowel"),
    Flower("Foxglove", "Foxglove", "1m", "2m", "0.3m", "0.6m", "Pink", "Temperate", 2, "Shears"),
    Flower("Iris", "Iris", "0.3m", "0.6m", "0.1m", "0.3m", "Various", "Temperate", 3, "Watering Can"),
    Flower("Morning Glory", "Morning Glory", "2m", "3m", "0.2m", "0.3m", "Various", "Temperate", 1, "Shears"),
    Flower("Dahlia", "Dahlia", "0.5m", "1m", "0.3m", "0.5m", "Various", "Temperate", 4, "Pruner"),
    Flower("Freesia", "Freesia", "0.2m", "0.5m", "0.1m", "0.2m", "Various", "Temperate", 2, "Trowel"),
    Flower("Bougainvillea", "Bougainvillea", "1m", "3m", "0.5m", "1m", "Various", "Tropical", 5, "Pruning Shears"),
    Flower("Gladiolus", "Gladiolus", "0.6m", "1m", "0.1m", "0.2m", "Various", "Temperate", 3, "Garden Trowel"),
    Flower("Petunia", "Petunia", "0.1m", "0.5m", "0.1m", "0.5m", "Various", "Temperate", 2, "Shears"),
    Flower("Zinnia", "Zinnia", "0.2m", "0.6m", "0.2m", "0.6m", "Various", "Temperate", 2, "Watering Can"),
    Flower("Marigold", "Marigold", "0.1m", "0.5m", "0.1m", "0.5m", "Various", "Temperate", 2, "Pruner"),
]
