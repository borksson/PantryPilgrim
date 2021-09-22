import PantryPilgrim_CLASSES as pp
import json

SAVE_TEMPLATE_OBJ = {"pantry": {"ingredientInventory": []}, "cookbook": {"recipeList": [], "base_ingredientList": []}, "calendar": {"recipeCalendar": []}}

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def importSave():
	with open("pantryPilgrim.json", 'r') as file:
		try:
			save = json.load(file)
		except json.decoder.JSONDecodeError:
			print("SAVE FILE CORRUPTED")
			save = SAVE_TEMPLATE_OBJ
		return save

def saveFile(save):
	with open("pantryPilgrim.json", 'w') as file:
		file.write(json.dumps(save))
# Open and parse save into active objects
save = importSave()

newPantry = pp.Pantry([pp.Ingredient(pp.Base_Ingredient(ingredient["base_ingredient"]["name"],ingredient["base_ingredient"]["cost"]), ingredient["quantity"]) for ingredient in save["pantry"]["ingredientInventory"]])

newCookbook = pp.Cookbook([pp.Recipe([pp.Ingredient(pp.Base_Ingredient(ingredient["base_ingredient"]["name"],ingredient["base_ingredient"]["cost"]), ingredient["quantity"]) for ingredient in recipe["ingredientList"]],
 recipe["recipeSteps"], recipe["recipeTime"], recipe["name"]) for recipe in save["cookbook"]["recipeList"]], [pp.Base_Ingredient(base_ingredient["name"], base_ingredient["cost"]) for base_ingredient in save["cookbook"]["base_ingredientList"]])

newCalendar = pp.Calendar([pp.Date(date["dts"], [pp.Meal(meal["mealType"], pp.Recipe([pp.Ingredient(pp.Base_Ingredient(ingredient["base_ingredient"]["name"],ingredient["base_ingredient"]["cost"]), ingredient["quantity"]) for ingredient in meal["recipe"]["ingredientList"]],
 meal["recipe"]["recipeSteps"], meal["recipe"]["recipeTime"], meal["recipe"]["name"])) for meal in date["mealList"]]) for date in save["calendar"]["recipeCalendar"]])




# Export active objects and write to JSON
save["pantry"] = newPantry.toOBJ()
save["cookbook"] = newCookbook.toOBJ()
save["calendar"] = newCalendar.toOBJ()
saveFile(save)
