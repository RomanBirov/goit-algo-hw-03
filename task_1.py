import os
import shutil
import argparse


def copy_and_sort_files(src_dir, dist_dir):
    
    try:
        items = os.listdir(src_dir)
    except PermissionError:
        print(f"Немає доступу до директорії: {src_dir}")
        return
    except FileNotFoundError:
        print(f"Директорію не знайдено: {src_dir}")
        return

    for item in items:
        full_path = os.path.join(src_dir, item)

        # Якщо директорія — рекурсія
        if os.path.isdir(full_path):
            copy_and_sort_files(full_path, dist_dir)

        # Якщо файл — копіюємо
        else:
            ext = os.path.splitext(item)[1].lower().replace(".", "")
            if not ext:
                ext = "no_extension"

            target_folder = os.path.join(dist_dir, ext)
            os.makedirs(target_folder, exist_ok=True)

            try:
                shutil.copy2(full_path, target_folder)
                print(f"📁 Скопійовано: {item} → {ext}")
            except Exception as e:
                print(f"Помилка копіювання {item}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Recursive file sorter")
    parser.add_argument("src", help="Source directory")
    parser.add_argument("dist", nargs="?", default="dist",
                        help="Destination directory (default: dist)")
    args = parser.parse_args()

    src_dir = args.src
    dist_dir = args.dist

    if not os.path.exists(src_dir):
        print("Вихідна директорія не існує!")
        return

    os.makedirs(dist_dir, exist_ok=True)

    print(f"Старт сортування...")
    copy_and_sort_files(src_dir, dist_dir)
    print(f"Готово! Файли скопійовано в '{dist_dir}'")


if __name__ == "__main__":
    main()
