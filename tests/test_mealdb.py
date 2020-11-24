import unittest

from src.mealdb.main import MealDB


class MealDBTest(unittest.TestCase):
    def setUp(self):
        self.db = MealDB()

    def test_how_many_ingredients_1(self):
        self.assertEqual(self.db.howManyIngredients("Arrabiata"), "Spicy Arrabiata Penne consists of 8 ingredients")

    def test_how_many_ingredients_2(self):
        self.assertEqual(self.db.howManyIngredients("Carrot Cake"), "Carrot Cake consists of 12 ingredients")

    def test_how_many_ingredients_3(self):
        self.assertEqual(self.db.howManyIngredients("Tonkatsu"), "Tonkatsu pork consists of 9 ingredients")

    def test_how_many_ingredients_4(self):
        self.assertEqual(self.db.howManyIngredients("Kumpir"), "Kumpir consists of 6 ingredients")

    def test_all_categories(self):
        self.assertEqual(self.db.allCategories(), ['Beef', 'Breakfast', 'Chicken', 'Dessert', 'Goat', 'Lamb', 'Miscellaneous', 'Pasta', 'Pork', 'Seafood', 'Side', 'Starter', 'Vegan', 'Vegetarian'])

    def test_how_many_meals_by_ingredient_1(self):
        self.assertEqual(self.db.howManyMealsByIngredient("Chicken"), 10)

    def test_how_many_meals_by_ingredient_2(self):
        self.assertEqual(self.db.howManyMealsByIngredient("Aubergine"), 3)

    def test_how_many_meals_by_ingredient_3(self):
        self.assertEqual(self.db.howManyMealsByIngredient("Biryani Masala"), 0)

    def test_meals_by_cuisine_1(self):
        self.assertEqual(self.db.mealsByCuisine("Polish"), ['Bigos (Hunters Stew)', 'Gołąbki (cabbage roll)', 'Paszteciki (Polish Pasties)', 'Pierogi (Polish Dumplings)', 'Polskie Naleśniki (Polish Pancakes)', 'Rogaliki (Polish Croissant Cookies)', 'Rosół (Polish Chicken Soup)', 'Sledz w Oleju (Polish Herrings)'])

    def test_meals_by_cuisine_2(self):
        self.assertEqual(self.db.mealsByCuisine("Russian"), ['Beef stroganoff'])

    def test_meals_by_cuisine_3(self):
        self.assertEqual(self.db.mealsByCuisine("Unknown"), ['Cream Cheese Tart', 'Potato Gratin with Chicken'])

    def test_average_amount_of_ingredients_by_cuisine_1(self):
        self.assertAlmostEqual(10.625, self.db.averageAmountOfIngredientsByCuisine("Polish"), places=3)

    def test_average_amount_of_ingredients_by_cuisine_2(self):
        self.assertAlmostEqual(11.0, self.db.averageAmountOfIngredientsByCuisine("Russian"), places=1)

    def test_average_amount_of_ingredients_by_cuisine_3(self):
        self.assertAlmostEqual(11.0, self.db.averageAmountOfIngredientsByCuisine("Unknown"), places=1)

    def test_how_many_ingredients_wrong_type_1(self):
        with self.assertRaises(TypeError):
            self.db.howManyIngredients([])

    def test_how_many_ingredients_wrong_type_2(self):
        with self.assertRaises(TypeError):
            self.db.howManyIngredients(True)

    def test_how_many_meals_by_ingredient_wrong_type_1(self):
        with self.assertRaises(TypeError):
            self.db.howManyMealsByIngredient([])

    def test_how_many_meals_by_ingredient_wrong_type_2(self):
        with self.assertRaises(TypeError):
            self.db.howManyMealsByIngredient(True)

    def test_meals_by_cuisine_wrong_type_1(self):
        with self.assertRaises(TypeError):
            self.db.mealsByCuisine([])

    def test_meals_by_cuisine_wrong_type_2(self):
        with self.assertRaises(TypeError):
            self.db.mealsByCuisine(True)

    def test_average_amount_of_ingredients_by_cuisine_wrong_type_1(self):
        with self.assertRaises(TypeError):
            self.db.averageAmountOfIngredientsByCuisine([])

    def test_average_amount_of_ingredients_by_cuisine_wrong_type_2(self):
        with self.assertRaises(TypeError):
            self.db.averageAmountOfIngredientsByCuisine(True)

    def tearDown(self):
        self.db = None
