from .ShrubPlant import ShrubPlants

class Shrub(ShrubPlants):
    def __init__(self, name, species, MinHeight, MaxHeight, MinWidth, MaxWidth, color, climate, average_lifespan, essential_tool):
        super().__init__(name, species, MinHeight, MaxHeight, MinWidth, MaxWidth, color, climate, average_lifespan, essential_tool)

    def describe(self):
        return f"★{self._name} is a normal shrub.★"

shrubs_data = [
    Shrub("Abelia", "Abelia", "1.5m", "2m", "1m", "1.5m", "Green", "Temperate", 10, "Pruner"),
    Shrub("Acer", "Maple", "2m", "4m", "1.5m", "3m", "Red, Green", "Temperate", 20, "Shears"),
    Shrub("Actinidia", "Actinidia", "3m", "5m", "2m", "3m", "Green", "Temperate", 15, "Pruner"),
    Shrub("Aloe", "Aloe", "0.5m", "1m", "0.3m", "0.8m", "Green", "Arid", 5, "Spade"),
    Shrub("Aralia", "Angelica Tree", "2m", "3m", "1.5m", "2m", "Green", "Temperate", 25, "Shears, Pruner"),
    Shrub("Arctostaphylos", "Bearberry", "0.2m", "1m", "0.5m", "2m", "Red, Green", "Arid, Temperate", 7, "Hoe"),
    Shrub("Aronia", "Chokeberry", "1.5m", "2m", "1m", "1.5m", "Purple, Red, Green", "Cold, Temperate", 15, "Hoe, Pruner"),
    Shrub("Artemisia", "Sagebrush", "0.5m", "1.5m", "0.5m", "1.2m", "Silver, Green", "Arid, Temperate", 10, "Pruner, Shears"),
    Shrub("Aucuba", "Aucuba", "1m", "2.5m", "0.5m", "1.5m", "Green, Yellow", "Temperate", 20, "Rake, Pruner"),
    Shrub("Berberis", "Barberry", "0.5m", "2m", "0.5m", "1.5m", "Red, Green, Purple", "Temperate", 12, "Shears, Pruner"),
    Shrub("Bougainvillea", "Bougainvillea", "2m", "4m", "2m", "3m", "Purple, Pink, Red, White", "Tropical, Subtropical", 20, "Pruner, Shears"),
    Shrub("Brugmansia", "Angel's trumpet", "3m", "5m", "2.5m", "4m", "White, Yellow, Pink", "Tropical", 10, "Shears, Pruner"),
    Shrub("Buddleja", "Butterfly bush", "1.5m", "3m", "1.2m", "2m", "Purple, White, Pink", "Temperate", 15, "Pruner, Shears"),
    Shrub("Buxus", "Box", "0.5m", "1.5m", "0.5m", "1.2m", "Green", "Temperate", 12, "Rake, Shears"),
    Shrub("Calia", "Mescalbean", "1.5m", "3m", "1m", "2m", "Red", "Temperate", 15, "Hoe, Pruner"),
    Shrub("Callicarpa", "Beautyberry", "1m", "3m", "1m", "2m", "Purple", "Temperate", 10, "Pruner, Shears"),
    Shrub("Callistemon", "Bottlebrush", "2m", "4m", "1m", "2m", "Red", "Temperate", 8, "Pruner"),
    Shrub("Calluna", "Heather", "0.1m", "0.6m", "0.3m", "1m", "Purple", "Temperate", 20, "Shears"),
    Shrub("Calycanthus", "Sweetshrub", "1.5m", "3m", "1m", "2m", "Red", "Temperate", 15, "Shears, Pruner"),
    Shrub("Camellia", "Camellia", "1m", "5m", "1m", "2m", "Red, Pink, White", "Temperate", 50, "Shears"),
    Shrub("Caragana", "Pea-tree", "2m", "4m", "1m", "2m", "Yellow", "Temperate", 20, "Pruner"),
    Shrub("Carpenteria", "Carpenteria", "1.5m", "3m", "1m", "2m", "White", "Temperate", 15, "Shears"),
    Shrub("Caryopteris", "Blue Spiraea", "0.5m", "1m", "0.5m", "1m", "Blue", "Temperate", 8, "Pruner"),
    Shrub("Cassiope", "Moss-heather", "0.1m", "0.3m", "0.3m", "0.6m", "Pink, White", "Temperate", 25, "Shears, Pruner"),
    Shrub("Ceanothus", "Ceanothus", "0.5m", "3m", "0.5m", "2m", "Blue", "Temperate", 20, "Pruner"),
    Shrub("Celastrus", "Staff vine", "3m", "10m", "2m", "5m", "Red", "Temperate", 50, "Shears"),
    Shrub("Ceratostigma", "Hardy Plumbago", "0.1m", "0.5m", "0.3m", "1m", "Blue", "Temperate", 10, "Pruner"),
    Shrub("Cercocarpus", "Mountain-mahogany", "2m", "6m", "1m", "3m", "Red, Yellow", "Temperate", 50, "Shears"),
    Shrub("Chaenomeles", "Japanese Quince", "1m", "3m", "1m", "2m", "Red, Pink, White", "Temperate", 25, "Pruner"),
    Shrub("Chamaebatiaria", "Fernbush", "1m", "3m", "1m", "2m", "White", "Temperate", 15, "Shears"),
    Shrub("Chamaedaphne", "Leatherleaf", "1m", "2m", "1m", "2m", "White, Pink", "Temperate", 20, "Pruner"),
    Shrub("Chimonanthus", "Wintersweet", "2m", "4m", "1m", "2m", "Yellow", "Temperate", 25, "Shears"),
    Shrub("Chionanthus", "Fringe-tree", "3m", "10m", "2m", "5m", "White", "Temperate", 50, "Pruner"),
    Shrub("Choisya", "Mexican-orange Blossom", "1m", "3m", "1m", "2m", "White", "Temperate", 20, "Shears"),
    Shrub("Cistus", "Rockrose", "0.1m", "0.5m", "0.3m", "1m", "White, Pink", "Arid, Temperate", 10, "Pruner"),
    Shrub("Clerodendrum", "Clerodendrum", "1m", "3m", "1m", "2m", "Red, Purple, White", "Tropical", 15, "Shears"),
    Shrub("Clethra", "Summersweet", "1m", "2m", "1m", "2m", "White, Pink", "Temperate", 30, "Pruner"),
    Shrub("Clianthus", "Glory Pea", "2m", "4m", "1m", "2m", "Red", "Temperate", 15, "Shears"),
    Shrub("Colletia", "Colletia", "0.5m", "2m", "0.5m", "1.5m", "White", "Temperate", 25, "Pruner"),
    Shrub("Colutea", "Bladder Senna", "1m", "3m",     "0.5m", "1.5m", "Yellow", "Temperate", 20, "Pruner"),
    Shrub("Cordyline", "Cabbage Palm", "1m", "10m", "0.5m", "3m", "Red, Purple, Green", "Temperate", 20, "Pruner"),
    Shrub("Cornus", "Dogwood", "1m", "10m", "1m", "4m", "Red, Green", "Temperate", 30, "Shears"),
    Shrub("Corylus", "Hazel", "3m", "10m", "2m", "5m", "Red, Green", "Temperate", 50, "Shears"),
    Shrub("Cotoneaster", "Cotoneaster", "0.5m", "4m", "0.5m", "2m", "Red", "Temperate", 30, "Pruner"),
    Shrub("Crataegus", "Hawthorn", "1m", "10m", "1m", "4m", "White", "Temperate", 50, "Shears"),
    Shrub("Cytisus", "Broom", "0.5m", "3m", "0.5m", "2m", "Yellow", "Temperate", 30, "Shears"),
    Shrub("Daboecia", "St. Dabeoc's Heath", "0.1m", "0.5m", "0.2m", "1m", "Pink", "Temperate", 10, "Pruner"),
    Shrub("Daphne", "Daphne", "0.5m", "1.5m", "0.5m", "1m", "Pink, White", "Temperate", 20, "Pruner"),
    Shrub("Deutzia", "Deutzia", "1m", "3m", "1m", "2m", "White, Pink", "Temperate", 25, "Shears"),
    Shrub("Diervilla", "Bush honeysuckle", "1m", "2m", "1m", "2m", "Yellow", "Temperate", 30, "Shears"),
    Shrub("Dodonaea", "Hop Bush", "1m", "4m", "1m", "2m", "Green, Red", "Temperate", 25, "Pruner"),
    Shrub("Dracaena", "Dragon Tree", "1m", "10m", "0.5m", "3m", "Red, Green", "Temperate", 20, "Pruner"),
    Shrub("Echium", "Viper's Bugloss", "0.5m", "2m", "0.5m", "1.5m", "Blue", "Temperate", 5, "Shears"),
    Shrub("Elaeagnus", "Oleaster", "1m", "6m", "1m", "3m", "Yellow, Silver, Green", "Temperate", 50, "Pruner"),
    Shrub("Embothrium", "Chilean Firebush", "2m", "10m", "1m", "3m", "Red", "Temperate", 50, "Shears"),
    Shrub("Enkianthus", "Enkianthus", "1m", "6m", "1m", "3m", "Red, Green", "Temperate", 50, "Shears"),
    Shrub("Erica", "Heath", "0.1m", "2m", "0.2m", "1m", "Pink, White", "Temperate", 30, "Pruner"),
    Shrub("Euonymus", "Spindle", "0.5m", "6m", "0.5m", "2m", "Red, Green, Purple", "Temperate", 50, "Pruner"),
    Shrub("Exochorda", "Pearl Bush", "1m", "3m", "1m", "2m", "White", "Temperate", 50, "Shears"),
    Shrub("Forsythia", "Forsythia", "1m", "3m", "1m", "2m", "Yellow", "Temperate", 20, "Pruner"),
    Shrub("Fothergilla", "Fothergilla", "1m", "2m", "1m", "2m", "White", "Temperate", 30, "Pruner"),
    Shrub("Gaultheria", "Gaultheria", "0.1m", "1m", "0.2m", "0.5m", "Red, Green", "Temperate", 10, "Shears"),
    Shrub("Genista", "Broom", "0.5m", "3m", "0.5m", "2m", "Yellow", "Temperate", 30, "Shears"),
    Shrub("Grevillea", "Grevillea", "1m", "6m", "1m", "3m", "Red", "Temperate", 50, "Shears"),
    Shrub("Hamamelis", "Witch Hazel", "1m", "6m", "1m", "3m", "Yellow", "Temperate", 30, "Shears"),
    Shrub("Hebe", "Hebe", "0.5m", "2m", "0.5m", "1.5m", "Purple, White", "Temperate", 20, "Pruner"),
    Shrub("Hedera", "Ivy", "0.1m", "20m", "0.2m", "5m", "Green", "Temperate", 50, "Shears"),
    Shrub("Helianthemum", "Rock Rose", "0.1m", "0.5m", "0.2m", "1m", "Yellow, Pink", "Arid, Temperate", 10, "Pruner"),
    Shrub("Hemerocallis", "Daylily", "0.5m", "2m", "0.5m", "1.5m", "Yellow, Orange, Red", "Temperate", 10, "Shears"),
    Shrub("Hibiscus", "Hibiscus", "1m", "3m", "1m", "2m", "Red, Pink, White", "Tropical, Temperate", 20, "Pruner"),
    Shrub("Hippeastrum", "Amaryllis", "0.5m", "1m", "0.5m", "1m", "Red, Pink, White", "Temperate", 20, "Pruner"),
    Shrub("Hydrangea", "Hydrangea", "1m", "3m", "1m", "2m", "Blue, Pink, White", "Temperate", 50, "Pruner"),
    Shrub("Hypericum", "St. John's Wort", "0.5m", "2m", "0.5m", "1.5m", "Yellow", "Temperate", 30, "Shears"),
    Shrub("Ilex", "Holly", "1m", "20m", "1m", "10m", "Red", "Temperate", 100, "Shears"),
    Shrub("Indigofera", "Indigo", "0.5m", "2m", "0.5m", "1.5m", "Pink, White", "Temperate", 10, "Pruner"),
    Shrub("Itea", "Sweetspire", "1m", "3m", "1m", "2m", "White", "Temperate", 30, "Shears"),
    Shrub("Jasminum", "Jasmine", "1m", "3m", "1m", "2m", "White, Yellow", "Temperate, Tropical", 20, "Pruner"),
    Shrub("Juniperus", "Juniper", "0.5m", "20m", "0.5m", "10m", "Green, Blue", "Temperate, Arid", 100, "Shears"),
    Shrub("Kalmia", "Mountain Laurel", "0.5m", "4m", "0.5m", "2m", "Pink, White", "Temperate", 50, "Pruner"),
    Shrub("Kerria", "Kerria", "1m", "3m", "1m", "2m", "Yellow", "Temperate", 20, "Shears"),
    Shrub("Lagerstroemia", "Crape Myrtle", "1m", "6m", "1m", "3m", "Purple, Pink, White", "Temperate", 50, "Pruner"),
    Shrub("Lantana", "Lantana", "0.5m", "2m", "0.5m", "1.5m", "Red, Yellow, Purple", "Temperate, Tropical", 20, "Shears"),
    Shrub("Lavandula", "Lavender", "0.5m", "1.5m", "0.5m", "1m", "Purple, Pink, White", "Temperate, Arid", 20, "Pruner"),
    Shrub("Laurus", "Bay Laurel", "1m", "10m", "1m", "5m", "Green", "Temperate", 50, "Pruner"),
    Shrub("Leptospermum", "Tea Tree", "1m", "6m", "1m", "3m", "White, Pink, Red", "Temperate", 50, "Shears"),
    Shrub("Ligustrum", "Privet", "1m", "6m", "1m", "3m", "White", "Temperate", 50, "Pruner"),
    Shrub("Lonicera", "Honeysuckle", "1m", "3m", "1m", "2m", "White, Yellow, Pink", "Temperate", 20, "Shears"),
    Shrub("Magnolia", "Magnolia", "1m", "10m", "1m", "5m", "White, Pink, Purple", "Temperate", 50, "Pruner"),
    Shrub("Mahonia", "Mahonia", "1m", "3m", "1m", "2m", "Yellow", "Temperate", 20, "Shears"),
    Shrub("Malus", "Apple", "1m", "10m", "1m", "5m", "White, Pink", "Temperate", 50, "Pruner"),
    Shrub("Melaleuca", "Paperbark", "1m", "10m", "1m", "5m", "White, Yellow, Red", "Temperate", 50, "Shears"),
    Shrub("Myrtus", "Myrtle", "1m", "5m", "1m", "3m", "White", "Temperate", 50, "Pruner"),
    Shrub("Nandina", "Heavenly Bamboo", "0.5m", "2m", "0.5m", "1.5m", "White", "Temperate", 30, "Shears"),
    Shrub("Nerium", "Oleander", "1m", "6m", "1m", "3m", "White, Pink, Red", "Tropical, Temperate", 50, "Pruner"),
    Shrub("Olearia", "Olearia", "0.5m", "4m", "0.5m", "2m", "White", "Temperate", 30, "Shears"),
    Shrub("Osmanthus", "Osmanthus", "1m", "10m", "1m", "5m", "White", "Temperate", 50, "Pruner"),
    Shrub("Paeonia", "Peony", "0.5m", "1m", "0.5m", "1m", "White, Pink, Red", "Temperate", 30, "Pruner"),
    Shrub("Pennisetum", "Fountain Grass", "0.5m", "2m", "0.5m", "1.5m", "Green", "Temperate", 10, "Shears"),
    Shrub("Perovskia", "Russian Sage", "1m", "2m", "1m", "2m", "Blue, Purple", "Temperate", 20, "Pruner"),
    Shrub("Phillyrea", "Mock Privet", "1m", "6m", "1m", "3m", "Green", "Temperate", 50, "Pruner"),
    Shrub("Phlomis", "Jerusalem Sage", "1m", "2m", "1m", "2m", "Yellow", "Temperate", 20, "Shears"),
    Shrub("Photinia", "Photinia", "1m", "6m", "1m", "3m", "White", "Temperate", 50, "Pruner"),
    Shrub("Pieris", "Pieris", "1m", "3m", "1m", "2m", "White, Pink", "Temperate", 30, "Shears"),
    Shrub("Pittosporum", "Pittosporum", "1m", "10m", "1m", "5m", "White", "Temperate", 50, "Pruner"),
    Shrub("Plumbago", "Plumbago", "0.5m", "2m", "0.5m", "1.5m", "Blue", "Temperate", 20, "Shears"),
    Shrub("Polygala", "Polygala", "0.5m", "2m", "0.5m", "1.5m", "Purple, Pink, White", "Temperate", 20, "Pruner"),
    Shrub("Potentilla", "Cinquefoil", "0.5m", "2m", "0.5m", "1.5m", "Yellow, Pink, White", "Temperate", 20, "Shears"),
    Shrub("Prunus", "Cherry", "1m", "10m", "1m", "5m", "White, Pink", "Temperate", 50, "Pruner"),
    Shrub("Pyracantha", "Firethorn", "1m", "4m", "1m", "2m", "White", "Temperate", 30, "Shears"),
    Shrub("Rhaphiolepis", "Indian Hawthorn", "0.5m", "2m", "0.5m", "1.5m", "White, Pink", "Temperate", 30, "Shears"),
    Shrub("Rhododendron", "Rhododendron", "0.5m", "6m", "0.5m", "3m", "White, Pink, Purple", "Temperate", 50, "Pruner"),
    Shrub("Rhus", "Sumac", "1m", "6m", "1m", "3m", "Red", "Temperate", 50, "Pruner"),
    Shrub("Ribes", "Currant", "0.5m", "2m", "0.5m", "1.5m", "Red, White, Pink, Yellow", "Temperate", 20, "Shears"),
    Shrub("Robinia", "Robinia", "1m", "10m", "1m", "5m", "White, Pink", "Temperate", 50, "Pruner"),
    Shrub("Rosmarinus", "Rosemary", "0.5m", "2m", "0.5m", "1.5m", "Blue", "Temperate, Arid", 20, "Shears"),
    Shrub("Rubus", "Bramble", "1m", "10m", "1m", "5m", "White", "Temperate", 50, "Pruner"),
    Shrub("Salix", "Willow", "1m", "20m", "1m", "10m", "Yellow, Green", "Temperate", 100, "Pruner"),
    Shrub("Santolina", "Cotton Lavender", "0.5m", "1m", "0.5m", "1m", "Yellow", "Temperate", 10, "Shears"),
    Shrub("Sarcococca", "Sweet Box", "0.5m", "1m", "0.5m", "1m", "White", "Temperate", 30, "Pruner"),
    Shrub("Sorbaria", "False Spiraea", "1m", "3m", "1m", "2m", "White", "Temperate", 50, "Shears"),
    Shrub("Spartium", "Spanish Broom", "1m", "3m", "1m", "2m", "Yellow", "Temperate", 30, "Shears"),
    Shrub("Spiraea", "Spiraea", "0.5m", "2m", "0.5m", "1.5m", "White, Pink", "Temperate", 20, "Pruner"),
    Shrub("Symphoricarpos", "Snowberry", "0.5m", "2m", "0.5m", "1.5m", "White, Pink", "Temperate", 30, "Shears"),
    Shrub("Syringa", "Lilac", "1m", "6m", "1m", "3m", "Purple, White", "Temperate", 50, "Pruner"),
    Shrub("Tamarix", "Tamarisk", "1m", "6m", "1m", "3m", "Pink", "Temperate", 50, "Shears"),
    Shrub("Thuja", "Arborvitae", "1m", "20m", "1m", "10m", "Green", "Temperate", 100, "Pruner"),
    Shrub("Viburnum", "Viburnum", "1m", "5m", "1m", "3m", "White, Pink", "Temperate", 50, "Pruner"),
    Shrub("Weigela", "Weigela", "1m", "3m", "1m", "2m", "Pink", "Temperate", 30, "Pruner"),
    Shrub("Yucca", "Yucca", "1m", "3m", "1m", "2m", "White", "Arid", 30, "Shears"),
    Shrub("Zanthoxylum", "Prickly Ash", "1m", "15m", "1m", "15m", "Green", "Temperate", 20, "Shears"),
    Shrub("Zelkova", "Zelkova", "15m", "30m", "15m", "30m", "Green", "Temperate", 50, "Pruner"),
    Shrub("Ziziphus", "Jujube", "2m", "10m", "2m", "10m", "Yellow, Green", "Tropical", 15, "Shears"),
]


