from pathlib import Path
import os
import datetime
import shutil

def create_destination(base, file_type_folder, date_folder):
    destination = base / file_type_folder / date_folder
    destination.mkdir(parents=True, exist_ok=True)
    return destination

def get_file_category(extension):
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".aac"]
    }
    for category, extensions in categories.items():
        if extension in extensions:
            return category
    return "Others"

def get_date_folder(file_path):
    timestamp = os.path.getmtime(file_path)
    date = datetime.datetime.fromtimestamp(timestamp)
    return f"{date.year}-{date.strftime('%B')}"

def organize_files(folder):
    for file in folder.glob("*"):
        if file.is_file():
            extension = file.suffix.lower()
            category = get_file_category(extension)
            date = get_date_folder(file)
            destination = create_destination(folder, category, date)
            try:
                shutil.move(file, destination / file.name)
                print(f"Moved: {file.name} → {destination}")
            except Exception as e:
                print(f"Skipped {file.name}: {e}")

def main():
    organize_files(Path.home() / "Downloads")
    organize_files(Path.home() / "Desktop")
    print("Done! Your folders are organized.")

if __name__ == "__main__":
    main()
    
