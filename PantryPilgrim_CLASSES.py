import json

class Base_Ingredient:
	def __init__(self, name = "", cost = 0):
		self.name = name
		self.cost = cost
		
	def getCost(self):
		return self.cost

	def toString(self):
		return "Name: " + self.name + "\tCost: " + str(self.cost)

	def toOBJ(self):
		return {"name": self.name, "cost": self.cost}


class Ingredient:
	def __init__(self, base_ingredient, quantity = 0):
		self.base_ingredient = base_ingredient
		self.quantity = quantity
		self.worth = self.quantity*self.base_ingredient.getCost()

	def getWorth(self):
		return self.worth

	def toString(self):
		return "Base Ingredient: " + self.base_ingredient.toString() + "\t\tQuantity: " + str(self.quantity) + "\t\tWorth: " + str(self.worth)

	def toOBJ(self):
		return {"base_ingredient": self.base_ingredient.toOBJ(),"quantity": self.quantity,"worth": self.worth}


class Recipe:
	def __init__(self, ingredientList = [], recipeSteps = [], recipeTime = 0, name = ""):
		self.ingredientList = ingredientList
		self.recipeSteps = recipeSteps
		self.recipeTime = recipeTime
		self.name = name

	def toString(self):
		exportSteps = [(str(ind+1)+'. '+step) for ind, step in enumerate(self.recipeSteps)]
		exportIngredients = [ingredient.toString() for ingredient in self.ingredientList]
		return "Name: " + self.name + "\nIngredients: " + ", ".join(exportIngredients) + "\nSteps:\n" + '\n'.join(exportSteps) + "\nTime: " + str(self.recipeTime)

	def toOBJ(self):
		return {"name": self.name,"ingredientList": [ingredient.toOBJ() for ingredient in self.ingredientList], "recipeSteps": self.recipeSteps, "recipeTime": self.recipeTime}


class Pantry:
	def __init__(self, ingredientInventory = []):
		#FIXME: Add time added, or ingredient-pantry relationship
		self.ingredientInventory = ingredientInventory

	def addIngredient(self, ingredient):
		self.ingredientInventory.append(ingredient)
	
	def toString(self):
		exportIngredients = [ingredient.toString() for ingredient in self.ingredientInventory]
		return "Ingredients:\n"+'\n'.join(exportIngredients)

	def toOBJ(self):
		return {"ingredientInventory": [ingredient.toOBJ() for ingredient in self.ingredientInventory]}


class Cookbook:
	def __init__(self, recipeList = [], base_ingredientList = []):
		self.recipeList = recipeList
		self.base_ingredientList = base_ingredientList

	def addBase_Ingredient(self, base_ingredient):
		self.base_ingredientList.append(base_ingredient)

	def addRecipe(self, recipe):
		self.recipeList.append(recipe)

	def toString(self):
		exportRecipe = [recipe.toString() for recipe in self.recipeList]
		exportBase_Ingredients = [ingredient.toString() for ingredient in self.base_ingredientList]
		return "Recipe List:\n" + '\n'.join(exportRecipe) + "\nBase Ingredients:\n" + '\n'.join(exportBase_Ingredients)

	def toOBJ(self):
		return {"recipeList": [recipe.toOBJ() for recipe in self.recipeList],"base_ingredientList": [base_ingredient.toOBJ() for base_ingredient in self.base_ingredientList]}


class Meal:
	def __init__(self, mealType, recipe):
		self.mealType = mealType
		self.recipe = recipe

	def toString(self):
		return "Meal Type: " + self.mealType + "\nRecipe:\n" + self.recipe.toString()

	def toOBJ(self):
		return {"mealType": self.mealType, "recipe": self.recipe.toOBJ()}
	

class Date:
	def __init__(self, dts, mealList):
		self.dts = dts
		self.mealList = mealList

	def toString(self):
		exportMealList = [meal.toString() for meal in self.mealList]
		return "Date: " + self.dts + "\nMeals:\n" + '\n'.join(exportMealList)

	def toOBJ(self):
		return {"dts": self.dts, "mealList": [meal.toOBJ for meal in self.mealList]}
		

class Calendar:
	def __init__(self, recipeCalendar = []):
		self.recipeCalendar = recipeCalendar

	def toString(self):
		exportCalendar = [date.toString() for date in self.recipeCalendar]
		return "Calendar:\n" + '\n'.join(recipeCalendar)

	def toOBJ(self):
		return {"recipeCalendar": [date.toOBJ() for date in self.recipeCalendar]}


class Shopper:
	def __init__(self, usrCalendar, usrCookbook, usrPantry, shoppingList = []):
		self.shoppingList = shoppingList
		self.usrCalendar = usrCalendar
		self.usrCookbook = usrCookbook
		self.usrPantry = usrPantry

	def getShoppingListOBJ(self):
		cost = 0
		for ingredient in self.shoppingList:
			cost += ingredient.getWorth()
		return {"shoppingList": [ingredient.toOBJ() for ingredient in self.shoppingList], "cost": cost}