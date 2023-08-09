import os

dict_folder = {'mpeg': 'Video', 'mp4': 'Video', 'flv': 'Video',
               'doc': 'Text Documents', 'txt': 'Text Documents', 'pdf': 'Text Documents',
               'png': 'Images', 'rav': 'Images','psd': 'Images', 'jpg': 'Images',
               }


def sort_files_for_dir(path=""):
    if path != "":
        os.chdir(path)

    list_files = os.listdir()
    for item in list_files:
        if os.path.isfile(item):
            *_, exp_file = item.split('.')
            name_folder = dict_folder.get(exp_file)
            if name_folder is not None:
                if not os.path.exists(name_folder):
                    os.mkdir(name_folder)
                os.replace(item, f'{name_folder}//{item}')

'''part2'''

def group_rename_files(path='', postfix='', count_digit=4, exp_old='txt', exp_new='', prefix=(1, 3)):
    list_files = os.listdir()
    curr_count = 0
    for item in list_files:
        if os.path.isfile(item):
            name_file, exp_file = item.split('.')
            if exp_file == exp_old:
                curr_count += 1
                spam = str(format(curr_count, f'0>{count_digit}'))
                eggs = exp_file if exp_new == "" else exp_new
                new_name = f'{name_file[prefix[0]:prefix[1] + 1]}{postfix}{spam}.{eggs}'

                os.rename(item, new_name)


how_task = input("Какую функцию запустить?\n1 - Сортировка\n2 - Групповое переименование\nВведите 1 или 2: ")
if how_task == '1':
    sort_files_for_dir(path="")
elif how_task == '2':
    group_rename_files(path=str(os.chdir('Text Documents')), postfix='_RE_', exp_old='txt', exp_new='doc')