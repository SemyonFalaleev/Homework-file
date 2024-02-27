from pprint import pprint
def fail_list(fail_name):
    """Эта функция нужна для перевода всего содержимого файла в list,
    удаляя все непечатные символы.
    На ввод принимает имя или путь до файла
    Выход: список с содержимым файла, за исключением непечатных 
    символов.
    """
    with open(fail_name, encoding='utf-8') as recieps:
        return [str_.strip() for str_ in recieps if not str_.isspace()]
    
def list_dict (list_):
    '''Эта функция предназначена для создания словаря из листа
    сформированного функцией fail_list, на основе файла, данные 
    в котором структурированны по определённым правилам. 
    Файл должен состоять из одного или нескольких рецептов блюд
    в таком формате(пример блюда из 3 ингредиентов): 
    Название блюда
    3 (колличество ингредиентов в блюде)
    название ингредиента | число(его колличество) | еденица измерения
    название ингредиента | число(его колличество) | еденица измерения
    название ингредиента | число(его колличество) | еденица измерения

    На выходе функция выдаст такой словарь: 
    {
  'Название блюда': [
    {'ingredient_name': 'название ингредиента', 'quantity': число,
    'measure': 'еденица измерения'},
    {'ingredient_name': 'название ингредиента', 'quantity': число,
    'measure': 'еденица измерения'},
    {'ingredient_name': 'название ингредиента', 'quantity': число,
    'measure': 'еденица измерения'}
    ]
    }
    '''
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
            coock_boock[keys].append({'ingredient_name': x[0], 'quantity': x[1], 'measure': x[2].strip()})
            keys = 0
            count = 0
            number = 0
        elif indx < number:
            x = str_.split("|")
            coock_boock[keys].append({'ingredient_name': x[0], 'quantity': x[1], 'measure': x[2].strip()})
    return coock_boock

def get_shop_list_by_dishes(dishes, person_count):
    '''Функция предназначена для получения из файла 
    "coock_boock/recieps.txt" словаря с названием и 
    колличеством продуктов, для введённых блюд и кол-ва персон
    На ввод принимает: словарь с названиями блюд имеющихся в файле
    "coock_boock/recieps.txt", и число персон на которых необходимо
    приготовить блюда int или str.
    Пример работы: 
    Ввод: ['Запеченный картофель', 'Омлет'], 2
    Вывод: 
    {
    'Картофель ': {'measure': 'кг', 'quantity': 2},
    'Молоко ': {'measure': 'мл', 'quantity': 200},
    'Помидор ': {'measure': 'шт', 'quantity': 4},
    'Сыр гауда ': {'measure': 'г', 'quantity': 200},
    'Чеснок ': {'measure': 'зубч', 'quantity': 6},
    'Яйцо ': {'measure': 'шт', 'quantity': 4}
    }
    '''
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
