import unittest
from main import calculate_score, find_top_ShrubPlants, extract_colors
from Classes.shrubs import Shrub
from Classes.flower import Flower
from Classes.tree import Tree

# Mock shrub data for testing
class MockShrub:
    def __init__(self, name, min_height, max_height, min_width, max_width, color, climate, average_lifespan, essential_tool):
        self.name = name
        self._min_height = min_height
        self._max_height = max_height
        self._min_width = min_width
        self._max_width = max_width
        self._color = color
        self._climate = climate
        self._average_lifespan = average_lifespan
        self._essential_tool = essential_tool

class TestShrubFinderFunctions(unittest.TestCase):
    def setUp(self):
        # Mock shrub data for testing
        self.shrub1 = MockShrub("Shrub1", "1.0m", "2.0m", "0.5m", "1.0m", "Purple", "Tropical", 15, "Shears")
        self.shrub2 = MockShrub("Shrub2", "0.5m", "1.5m", "0.5m", "1.0m", "Red, Yellow", "Temperate", 10, "Spade")
        self.shrub3 = MockShrub("Shrub3", "2.0m", "3.0m", "1.0m", "1.5m", "White, Blue", "Arid", 20, "Hoe")
        
        # Combine all data for testing
        self.all_data = [self.shrub1, self.shrub2, self.shrub3]

    def test_calculate_score(self):
        score1 = calculate_score(self.shrub1, 1.0, 2.0, 0.5, 1.0, ["Purple"], "Tropical", 10, "Shears")
        score2 = calculate_score(self.shrub2, 0.5, 1.5, 0.5, 1.0, ["Red"], "Temperate", 10, "Spade")
        score3 = calculate_score(self.shrub3, 2.0, 3.0, 1.0, 1.5, ["White", "Blue"], "Arid", 20, "Hoe")
        
        self.assertEqual(score1, 5, "Score for Shrub1 should be 5")
        self.assertEqual(score2, 6, "Score for Shrub2 should be 6")
        self.assertEqual(score3, 7, "Score for Shrub3 should be 7")

    def test_find_top_ShrubPlants(self):
        top_plants = find_top_ShrubPlants(self.all_data, 1.0, 2.0, 0.5, 1.0, ["Purple"], "Tropical", 10, "Shears")

        self.assertEqual(len(top_plants), 3, "There should be three top plants")
        self.assertEqual(top_plants[0][0].name, "Shrub1", "The top 1 plant should be Shrub1 (score 6 in this case)")
        self.assertEqual(top_plants[1][0].name, "Shrub2", "The top 2 plant should be Shrub2 (score 2 in this case)")
        self.assertEqual(top_plants[2][0].name, "Shrub3", "The top 3 plant should be Shrub3 (score 0 in this case)")

    def test_extract_colors(self):
        colors = extract_colors(self.all_data)
        
        self.assertIn("Purple", colors, "Purple should be in extracted colors")
        self.assertIn("Red", colors, "Red should be in extracted colors")
        self.assertIn("Blue", colors, "Blue should be in extracted colors")

if __name__ == '__main__':
    unittest.main()
