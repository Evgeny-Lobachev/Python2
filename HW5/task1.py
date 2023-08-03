import os

def elems_path(my_path):
    return os.path.split(my_path)[0], *os.path.split(my_path)[-1].split('.')

print(elems_path('C:\GeekBrains\Python_part2\HW\Python2\HW5\task1.py'))