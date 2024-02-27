def count_str(name_file):
    '''Данная функция нужна для подсчёта колличества строк в файле
    Функция принимает на вход имя файла или его путь в формате str
    Возвращает число строк в файле начиная от 1 в форамате int
    Пример:
    Ввод: "fail1"
    Вывод: 5
    '''
    with open(name_file, encoding='utf-8') as file_1:
        return max([count for  count,str_ in enumerate(file_1)])+1

def sorted_file(list_name_file):
    '''Данная функция предназначаена для сортировки списка с именнами
    файлов, по колличеству строк в этих файлах.
    На вход принимает лист, каждый элемент которого предстовляет собой
    имя файла или путь до него в формате str.
    Возвращает list с теми же элементами, но отсортированными по
    колличеству строк в файлах , от меньшего к большему.
    Пример рабты:
    Ввод: ["sorted/1.txt", "sorted/2.txt", "sorted/3.txt"] 
    Вывод: ["sorted/1.txt", "sorted/3.txt", "sorted/2.txt"]
    '''
    result = {}
    for name_file in list_name_file:
        result.setdefault(name_file, count_str(name_file))  
    result = (sorted(result.items(), key = lambda item: item[1]))
    result = [name[0] for name in result]
    return result

def union_file(list_name_file):
    '''Эта функция преднозначена для объединения N колличества файлов
    в один, по следующему правилу: 
    1. Объединяются файлы в том файле, который имеет наименьшее
    колличество строк
    2. Файлы записываются в результирующий файл попорядку, от файла с 
    наименьшим колличеством строк, до файла с наибольшим.
    3. Содержимое файла предваряеться служебной информацией на 2-х 
    строках: имя файла и количество строк в нем.
    Принимает на вход: list каждый объект которого, имя файла или путь
    до него.
    Возвращает None
    '''
    result = []
    first_fail = sorted_file(list_name_file)[0]
    with open(first_fail, encoding="utf-8") as file:
        result.append(f"{file.name}\n")
        result.append(f"{str(count_str(first_fail))}\n")
        result.append(file.read())
    with open(first_fail, "w", encoding="utf-8") as file:
        file.writelines(result)
    result = []
    for name_file in sorted_file(list_name_file)[1::]:
        with open(name_file, encoding="utf-8") as file:
            result.append(f"{file.name}\n")
            result.append(f"{str(count_str(name_file))}\n")
            result.append(f"{file.read()}\n")
        with open(first_fail, "a", encoding="utf-8") as file:
            file.writelines(result)
        result = []

union_file(["sorted/1.txt", "sorted/2.txt", "sorted/3.txt"])
