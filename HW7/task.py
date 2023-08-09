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

