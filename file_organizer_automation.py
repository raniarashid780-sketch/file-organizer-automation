from pathlib import Path

def create_destination(base, file_type_folder, date_folder):
    destination = base / file_type_folder / date_folder
    destination.mkdir(parents=True, exist_ok=True)
    return destination

if __name__ == "__main__":
    base = Path.home() / "Downloads"
    result = create_destination(base, "Images", "2025-March")
    print(result)
