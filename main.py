def parse_file(file_):
    cook_book = {}
    ingredients = []

    with open("recipes.txt", "r", encoding="utf-8") as f:
        res = f.readlines()
        res.append("\n")
        for line in res:
            if line != "\n":
                ingredients.append(line.strip())
            elif line == "\n":
                cook_book[ingredients[0]] = []
                i = 2
                for line in range(int(ingredients[1])):
                    forwards = ingredients[i].split(" | ")
                    i += 1
                    cook_book[ingredients[0]].append(
                        {'ingredient_name': forwards[0], 'quantity': forwards[1], 'measure': forwards[2]})
                ingredients = []

    return cook_book


def get_shop_list_by_dishes(ingredients, person_count):
    all_dishes = parse_file("recipe.txt")

    count_dict = {}

    for dish in ingredients:
        if dish in all_dishes:
            for ingredients_counts in all_dishes[dish]:
                if ingredients_counts["ingredient_name"] not in count_dict:
                    count_dict[ingredients_counts["ingredient_name"]] = {"measure": ingredients_counts["measure"],
                                                                         "quantity": int(ingredients_counts[
                                                                                             "quantity"]) * person_count}
                else:
                    count_dict[ingredients_counts["ingredient_name"]]["quantity"] += int(
                        ingredients_counts["quantity"]) * person_count

    return count_dict


print(get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 2))
