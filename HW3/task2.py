get_list = [1, 3, 1, 4, 3, 4, 7, 8, 9, 8, 2, 2]

dupl_elem = set()
for el in range(len(get_list)):
    if get_list.count(get_list[el]) > 1:
        dupl_elem.add(get_list[el])
print(f"Список с применением множеств: {list(dupl_elem)}")

dupl_elem = []
for el in range(len(get_list)):
    if get_list.count(get_list[el]) > 1 and dupl_elem.count(get_list[el]) < 1:
        dupl_elem.append(get_list[el])
print(f"Список без применения множеств: {dupl_elem}")