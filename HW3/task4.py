travel_items = {'Палатка': 3, 'Спальник': 2, 'Гиря': 24, 'Котелок': 3, 'Вода': 5, 'Еда': 6}
backpack_capacity = 9
res_dict = {}
weight = 0

for key, value in travel_items.items():
    if weight + value > backpack_capacity:
        continue
    if weight <= backpack_capacity:
        res_dict.update(dict([(key, value)]))
        weight += value
print(*res_dict, sep=", ")