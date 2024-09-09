from Buildings import *

class Recipe:
    def __init__(self, name, building, ingredients, output):
        self.name = name
        self.building = building
        self.ingredients = ingredients
        self.output = output

class Ore:
    def __init__(self, name):
        self.name = name
        self.building = None
    def setBuilding(self, building):
        self.building = building


class OreNode:
    def __init__(self, name, ore, purity, minerlevel):
        self.name = name
        self.ore = ore
        self.purity = purity
        self.minerlevel = minerLevel
        self.powerShards = 3

class Part:
    def __init__(self, name, recipes):
        self.name = name
        self.recipe = recipes


ironOre = Ore("Iron Ore")
copperOre = Ore("Copper Ore")
cateriumOre = Ore("Caterium Ore")
coal = Ore("Coal")
sulfurOre = Ore("Sulfur Ore")
limestone = Ore("Limestone")
rawQuartz = Ore("Raw Quartz")
bauxite = Ore("Bauxite")
uranium = Ore("Uranium")
samOre = Ore("SAM Ore")
nitrogenGas = Ore("Nitrogen Gas")
water = Ore("Water")
crudeOil = Ore("Crude Oil")
heavyOilResidue = Ore("Heavy Oil Residue")
polymerResin = Ore("Polymer Resin")
aluminumScrap = Ore("Aluminum Scrap")


silica = Part("Silica", [
    Recipe("Silica", constructor, {rawQuartz: 22.5}, {"self": 37.5}),
    Recipe("Cheap Silica", assembler, {rawQuartz: 11.25, limestone: 18.75}, {"self": 26.25})
    ])

quartzCrystal = Part("Quartz Crystal", [
    Recipe("Quartz Crystal", constructor, {rawQuartz: 37.5}, {"self": 22.5}),
    Recipe("Pure Quartz Crystal", refinery, {rawQuartz: 67.5, water: 37.5}, {"self": 52.5})
    ])

fuel = Part("Fuel", [
    Recipe("Fuel", refinery, {crudeOil: 60}, {"self": 40, polymerResin: 30}),
    Recipe("Residual Fuel", refinery, {heavyOilResidue: 60}, {"self": 40}),
#    Recipe("Packaged Fuel", packager, {fuel: 40}, {"self": 60})
    ])

plastic = Part("Plastic", [
    Recipe("Plastic", refinery, {polymerResin: 30, fuel: 10}, {"self": 20}),
    Recipe("Recycled Plastic", refinery, {polymerResin: 30, water: 20}, {"self": 20})
    ])

rubber = Part("Rubber", [
    Recipe("Rubber", refinery, {crudeOil: 30}, {"self": 20, heavyOilResidue: 20}),
    Recipe("Residual Rubber", refinery, {polymerResin: 30, water: 20}, {"self": 20}),
    Recipe("Recycled Rubber", refinery, {plastic: 15, fuel: 5}, {"self": 60})
    ])

concrete = Part("Concrete", [
    Recipe("Concrete", constructor, {limestone: 45}, {"self": 15}),
    Recipe("Wet Concrete", refinery, {limestone: 120, water: 100}, {"self": 80}),
    Recipe("Fine Concrete", assembler, {limestone: 30, silica: 7.5}, {"self": 25}),
    Recipe("Rubber Concrete", assembler, {limestone: 50, rubber: 10}, {"self": 50})
    ])

ironIngot = Part("Iron Ingot", [
    Recipe("Iron Ingot", smelter, {ironOre: 30}, {"self": 30}),
    Recipe("Iron Alloy Ingot", foundry, {copperOre: 20, ironOre: 20}, {"self": 50}),
    Recipe("Pure Iron Ingot", refinery, {ironOre: 35, water: 20}, {"self": 65})
    ])

copperIngot = Part("Copper Ingot", [
    Recipe("Copper Ingot", smelter, {copperOre: 30}, {"self": 30}),
    Recipe("Copper Alloy Ingot", foundry, {copperOre: 50,ironOre: 25}, {"self": 100}),
    Recipe("Pure Copper Ingot", refinery, {copperOre: 15, water: 10}, {"self": 37.5})
    ])

cateriumIngot = Part("Caterium Ingot", [
    Recipe("Caterium Ingot", smelter, {cateriumOre: 45}, {"self": 15}),
    Recipe("Pure Caterium Ingot", refinery, {cateriumOre: 15, water: 10}, {"self": 37.5})
    ])

quickwire = Part("Quickwire", [
    Recipe("Quickwire", constructor, {cateriumIngot: 12}, {"self": 60}),
    Recipe("Fused Quickwire", assembler, {cateriumIngot: 7.5, copperIngot: 37.5}, {"self": 90})
    ])

compactedCoal = Part("Compacted Coal", [
    Recipe("Compacted Coal", assembler, {coal: 25, sulfurOre: 25}, {"self": 25})
    ])

petroleumCoke = Part("Petroleum Coke", [
    Recipe("Petroleum Coke", refinery, {heavyOilResidue: 40}, {"self": 120})
    ])

steelIngot = Part("Steel Ingot", [
    Recipe("Steel Ingot", foundry, {ironOre: 45, coal: 45}, {"self": 45}),
    Recipe("Solid Steel Ingot", foundry, {ironIngot: 40,coal: 40}, {"self": 60}),
    Recipe("Coke Steel Ingot", foundry, {ironOre: 75, petroleumCoke: 75}, {"self": 100}),
    Recipe("Compacted Steel Ingot", foundry, {ironIngot: 22.5,compactedCoal: 11.25}, {"self": 37.5})
    ])

ironRod = Part("Iron Rod", [
    Recipe("Iron Rod", constructor, {ironIngot: 15}, {"self": 15}),
    Recipe("Steel Rod", constructor, {steelIngot: 12}, {"self": 48})
    ])

screw = Part("Screw", [
    Recipe("Screw", constructor, {ironRod: 10}, {"self": 40}),
    Recipe("Cast Screw", constructor, {ironIngot: 12.5}, {"self": 50}),
    Recipe("Steel Screw", constructor, {steelIngot: 5}, {"self": 260})
    ])

ironPlate = Part("Iron Plate", [
    Recipe("Iron Plate", constructor, {ironIngot: 30}, {"self": 20}),
    Recipe("Coated Iron Plate", assembler, {ironIngot: 50, plastic: 10}, {"self": 75}),
    Recipe("Steel Coated Plate", assembler, {steelIngot: 7.5, plastic: 5}, {"self": 45}),
])

wire = Part("Wire", [
    Recipe("Wire", constructor, {copperIngot: 15}, {"self": 30}),
    Recipe("Caterium Wire", constructor, {cateriumIngot: 15}, {"self": 120}),
    Recipe("Fused Wire", assembler, {copperIngot: 12, cateriumIngot: 3}, {"self": 90}),
    Recipe("Iron Wire", constructor, {ironIngot: 12.5}, {"self": 22.5})
    ])

cable = Part("Cable", [
    Recipe("Cable", constructor, {wire: 60}, {"self": 30}),
    Recipe("Quickwire Cable", assembler, {cateriumIngot: 7.5, rubber: 5}, {"self": 27.5}),
    Recipe("Coated Cable", refinery, {wire: 37.5, heavyOilResidue: 15}, {"self": 30}),
    Recipe("Insulated Cable", assembler, {wire: 45, rubber: 30}, {"self": 100})
    ])

copperSheet = Part("Copper Sheet", [
    Recipe("Copper Sheet", constructor, {copperIngot: 20}, {"self": 20}),
    Recipe("Steamed Copper Sheet", refinery, {copperIngot: 22.5, water: 22.5}, {"self": 40})
    ])

reinforcedIronPlates = Part("Reinforced Iron Plates", [
    Recipe("Reinforced Iron Plates", assembler, {ironPlate: 30, screw: 60}, {"self": 5}),
    Recipe("Bolted Iron Plates", assembler, {ironPlate: 90, screw: 250}, {"self": 15}),
    Recipe("Adhered Iron Plate", assembler, {ironPlate: 11.25, rubber: 3.75}, {"self": 3.75}),
    Recipe("Steel Coated Frame", assembler, {ironPlate: 15, wire: 37.5}, {"self": 5.63})
    ])

steelPipe = Part("Steel Pipe", [
    Recipe("Steel Pipe", constructor, {steelIngot: 30}, {"self": 20})
    ])

steelBeam = Part("Steel Beam", [
    Recipe("Steel Beam", constructor, {steelIngot: 60}, {"self": 15})
    ])

encasedIndustrialBeam = Part("Encased Industrial Beam", [
    Recipe("Encased Industrial Beam", assembler, {concrete: 30, steelBeam: 24}, {"self": 6}),
    Recipe("Encased Industrial Pipe", assembler, {concrete: 20, steelPipe: 28}, {"self": 4})
    ])

modularFrame = Part("Modular Frame", [
    Recipe("Modular Frame", assembler, {reinforcedIronPlates: 3, ironRod: 12}, {"self": 2}),
    Recipe("Bolted Frame", assembler, {reinforcedIronPlates: 7.5, screw: 140}, {"self": 6}),
    Recipe("Steeled Frame", assembler, {reinforcedIronPlates: 2, steelPipe: 10}, {"self": 5})
    ])

rotor = Part("Rotor", [
    Recipe("Rotor", assembler, {ironRod: 20, screw: 100}, {"self": 4}),
    Recipe("Steel Rotor", assembler, {steelPipe: 10, wire: 30}, {"self": 5}),
    Recipe("Copper Rotor", assembler, {copperSheet: 22.5, screw: 195}, {"self": 11.25})
    ])

stator = Part("Stator", [
    Recipe("Stator", assembler, {steelPipe: 10, wire: 20}, {"self": 6}),
    Recipe("Quickwire Stator", assembler, {quickwire: 10, steelPipe: 10}, {"self": 6}),
    ])

aiLimiter = Part("AI Limiter", [
    Recipe("AI Limiter", assembler, {quickwire: 100, copperSheet: 25}, {"self": 5})
    ])

circuitBoard = Part("Circuit Board", [
    Recipe("Circuit Board", assembler, {plastic: 30, copperSheet: 15}, {"self": 7.5}),
    Recipe("Silicon Circuit Board", assembler, {silica: 27.5, copperSheet: 27.5}, {"self": 12.5}),
    Recipe("Caterium Circuit Board", assembler, {plastic: 12.5, quickwire: 37.5}, {"self": 8.75}),
    Recipe("Electrode Circuit Board", assembler, {rubber: 30, petroleumCoke: 45}, {"self": 5}),
    ])

highSpeedConnector = Part("High-Speed Connector", [
    Recipe("High-Speed Connector", manufacturer, {quickwire: 210, cable: 37.5, circuitBoard: 3.75}, {"self": 5}),
    Recipe("Silicon High-Speed Connector", manufacturer, {quickwire: 90, silica: 37.5, circuitBoard: 3}, {"self": 5})
    ])

electromagneticControlRod = Part("Electromagnetic Control Rod", [
    Recipe("Electromagnetic Control Rod", assembler, {stator: 6, aiLimiter: 4}, {"self": 4}),
    Recipe("Magnetic Control Rod", assembler, {stator: 8, highSpeedConnector: 4}, {"self": 8}),
    ])


crystalOscillator = Part("Crystal Oscillator", [
    Recipe("Crystal Oscillator", manufacturer, {quartzCrystal: 18, cable: 14, reinforcedIronPlates: 2.5}, {"self": 1}),
    Recipe("Insulated Crystal Oscillator", manufacturer, {quartzCrystal: 18.75, aiLimiter: 1.88, rubber: 7.5}, {"self": 1}),
    ])

motor = Part("Motor", [
    Recipe("Motor", assembler, {rotor: 10, stator: 10}, {"self": 5}),
    Recipe("Electric Motor", assembler, {rotor: 7.5, electromagneticControlRod: 3.75}, {"self": 7.5}),
    Recipe("Rigour Motor", manufacturer, {rotor: 3.75, stator: 3.75, crystalOscillator: 1.25}, {"self": 7.5})
    ])

heavyModularFrame = Part("Heavy Modular Frame", [
    Recipe("Heavy Modular Frame", manufacturer, {modularFrame: 10, steelPipe: 30, encasedIndustrialBeam: 10, screw: 200}, {"self": 2}),
    Recipe("Heavy Encased Frame", manufacturer, {modularFrame: 7.5, steelPipe: 33.75, encasedIndustrialBeam: 9.38, concrete: 20.63}, {"self": 2.81}),
    Recipe("Heavy Flexible Frame", manufacturer, {modularFrame: 18.75, encasedIndustrialBeam: 11.25, rubber: 75, screw: 390}, {"self": 3.75})
    ])

smelter.setCost({ironRod: 5, wire: 8})
foundry.setCost({modularFrame: 10, rotor: 10, concrete: 20})
constructor.setCost({reinforcedIronPlates: 2, cable: 8})
assembler.setCost({reinforcedIronPlates: 8, rotor: 4, cable: 10})
manufacturer.setCost({heavyModularFrame: 10, motor: 5, cable: 50, plastic: 50})
refinery.setCost({motor: 10, encasedIndustrialBeam: 10, steelPipe: 30, copperSheet: 20})
packager.setCost({rubber: 10, steelBeam: 10, plastic: 10})
minermk1.setCost({ironPlate: 10, concrete: 10})
minermk2.setCost({encasedIndustrialBeam: 10, steelPipe: 20, modularFrame: 10})
#minermk3.setCost({heavyModularFrame: 10, motor: 10, cable: 50, plastic: 50})

#ores = [ironOre, copperOre, limestone, coal, cateriumOre, sulfurOre, rawQuartz, bauxite, uranium, samOre, rawQuartz, crudeOil, water]

#buildings = [smelter, foundry, constructor, assembler, manufacturer, refinery, packager, minermk1, minermk2, minermk3]

parts = [concrete, 
         ironIngot, ironRod, screw, ironPlate, reinforcedIronPlates,
         copperIngot, wire, cable, copperSheet,  
         cateriumIngot, quickwire, aiLimiter,
         quartzCrystal, silica, crystalOscillator,
         steelIngot, steelPipe, steelBeam, encasedIndustrialBeam,           
         plastic, rubber,  
         modularFrame, rotor, stator, motor, heavyModularFrame,
         circuitBoard, highSpeedConnector, electromagneticControlRod,  
         fuel, compactedCoal, petroleumCoke, 
         ]
