### Задача 1 и 2

with open('cook_book.txt', encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        dish_ingredients = int(file.readline())
        ingredients_list = []
        for ingredients in range(dish_ingredients):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients_list.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
            cook_book.update({dish_name: ingredients_list})
        file.readline()

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_for_dishes = {}
    for dish in dishes:
        for dish_name, ingredients in cook_book.items():
            if dish == dish_name:
                for ingredient in ingredients:
                    ingredient['quantity'] *= person_count
                    if ingredient['ingredient_name'] not in ingredients_for_dishes:
                        count = {}
                        for key, value in ingredient.items():
                            if key == 'quantity' or key == 'measure':
                                count.update({key: value})
                        ingredients_for_dishes.update({ingredient['ingredient_name']: count})
                    else:
                        ingredients_for_dishes[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
    for v, k in ingredients_for_dishes.items():
        print(v, '-', k)

get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Картофель по деревенски'], 1)


### Задача 3

target_file = {}
count_file = 1
while count_file <= 3:
    with open(f'{count_file}.txt', encoding="utf-8") as file:
        target_file.update({count_file: len(file.readlines())})
    count_file += 1

target_file = dict(sorted(target_file.items(), key=lambda x: x[1]))

with open('target_file.txt', 'w', encoding="utf-8") as file:
    for key, value in target_file.items():
        file.write(f'{key}.txt\n')
        file.write(f'{value}\n')
        for i in range(1, value+1):
            file.write(f'Строка номер {i} файла номер {key}\n')
        file.write('\n')
