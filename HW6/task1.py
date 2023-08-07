def date_exist(str_date):
    day, month, year = str_date.split(".")
    print(day, month, year)

    if int(year) in range(1, 9999):
        if int(year) % 400 == 0 or int(year) % 4 == 0 and int(year) % 100 != 0 and month == "02":
            if int(day) <= 29:
                return True
            else:
                return False
        elif int(year) % 400 == 0 or int(year) % 4 == 0 and int(year) % 100 != 0 and month == "02":
            if int(day) <= 28:
                return True
            else:
                return False
    elif int(year) not in range(1, 9999):
        return False

    if month in ["01", "03", "05", "07", "08", "10", "12"]:
        if int(day) in range(1, 32):
            return True
        else:
            return False
    else:
        if int(day) in range(1, 31) and month != "02":
            return True
        elif month == "02" and int(day) in range(1, 29):
            return True
        else:
            return False


str_date = input("Введите дату в формате DD.MM.YYYY: ")
print(date_exist(str_date))