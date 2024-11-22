import argparse
from pathlib import Path
import shutil

from datetime import datetime

import os


filetypes = {
        "Documents": [".pdf", ".docx", ".pptx", ".rtf", ".txt", ".xlsx", ".csv"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Videos": [".mp4", ".mkv", ".webm", ".avi", ".mov"],
        "Music": [".mp3", "wav"]
    }

def organize_by_type(directory):
    for file in Path(directory).iterdir():
        if file.is_file():
            for folder, extensions in filetypes.items():
                if file.suffix in extensions:
                    target_folder = Path(directory) / folder
                    target_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(target_folder))
                    print(f"Moved {file} to folder {target_folder}\n")
                    break
            else:
                target_folder = Path(directory) / "Other"
                target_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(target_folder))
                print(f"Moved {file} to folder {target_folder}\n")


def organize_by_date(directory):
    for file in Path(directory).iterdir():
        if file.is_file():
            modification_time = file.stat().st_mtime
            folder_name = Path(directory) / datetime.fromtimestamp(modification_time).strftime("%Y-%m")
            folder_name.mkdir(exist_ok=True)
            shutil.move(str(file), str(folder_name))
            print(f"Moved {file} to folder {folder_name}\n")


def main():
    parser = argparse.ArgumentParser(description = "File Organizer CLI")
    parser.add_argument("directory", type = str, help = "The directory to be organized")
    parser.add_argument("type", type = str, choices = ["type", "date"], help = "Mode of organization")
    args = parser.parse_args()

    if not os.path.exists(args.directory):
        print("Enter a valid directory name")
        return

    if args.type == "type":
        organize_by_type(args.directory)
    else:
        organize_by_date(args.directory)



if __name__ == "__main__":
    main()