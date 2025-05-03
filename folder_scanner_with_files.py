import os
from datetime import datetime
import sys
import subprocess
import json
from pathlib import Path

AUDIO_EXTENSIONS = {'.mp3', '.flac', '.wav', '.ogg', '.m4a', '.aac', '.wma'}
# 1 Проверяет наличие музыкальных файлов в папках
def has_music_files(folder_path):
    """Проверить наличие музыкальных файлов в папках"""
    for root, _, files in os.walk(folder_path):
        for file in files:
            if os.path.splitext(file)[1].lower() in AUDIO_EXTENSIONS:
                return True
    return False
# 2 Рекурсивно сканирует папку и сохраняет структуру с метаданными
def scan_directory(directory, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for root, dirs, files in os.walk(directory):
                level = root.replace(directory, "").count(os.sep)
                indent = "│   " * level
                # Папка
                f.write(f"{indent}│   ├─📁 {os.path.basename(root)}/\n")
                # Файлы
                for file in files:
                    filepath = os.path.join(root, file)
                    try:
                        stat = os.stat(filepath)
                        size = stat.st_size / 1024  # KB
                        #mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%d.%m.%Y %H:%M")
                        f.write(f"{indent}│   ├     📄 {file} ({size:.2f} KB)\n")
                    except OSError as e:
                        f.write(f"{indent}│  ├── ❌ {file} (ошибка: {e})\n")
        return True
    except Exception as e:
        print(f"Ошибка сканирования: {e}", file=sys.stderr)
        return False

def main():
    print("🔍 Глубокий сканер папок с файлами")
    target_dir = r'C:\Users\genn1\Downloads'#"/storage/emulated/0/Music"


    #3. Проверка
    if not os.path.isdir(target_dir):
        print(f"❌ Ошибка: Папка '{target_dir}' не найдена!", file=sys.stderr)
        sys.exit(1)

    # 4. Сканирование
    output_file = f"Сканер_папок_с_файлами ({datetime.now().strftime('%H_%M  %d-%B-%y')}).txt"
    print(f"Сканирую '{target_dir}'...")
    if scan_directory(target_dir, output_file):
        print(f"✅ Результат сохранён в '{output_file}'")
    else:
        print("❌ Сканирование завершено с ошибками", file=sys.stderr)


    print(f"\nОтсортированная структура сохранена в файле\n {output_file}")
    print("\nПример содержимого:\n")
    with open(output_file, 'r', encoding='utf-8') as f:
        n = 250  # печатаем первые n символов из созданного файла
        print(f.read(n))



if __name__ == "__main__":
    print("\nСКРИПТ ЗАПУСКАЕТСЯ НАПРЯМУЮ\n")
    main()
else:
    main()
