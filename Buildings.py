class Building:
    def __init__(self, name):
        self.name = name
        self.cost = {}
    def setCost(self, cost):
        self.cost = cost

smelter = Building("Smelter")
constructor = Building("Constructor")
assembler = Building("Assembler")
foundry = Building("Foundry")
manufacturer = Building("Manufacturer")
refinery = Building("Refinery")
packager = Building("Packager")
blender = Building("Blender")
waterExtractor = Building("Water Extractor")
oilExtractor = Building("Oil Extractor")
oilRefinery = Building("Oil Refinery")
coalGenerator = Building("Coal Generator")
fuelGenerator = Building("Fuel Generator")
nuclearPowerPlant = Building("Nuclear Power Plant")
geothermalGenerator = Building("Geothermal Generator")
battery = Building("Battery")
coalGenerator = Building("Coal Generator")
nuclearPowerPlant = Building("Nuclear Power Plant")
biomassBurner = Building("Biomass Burner")
minermk1 = Building("Miner Mk.1")
minermk2 = Building("Miner Mk.2")
minermk3 = Building("Miner Mk.3")