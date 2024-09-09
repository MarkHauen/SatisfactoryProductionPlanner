from Parts import *

def printPartList(columns=3):
    num_parts = len(parts)
    rows = (num_parts + columns - 1) // columns 
    column_width = max(len(part.name) for part in parts) + 5  
    for row in range(rows):
        row_str = ""
        for col in range(columns):
            idx = row + col * rows
            if idx < num_parts:
                row_str += f"{idx + 1}: {parts[idx].name}".ljust(column_width)
        print(row_str)

    return int(input("   Choose a part: ")) - 1

def printRecipeOptions(partChoice):
    print(f"\n{parts[partChoice].name} Recipes:")
    for i in range (0, len(parts[partChoice].recipe)):
        print(f"    {(i+1)}: {parts[partChoice].recipe[i].name}: {", ".join([x.name for x in parts[partChoice].recipe[i].ingredients])}")
    return int(input("   Choose a recipe: "))