import os

def print_directory_structure(base_path, excluded_dirs=None, indent=0):
    if excluded_dirs is None:
        excluded_dirs = {'.venv', '__pycache__', 'tasks', '.git'}
    
    try:
        entries = sorted(os.listdir(base_path))
    except PermissionError:
        print(" " * indent + f"[Permission Denied] {base_path}")
        return

    for entry in entries:
        entry_path = os.path.join(base_path, entry)
        if os.path.isdir(entry_path):
            if entry in excluded_dirs:
                continue
            print(" " * indent + f"{entry}/")
            print_directory_structure(entry_path, excluded_dirs, indent + 4)
        else:
            print(" " * indent + entry)

# Usage
if __name__ == "__main__":
    directory_to_scan = "C:/Users/Osamih/Desktop/VS Code Projects/newsletter-gen"  # Change to your desired base directory
    print_directory_structure(directory_to_scan)
