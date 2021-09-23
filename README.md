Class file:
OBJECTS
- Ingredient (type of food and quantity)

- Recipe (list of ingredients, steps, and time)


SAVE DATA
- Pantry (inventory of ingredients)

- Cookbook (list of recipes, ingredients and their cost)

- Calendar (recipe scheduler)


UTILITY
- Shopper (builds shopping list off recipes and pantry, includes cost)
- MealPlanner (plans meals for a specific time period)
	- Cookbook population will be based off of recipes for the week. If a recipe is already in the cookbook, it will not be added ect.

Use Case:
I want to plan and shop for my meals for the next 7 days.
Get the current day and skip planning for that day.
Pattern for a week is have a meal for 5 of the seven days that take less than 30min to prepare.
Filter recipes on time to prepare (Sunday can be longer), dinner meals only (add breakfast dish for sunday?), cost (roughly 50 a week, optimal <10 per meal)
Mon - Meal
Tue - Meal
Wed - Meal
Thu - Left overs
Fri - Go out
Sat - Meal
Sun - Meal

Data file:
JSON OBJ with Pantry, Cookbook, and Calendar objects.

SSH scripts:
- getPantry()
- getCalendar()
- buildCalendar()
- buildShoppingList()
- getTodaysRecipe()

Export files:
- shopping list CSV? Microsoft task?