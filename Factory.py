from Dialog import *

class SubSystem:
    def __init__(self, recipe, amount, id):
        self.name = recipe.name              
        self.recipe = recipe        
        self.amount = amount          
        self.buildings = {}  
        self.id = id

    def addBuilding(self, building, amount):         
        if building not in self.buildings:
            self.buildings[building] = 0
        self.buildings[building] += amount

class BuildPlan:
    def __init__(self, recipe, amount):
        self.subsystems = []            
        self.buildings_needed = {}     
        self.total_building_cost = {}
        self.oresNeeded = {}  
        self.subcount = 1    
        self.magic = 42
        self.plan_recipe(recipe, amount)  

    def printSubSystems(self):
        for sub in self.subsystems:
            print(f"      SubSystem {sub.id}: {sub.recipe.name}: {sub.amount}")
            for buiding in sub.buildings:
                print(f"        {buiding.name}: {sub.buildings[buiding]}")

    def plan_recipe(self, recipe, amount):
        print(f"\n*****Building plan to produce {amount}/min of {recipe.name}*****")        
        stack = [(recipe, amount)] 
        while stack:
            current_recipe, current_amount = stack.pop()  
            machines_needed = self.calculate_machines(current_recipe, current_amount)
            building = current_recipe.building
            print(f"   Requires {machines_needed} {building.name}(s) for {current_recipe.name}")
            newSubsystem = SubSystem(current_recipe, current_amount, self.subcount)
            newSubsystem.addBuilding(building, machines_needed)
            self.subsystems.append(newSubsystem)
            self.track_building_usage(building, machines_needed)
            for ingredient_part, ingredient_amount_per_min in current_recipe.ingredients.items():
                required_amount = (ingredient_amount_per_min / current_recipe.output["self"]) * current_amount
                print(f"\n   Need {required_amount} of {ingredient_part.name}/min for {current_recipe.output['self']} of {current_recipe.name}/min")
                if isinstance(ingredient_part, Ore):
                    print(f"      Base resource: {ingredient_part.name}")
                    if ingredient_part.name not in self.oresNeeded:
                        self.oresNeeded[ingredient_part.name] = 0
                    self.oresNeeded[ingredient_part.name] += required_amount
                    print(f"     {required_amount} of {ingredient_part.name} will be needed (Total: {self.oresNeeded[ingredient_part.name]})")
                    oreSubSystem = SubSystem(ingredient_part, required_amount, self.subcount)
                    self.subsystems.append(oreSubSystem)
                    self.subcount += 1
                    continue  
                print(f"      Choose a recipe for {ingredient_part.name}:")
                for i, recipe in enumerate(ingredient_part.recipe, 1):
                    print(f"         {i}. {recipe.name}")
                recipe_choice = int(input("      Recipe choice: ")) - 1
                chosen_recipe = ingredient_part.recipe[recipe_choice]
                stack.append((chosen_recipe, required_amount))
    
    def calculate_machines(self, recipe, amount):
        output_rate = recipe.output["self"]
        machines_needed = amount / output_rate
        return round(machines_needed + 0.5)  

    def track_building_usage(self, building, machines_needed):
        if building not in self.buildings_needed:
            self.buildings_needed[building] = 0
        self.buildings_needed[building] += machines_needed
        for part, cost_amount in building.cost.items():
            total_cost = cost_amount * machines_needed
            if part not in self.total_building_cost:
                self.total_building_cost[part] = 0
            self.total_building_cost[part] += total_cost
    
    def display_total_building_cost(self):
        print("\n      Buildings Required:")
        for building, amount in self.buildings_needed.items():
            print(f"       {building.name}: {amount}")
        print("\n      Total building materials required:")
        for part, amount in self.total_building_cost.items():
            print(f"       {part.name}: {amount}")
        print("\n      Total Ores required:")
        for ore, amount in self.oresNeeded.items():
            print(f"       {ore}: {amount}")
            
########################################################

exitcode = 2
while exitcode == 2:
    partChoice = printPartList()
    amountchoice = int(input(f"   {parts[partChoice].name} Output Goal: "))
    recipechoice = printRecipeOptions(partChoice)    
    buildPlan = BuildPlan(parts[partChoice].recipe[recipechoice - 1], amountchoice)
    print(f"\n\n||||| Final Building plan for {parts[partChoice].recipe[recipechoice - 1].name} ({amountchoice}) |||||")
    buildPlan.printSubSystems()
    buildPlan.display_total_building_cost()    
    exitcode = int(input("Exit? 1: Yes, 2: No: "))
    