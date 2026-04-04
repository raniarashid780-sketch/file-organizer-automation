from pathlib import Path

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

if __name__ == "__main__":
    base = Path.home() / "Downloads"
    result = create_destination(base, "Images", "2025-March")
    print(result)
    print(get_file_category(".jpg"))
    print(get_file_category(".pdf"))
    print(get_file_category(".mp3"))
    print(get_file_category(".xyz"))

