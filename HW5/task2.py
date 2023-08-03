names, salaries, bonuses = ["Максим", "Кирилл", "Пётр"], [8000, 5000, 9000], ["11%", "15%", "23%"]

def gen_salary_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in
            zip(names_list, salaries_list, bonuses_list)}

print(gen_salary_dict(names, salaries, bonuses))