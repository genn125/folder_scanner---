import os
from datetime import datetime
# import sys
# import subprocess
# import json
# from pathlib import Path

AUDIO_EXTENSIONS = {'.mp3', '.flac', '.wav', '.ogg', '.m4a', '.aac', '.wma'}
# 1 Проверяет наличие музыкальных файлов в папках
def has_music_files(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if os.path.splitext(file)[1].lower() in AUDIO_EXTENSIONS:
                return True
    return False
# 2 Рекурсивно получает отсортированную структуру папок
def get_sorted_folder_structure(root_path):
    structure = [] #  Список папок и сортировка по имени
    items = sorted(os.listdir(root_path), key=lambda x: x.lower())
    for item in items:
        item_path = os.path.join(root_path, item)
        if os.path.isdir(item_path) and not item.startswith('.'):
           if has_music_files(item_path): # Для каждой папки получить её подпапки (рекурсивно)
                subfolders = get_sorted_folder_structure(item_path)
                structure.append({
                        'name': item,
                        'path': item_path,
                        'subfolders': subfolders
                    })

    return structure

#3 Сохраняет отсортированную структуру в файл
def save_sorted_structure(structure, output_file, level=0):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Структура папок:\n\n")
        _write_structure_recursive(f, structure, level)



def _write_structure_recursive(f, structure, level):
    """Рекурсивно записать структуру папок с отступами."""
    for folder in structure:
        indent = "    |-->" * level
        f.write(f"{indent} {folder['name']}\n")
        if folder['subfolders']:
            _write_structure_recursive(f, folder['subfolders'], level + 1)

def main():
    print("\n---===== Сканирование папок без файлов =====---")
    target_dir = r"C:\Users\genn1\Downloads"#"/storage/emulated/0/Music"#
    output_file = f"Сканер_папок_без_файлов ({datetime.now().strftime('%H_%M  %d-%B-%y')}).txt"

    """Получить отсортированную структуру"""
    folder_structure = get_sorted_folder_structure(target_dir)
    
    """Сохранить в файл"""
    save_sorted_structure(folder_structure, output_file)

    print(f"\nОтсортированная структура сохранена в файле\n {output_file}")
    print("\nПример содержимого:\n")
    with open(output_file, 'r', encoding='utf-8') as f:
        n = 1000  # печатаем первые n символов из созданного файла
        print(f.read(n))

if __name__ == "__main__":
    print("\nСКРИПТ ЗАПУСКАЕТСЯ НАПРЯМУЮ\n")
    main()
else:
    main()
