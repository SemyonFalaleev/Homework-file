from pprint import pprint
def fail_list(fail_name):
    with open(fail_name, encoding='utf-8') as recieps:
        return [str_.strip() for str_ in recieps if not str_.isspace()]
    
def list_dict (list_):
    coock_boock = {}
    count = 0
    for indx,str_ in enumerate(list_):
        if count == 0:
            coock_boock[str_] = []
            count += 1
            keys = str_
            continue
        elif count == 1:
            count += 1 
            number = indx + int(str_)
            continue
        elif indx == number:
            x = str_.split("|")
            coock_boock[keys].append({'ingredient_name': x[0], 'quantity': x[1], 'measure': x[2]})
            keys = 0
            count = 0
            number = 0
        elif indx < number:
            x = str_.split("|")
            coock_boock[keys].append({'ingredient_name': x[0], 'quantity': x[1], 'measure': x[2]})
    return coock_boock

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = []
    result_dict = {}
    for dish in dishes:
        ingredients_list.append(list_dict(fail_list("coock_boock/recieps.txt"))[dish])
    for ingredient_dish in ingredients_list:
        for ingredient in ingredient_dish:
            if result_dict.get(ingredient['ingredient_name']) == None:
                result_dict.setdefault(ingredient['ingredient_name'], 
                {'quantity':int(f"{int(ingredient['quantity'])*int(person_count)}"),
                'measure': ingredient['measure']})
            else:
                result_dict[ingredient['ingredient_name']]['quantity'] += int(f"{int(ingredient['quantity'])*int(person_count)}")
    return result_dict

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
