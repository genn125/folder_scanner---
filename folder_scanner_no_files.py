import os
from datetime import datetime
import sys
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

# 2 Сканирует ТОЛЬКО папки с музыкой
def scan_music_folders(folder_path):
    music_folders = []
    with os.scandir(folder_path) as entries:
        for entry in entries:
            if entry.is_dir() and has_music_files(entry.path):  # Проверяем, что это директория
                music_folders.append(entry.path)  # Добавляем путь в список
    return music_folders

# 3 Рекурсивно сканирует и сохраняет структуру с метаданными в файл
def scan_directory(music_folders, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"        Мои группы. \nДата создания списка: ({datetime.now().strftime('%H:%M %d-%B-%y')})\n\n")
            for folder in sorted(music_folders, key=lambda x: os.path.basename(x).lower()):  # Сортируем папки
                for root, _, files in os.walk(folder):
                    level = root.replace(folder, "").count(os.sep)
                    indent = "       " * level
                    # Папка
                    f.write(f"{indent}📁 {os.path.basename(root)}\n")
                    # # Файлы
                    # for file in files:
                    #     filepath = os.path.join(root, file)
                    #     try:
                    #         stat = os.stat(filepath)
                    #         size = stat.st_size / 1024  # KB
                    #         # mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%d.%m.%Y %H:%M")
                    #         f.write(f"{indent}       ──>📄 {file} ({size:.2f} KB)\n")
                    #     except OSError as e:
                    #         f.write(f"{indent}│  ├── ❌ {file} (ошибка: {e})\n")
        return True
    except Exception as e:
        print(f"Ошибка сканирования  1: {e}", file=sys.stderr)
        return False

def main():
    print("\n🔍---===== Сканирование папок без файлов =====---")
    folder_path = r
    
    output_file = f"Сканер папок БЕЗ файлов ({datetime.now().strftime('%H_%M  %d-%B-%y')}).txt"
    print(f"\nСканирую '{folder_path}'...")

    """Сканирует только папки с музыкой"""
    music_folders = scan_music_folders(folder_path)

    if music_folders:  # Проверяем, что найдены папки с музыкой
        if scan_directory(music_folders, output_file):
            print(f"✅ Результат сохранён в файл\n   '{output_file}'")
        else:
            print("❌ Сканирование завершено с ошибками", file=sys.stderr)
    else:
        print("⚠️ Не найдено папок с музыкой", file=sys.stderr)

    print("\nПример содержимого:\n")
    with open(output_file, 'r', encoding='utf-8') as f:
        n = 500  # печатаем первые n символов из созданного файла
        print(f.read(n))

if __name__ == "__main__":
    print("\nСКРИПТ ЗАПУСКАЕТСЯ НАПРЯМУЮ\n")
    main()
else:
    main()
