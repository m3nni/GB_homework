"""
Задание 1
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок
под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные
о вложенных папках и файлах (добавлять детали)?
"""

import os

folder_structure = {
    'my_project': [
        {
            'settings': [{'bar': [], 'house': [{'gross': []}]}],
            'mainapp': [{'key_house': []}],
            'adminapp': [],
            'authapp': []
        }
    ]
}


def starter(path, structure):

    for folder, fold_in in structure.items():

        lesson_path = os.path.join(path, folder)

        if not os.path.exists(lesson_path):
            os.mkdir(lesson_path)

        if len(fold_in) > 0:
            for fold in fold_in:
                starter(lesson_path, fold)


if __name__ == '__main__':

    starter(os.getcwd(), structure=folder_structure)
