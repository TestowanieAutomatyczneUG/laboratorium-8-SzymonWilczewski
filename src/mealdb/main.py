import requests


class MealDB:
    def howManyIngredients(self, mealName):
        if type(mealName) != str:
            raise TypeError
        meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={mealName}").json()["meals"][0]
        ingredientsCount = 0
        for i in range(1, 21):
            if type(meal[f"strIngredient{i}"]) == str:
                if meal[f"strIngredient{i}"].upper().isupper() or meal[f"strIngredient{i}"].lower().islower():
                    ingredientsCount += 1
        return f"{meal['strMeal']} consists of {ingredientsCount} ingredients"

    def allCategories(self):
        categories = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?c=list").json()["meals"]
        result = []
        for category in categories:
            result.append(category["strCategory"])
        return result

    def howManyMealsByIngredient(self, ingredient):
        if type(ingredient) != str:
            raise TypeError
        meals = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}").json()["meals"]
        if not meals:
            return 0
        else:
            return len(meals)

    def mealsByCuisine(self, cuisine):
        if type(cuisine) != str:
            raise TypeError
        meals = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?a={cuisine}").json()["meals"]
        result = []
        for meal in meals:
            result.append((meal["strMeal"]))
        return result

    def averageAmountOfIngredientsByCuisine(self, cuisine):
        if type(cuisine) != str:
            raise TypeError
        meals = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?a={cuisine}").json()["meals"]
        ingredientsCount = 0
        for meal in meals:
            idMeal = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={int(meal['idMeal'])}").json()["meals"][0]
            for i in range(1, 21):
                if type(idMeal[f"strIngredient{i}"]) == str:
                    if idMeal[f"strIngredient{i}"].upper().isupper() or idMeal[f"strIngredient{i}"].lower().islower():
                        ingredientsCount += 1
        return ingredientsCount / len(meals)
