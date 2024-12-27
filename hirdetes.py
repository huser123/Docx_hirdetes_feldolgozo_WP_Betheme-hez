# Hirdetés elválasztó kezelő WP BeTheeme-hez

import os
from docx import Document

def clear_screen():
    """Clears the console screen based on the operating system."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux and macOS
        os.system('clear')

def list_docx_files():
    """List all .docx files in the current directory."""
    files = [f for f in os.listdir(os.getcwd()) if f.endswith(".docx")]
    return files

def process_docx(file_path):
    """Process the selected .docx file."""
    doc = Document(file_path)
    modified_content = []

    for paragraph in doc.paragraphs:
        # Remove 'IDEIS' and add the modified text
        if "IDEIS" in paragraph.text:
            modified_text = paragraph.text.replace("IDEIS", "").strip()
            if modified_text:
                modified_content.append(modified_text)
            modified_content.append("\n[hr height=30 style=default line=default themecolor=1]")
        else:
            modified_content.append(paragraph.text)

    # Print the modified content to the terminal
    print("\nProcessed Content:\n")
    for line in modified_content:
        print(line)

def main():
    # Clear the screen at the start
    clear_screen()

    # List all .docx files in the current directory
    docx_files = list_docx_files()

    if not docx_files:
        print("No .docx files found in the current directory.")
        return

    # Display the files with numbers
    print("Available .docx files:\n")
    for i, file in enumerate(docx_files, start=1):
        print(f"{i}. {file}")

    # Ask the user to select a file
    while True:
        try:
            choice = int(input("\nWhich file should I process? (Enter the number): "))
            if 1 <= choice <= len(docx_files):
                break
            else:
                print(f"Please enter a number between 1 and {len(docx_files)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Process the selected file
    selected_file = docx_files[choice - 1]
    print(f"\nProcessing: {selected_file}\n")
    process_docx(selected_file)

if __name__ == "__main__":
    main()
