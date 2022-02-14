
"""
import os

folder = r'E:\pr\My_Work_Python\Test_l_7'
py_files = [item
            for item in os.listdir(folder)
            if item.lower().endswith('.py')]
print(py_files)
# ['abc.py', 'client.py', 'client_exceptions.py', 'client_proto.py', ...

"""
"""
Примечание: библиотека aiohttp очень часто используется в проектах — р
екомендуем установить её в систему и поработать самостоятельно в будущем.

Вторая особенность — мы получаем только имена сущностей, а не пути к ним. 
Придется воссоздавать путь при помощи функции join() из модуля os.path:

из модуля os.path:  isfile(), isdir() или из os: stat().
"""
"""
import os
folder = r'E:\pr\Test\venv\Lib\site-packages\django'
django_dirs = [item
               for item in os.listdir(folder)
               if os.path.isdir(os.path.join(folder, item))]
print(django_dirs)
"""

import random
'''
folder = 'E:\pr\My_Work_Python\Test_l_7'
letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
for _ in range(10 ** 3):
   f_name = ''.join(random.sample(letters, random.randint(5, 10)))
   f_content = bytes(random.randint(0, 255)
                     for _ in range(random.randrange(10 ** 5)))
   with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
       f.write(f_content)
'''

'''
from time import perf_counter

folder = 'E:\pr\My_Work_Python\Test_l_7'
start = perf_counter()
size_threshold = 15 * 2 ** 10
small_files = [item
              for item in os.listdir(folder)
              if os.stat(os.path.join(folder, item)).st_size < size_threshold]
print(len(small_files), perf_counter() - start)
# 155 2.271335837

from time import perf_counter
size_threshold = 15 * 2 ** 10
start = perf_counter()
small_files_2 = [item.name
                 for item in os.scandir(folder)
                 if item.stat().st_size < size_threshold]
print(len(small_files_2), perf_counter() - start)
print(small_files == small_files_2)
# 155 0.0739816499999999
# True

import os
from time import perf_counter

folder = 'some_data'
start = perf_counter()
all_files = [item
              for item in os.listdir(folder)]
print(len(all_files), perf_counter() - start)
# 1000 0.056053622000000025
start = perf_counter()
all_files_2 = [item.name
                for item in os.scandir(folder)]
print(len(all_files_2), perf_counter() - start)
print(all_files == all_files_2)
# 1000 0.04480954299999995
# True
'''
'''
Полезные функции модуля os.path
В модуле os.path есть ещё много полезных функций для работы с файловой системой:
abspath() — возвращает абсолютный путь;
basename() — возвращает имя файла из абсолютного или относительного пути;
dirname() — возвращает имя (путь) папки, в которой расположен файл;
split() — делит путь к файлу на путь к папке и имя файла (заменяет вызов двух предыдущих функций);
relpath() — определяет путь к файлу относительно другой папки, не обращается к реальной файловой системе, 
чисто вычисления (полезна при сохранении путей к файлам в базе данных относительно заданного корня);

join() — склеивает путь из частей (надеемся, вы не делаете это через строки!);
exists() — проверяет существование объекта файловой системы.
'''
"""
import os

root = r'E:\pr\Test\venv\Lib\site-packages\django'
folder = r'E:\pr\Test\venv\Lib\site-packages\django\contrib\admin'
django_admin_dirs = [
   os.path.relpath(item, root)
   for item in os.scandir(folder)
   if item.is_dir() and not item.name.startswith('_')
]
print(django_admin_dirs)
# ['contrib\\admin\\locale', 'contrib\\admin\\migrations',
# 'contrib\\admin\\static', 'contrib\\admin\\templates',
# 'contrib\\admin\\templatetags', 'contrib\\admin\\views']
"""
import os

# определяем путь до базовой директории, относительного которой будет работать
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

# получаем список файлов и папок в директориях
print(os.listdir(BASE_DIR))
parent_dir = os.path.dirname(BASE_DIR)
#print(os.listdir(parent_dir))
#print([filename for filename in os.listdir(BASE_DIR) if filename.endswith('.py')])