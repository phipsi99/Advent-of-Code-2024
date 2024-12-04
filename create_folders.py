from pathlib import Path

# Define the template folder path and the destination path
template_folder = Path(__file__).parent / 'templates'
destination_path = Path(__file__).parent

# Create the destination folders and copy files
for i in range(4, 26):
    # Create the folder name with leading zero if necessary
    folder_name = f'{i:02d}'

    # Create the destination folder if it doesn't exist
    destination_folder = destination_path / folder_name
    destination_folder.mkdir(parents=True, exist_ok=True)

    # Copy files from the template folder to the destination folder
    for source_file in template_folder.iterdir():
        if source_file.is_file():
            main = source_file.read_text()
            if source_file.name == "main.py":
                main = main.replace("{XX}", folder_name)
            destination_file = destination_folder / source_file.name
            destination_file.write_text(main)
            print(f'File {source_file.name} copied to folder {folder_name}')

print('All files copied successfully.')