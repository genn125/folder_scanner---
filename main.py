import importlib
import sys
import os
from pathlib import Path

# ==============================================
# Настройки для корректной работы в .exe
# ==============================================

# Определяем базовую директорию
if getattr(sys, 'frozen', False):
    # Режим .exe
    BASE_DIR = Path(sys.executable).parent
else:
    # Режим разработки
    BASE_DIR = Path(__file__).parent

# Добавляем папку с программой в пути поиска модулей
sys.path.append(str(BASE_DIR))


# ==============================================
# Безопасный ввод данных
# ==============================================

def safe_input(prompt):
    """Функция для безопасного ввода в .exe и обычном режиме"""
    try:
        return input(prompt)
    except:
        try:
            return sys.__stdin__.readline().strip()
        except:
            return "0"  # Значение по умолчанию при ошибке


# ==============================================
# Словарь соответствия выбора и модулей
# ==============================================
# Важно: используйте латинские имена для модулей!
MODULES_MAP = {
    '1': 'folder_scanner_level1',  # Было: Сканер_папок_1_уровня
    '2': 'folder_scanner_no_files',  # Было: Сканер_папок_без_файлов
    '3': 'folder_scanner_with_files'  # Было: Сканер_папок_с_файлами
}


# ==============================================
# Основной цикл программы
# ==============================================

def main():
    while True:
        # Получаем выбор пользователя
        choice = safe_input("Введите 1,2,3 или 0 для выхода: ").strip()
        print("Вы ввели:", choice)

        # Выход из программы
        if choice == '0':
            print('Выход')
            break

        # Получаем имя модуля из словаря
        module_name = MODULES_MAP.get(choice)

        if not module_name:
            print("\nНеизвестный выбор!\n")
            continue


        try:
            # Динамический импорт модуля
            module = importlib.import_module(module_name)
            print(f"\nИмпортирован модуль {module_name}")

            # Здесь можно вызвать нужные функции из модуля
            # Например: module.main_function()

        except ImportError as e:
            print(f"\nОшибка импорта модуля {module_name}: {e}")
            print("Убедитесь, что:")
            print(f"1. Файл {module_name}.py существует")
            print("2. Модуль указан при сборке")
            print("3. Нет проблем с путями")


if __name__ == "__main__":
    main()



# import importlib
# import sys
# #from past.builtins import raw_input
#
# while True:
#     #choice = sys.stdin.readline('hhhhhhh')
#     def safe_input(prompt):
#         try:
#             return input(prompt)  # Пробуем обычный input()
#         except:
#             try:
#                 return sys.__stdin__.readline()  # Пробуем резервный stdin
#             except:
#                 return "default_value"  # Возвращаем значение по умолчанию
#
#     choice = safe_input("Введите 1,2,3 или 0 для выхода: ")
#     print("Вы ввели:", choice)
#
#     module_name = (
#         'Сканер_папок_1_уровня' if choice == '1' else
#         'Сканер_папок_без_файлов' if choice == '2' else
#         'Сканер_папок_с_файлами' if choice == '3' else
#         None
#     )
#     if choice == '0':
#                 print('Выход')
#                 break
#     if not module_name:
#         print("\nНеизвестный выбор!\n")
#
#     else:
#         module = importlib.import_module(module_name)
#         print(f"\nИмпортирован модуль {module_name}")
        
   
        