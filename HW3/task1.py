friends = {
    'Лев': ('фонарик', 'палатка', 'удочка', 'спальник', 'лопата', 'горелка', 'нож', 'тушенка'),
    'Инокентий': ('котелок', 'пила', 'удочка', 'нож', 'спальник', 'лопата', 'фонарик', 'фотоаппарат'),
    'Григорий': ('фонарик', 'тушенка', 'удочка', 'спальник', 'фотоаппарат', 'лопата', 'отвертка', 'топорик'),
}

all_set = set()
uniq_set = set()
two_set = set()

for friend, items in friends.items():
    all_set.update(items)
    for item in items:
        if sum(item in friend_items for friend_items in friends.values()) == 1:
            uniq_set.add(item)
        elif sum(item in friend_items for friend_items in friends.values()) == 2:
            two_set.add(item)

common_set = set.intersection(*map(set, friends.values()))

print(f'Эти вещи взяли все: {common_set}')
print(f'Эти вещи только у одного: {uniq_set}')

for item in two_set:
    for friend, items in friends.items():
        if item not in items:
            print(f'Эти вещи имеют все, кроме {friend}: {item}')