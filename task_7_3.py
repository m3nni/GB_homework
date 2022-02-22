"""
Задание 3
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены
в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django.
"""

import os
import shutil


paths = {}
paths_dirs = []
base_dir = 'my_project'

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            template = os.path.join(*root.split(os.sep)[-1:])
            if template not in paths:
                paths_dirs.append(os.path.join(base_dir, 'templates', template))
            path_to_html = os.path.join(root, file)
            paths.update({path_to_html: os.path.join(base_dir, 'templates', template, file)})

if not os.path.exists(os.path.join(base_dir, 'templates')):
    os.mkdir(os.path.join(base_dir, 'templates'))

for d in paths_dirs:
    if not os.path.exists(d):
        os.mkdir(d)

for old, new in paths.items():
    if not os.path.exists(new):
        shutil.copy2(old, new)
