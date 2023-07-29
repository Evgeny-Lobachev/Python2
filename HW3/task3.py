big_text = "'Каждый выбирает для себя', Юрий Левитанский" \
           "Каждый выбирает для себя женщину, религию, дорогу." \
           "Дьяволу служить или пророку - каждый выбирает для себя." \
           "Каждый выбирает по себе слово для любви и для молитвы." \
           "Шпагу для дуэли, меч для битвы каждый выбирает по себе " \
           "Каждый выбирает по себе. Щит и латы. Посох и заплаты." \
           "Мера окончательной расплаты. Каждый выбирает по себе." \
           "Каждый выбирает для себя. Выбираю тоже - как умею." \
           "Ни к кому претензий не имею. Каждый выбирает для себя."

get_dict = {}
big_text_list = big_text.lower().split()
big_text_list_new = [''.join(filter(str.isalpha, a)) for a in
                     big_text_list]  

while '' in big_text_list_new:
    big_text_list_new.remove('')

for word in big_text_list_new:
    get_dict.setdefault(word, big_text_list_new.count(word))

count_words = 1
while count_words <= 10:
    count_words += 1
    max_key = max(get_dict, key=get_dict.get)
    print(f'{max_key:>5}  =  {get_dict[max_key]}')
    get_dict.pop(max_key)