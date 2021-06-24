import io
from pprint import pprint


def read_file(filename):
    """Чтение из файла и создание словаря cook_book"""

    with open(filename, 'r', encoding="utf-8") as f:
        text = f.read()
        recipes = text.split('\n\n')

    cook_book = {}
    for item in recipes:
        recipe = item.split('\n')
        dish = recipe[0]
        kol = recipe[1]
        sostav = []
        for ingredient in recipe[2:int(kol)+2]:
            ingr = ingredient.split(' | ')
            d = {}
            d.update({'ingredient_name': ingr[0]})
            d.update({'quantity': ingr[1]})
            d.update({'measure': ingr[2]})
            sostav.append(d)
        cook_book.update({dish: sostav})
    # pprint(cook_book)

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    """Подготовка списка ингредиентов"""

    cook_book = read_file('recipes.txt')
    shop_list = {}
    for dish in dishes:
        # pprint(dish)
        for ingredient in cook_book[dish]:
            d = {}
            # pprint(ingredient)
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * int(person_count)
            else:
                d['measure'] = ingredient['measure']
                d['quantity'] = int(ingredient['quantity']) * int(person_count)
                shop_list[ingredient['ingredient_name']] = d

    return shop_list


# pprint(read_file('recipes.txt'))
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
