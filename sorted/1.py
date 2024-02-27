def count_str(name_file):
    with open(name_file, encoding='utf-8') as file_1:
        return max([count for  count,str_ in enumerate(file_1)])+1

def sorted_file(list_name_file):
    result = {}
    for indx, name_file in enumerate(list_name_file):
        result.setdefault(name_file, count_str(name_file))  
    result = (sorted(result.items(), key = lambda item: item[1]))
    result = [name[0] for name in result]
    return result

def union_file(list_name_file):
    for indx, name_file in enumerate(sorted(list_name_file)):
        with open(name_file, encoding="utf-8") as file:
            fail_text = file.read()
    return fail_text
        # with open(name_file, "w") as file:    



           
    
print(union_file(["sorted/1.txt", "sorted/2.txt", "sorted/3.txt"]))
