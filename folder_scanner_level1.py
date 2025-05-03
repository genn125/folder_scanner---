import os
from datetime import datetime
# import subprocess
# import json
# import sys
# from pathlib import Path

AUDIO_EXTENSIONS = {'.mp3', '.flac', '.wav', '.ogg', '.m4a', '.aac', '.wma'}
# 1 Проверяет наличие музыкальных файлов в папках
def has_music_files(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if os.path.splitext(file)[1].lower() in AUDIO_EXTENSIONS:
                return True
    return False
# 2 Сканирует ТОЛЬКО папки с музыкой

def scan_music_folders(folder_path):
    music_folders = set()
    with os.scandir(folder_path) as entries:
        for entry in entries:
            if has_music_files(entry):
                music_folders.add(entry)

    return music_folders
# 3 Сортирует и сохраняет папки в файл
def sorted_save_folders(music_folders,output_file):
    sorted_folders = sorted(music_folders, key=lambda x: x.name)
    #sorted_folders = sorted(music_folders, key=lambda x: x.stat().st_mtime)  # по времени изменения
    with open(output_file, "w", encoding="utf-8") as fa:
        fa.write(f"Мои группы дата создания списка: ({datetime.now().strftime('%H:%M %d-%B-%y')})")
        for folder in sorted_folders:
            fa.write(f"\n{folder.name}")

def main():
    print("\n===== Сканирование папок 1 уровня =====")
    folder_path = r"C:\Users\genn1\Downloads"#"/storage/emulated/0/Music"#
    output_file = f"Сканер_папок_1_уровня ({datetime.now().strftime('%H_%M  %d-%B-%y')}).txt"

    """Проверяем на наличие музыкальных файлов"""
    #has_music_files(folder_path)
    """Сканирует только папки с музыкой"""
    music_folders = scan_music_folders(folder_path)
    """Сортирует и пишет в файл папки с музыкой"""
    sorted_save_folders(music_folders, output_file)

    print(f"\nОтсортированная структура сохранена в файле\n {output_file}")
    print(f"\nПример содержимого:\n")
    with open(output_file, 'r', encoding='utf-8') as f:
        n = 200 #печатаем первые n символов из созданного файла
        print(f.read(n))

if __name__ == "__main__":
    print("\nСКРИПТ ЗАПУСКАЕТСЯ НАПРЯМУЮ")
    main()
else:
    main()
