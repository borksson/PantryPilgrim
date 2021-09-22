import PantryPilgrim_CLASSES as pp
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def importSave():
	with open("pantryPilgrim.json", 'r') as file:
		save = json.load(file)
	return save

def saveFile(save):
	with open("pantryPilgrim.json", 'w') as file:
		file.write(json.dumps(save))

save = importSave()

newPantry = pp.Pantry([pp.Ingredient(pp.Base_Ingredient(ingredient["base_ingredient"]["name"],ingredient["base_ingredient"]["cost"]), ingredient["quantity"]) for ingredient in save["pantry"]["ingredientInventory"]])

newCookbook = pp.Cookbook([pp.Recipe([pp.Ingredient(pp.Base_Ingredient(ingredient["base_ingredient"]["name"],ingredient["base_ingredient"]["cost"]), ingredient["quantity"]) for ingredient in recipe["ingredientList"]],
 recipe["recipeSteps"], recipe["recipeTime"], recipe["name"]) for recipe in save["cookbook"]["recipeList"]], [pp.Base_Ingredient(base_ingredient["name"], base_ingredient["cost"]) for base_ingredient in save["cookbook"]["base_ingredientList"]])

newCalendar = pp.Calendar(([pp.Date(date["dts"],([pp.Meal(meal["mealType"],pp.Recipe(([pp.Ingredient(pp.Base_Ingredient(ingredient["base_ingredient"]["name"],ingredient["base_ingredient"]["cost"]),ingredient["quantity"])for ingredient in meal["recipe"]["ingredientList"]]),meal["recipe"]["recipeSteps"],meal["recipe"]["recipeTime"],meal["recipe"]["name"])for meal in date["mealList"])])for date in save["calendar"]["recipeCalendar"])]))


newRecipe = pp.Recipe([pp.Ingredient(pp.Base_Ingredient("Apple", 3), 2)],["Eat"],0,"Eat apple.")


print(newCalendar.toString())

save["pantry"] = newPantry.toOBJ()
save["cookbook"] = newCookbook.toOBJ()
save["calendar"] = newCalendar.toOBJ()
saveFile(save)
