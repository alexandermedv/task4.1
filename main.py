import io
from pprint import pprint

with open('recipes.txt', 'r', encoding="utf-8") as f:
    text = f.read()
    recipes = text.split('\n\n')
    # print (recipes)

cook_book = {}
for item in recipes:
    recipe = item.split('\n')
    # print(recipe)
    dish = recipe[0]
    kol = recipe[1]
    # print('Название блюда:', dish)
    # print('Количество ингредиентов:', kol)
    sostav = []
    for ingredient in recipe[2:int(kol)+2]:
        # print(ingredient)
        ingr = ingredient.split(' | ')
        d = {}
        d.update({'ingredient_name': ingr[0]})
        d.update({'quantity': ingr[1]})
        d.update({'measure': ingr[2]})
        sostav.append(d)
    # print('sostav:', sostav)
    cook_book.update({dish: sostav})
# print(dish)
# print(sostav)
pprint(cook_book)
