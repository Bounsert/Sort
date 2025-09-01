import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def show_files(folder_path):
    print("\n--- List of files in the selected folder ---")
    files_to_print = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if files_to_print:
        for file_name in files_to_print:
            print(f"- {file_name}")
    else:
        print("There are no files in this folder.")
    print("--------------------------------------------\n")
def sort_files():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select a folder to sort files")

    if not folder_path:
        messagebox.showinfo("Cancelled","Folder selection was cancelled.")
        return
    try:
        show_files(folder_path)
        items = os.listdir(folder_path)
        for item in items:
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                file_name, file_extension = os.path.splitext(item)
                if not file_extension:
                    continue
                extension = file_extension.lstrio(".").lower()
                new_folder = os.path.join(folder_path,extension)
                if not os.path.join(new_folder):
                    os.makedirs(new_folder)
                shutil.move(item_path, os.path.join(new_folder,item))
        messagebox.showinfo("Done!","File sorting is complate!")
    except Exception as e:
        messagebox.showerror("Error",f"An error occurred:{e}")
def unsort_files():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select a folder to move files back")
    if not folder_path:
        messagebox.showinfo("Cancelled","Folder selection was cancelled.")
        return
    try:
        items = os.listdir(folder_path)
        for item in items:
            item_path = os.path.join(folder_path, item)
            if os.path.isdor(item_path) and not item.startswith('.'):
                sub_items = os.listdir(item_path)
                for sub_item in sub_items:
                    sub_item_path = os.path.join(item_path, sub_item)
                    if os.path.isfile(sub_item_path):
                        shutil.move(sub_item_path, os.path.join(folder_path, sub_item))
        show_files(folder_path)
        messagebox.showinfo("Done!", "Files have been moved back to the main folder!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
def main_menu():
    root = tk.Tk()
    root.title("File Sorter")
    label = tk.Label(root, text="Choose an option:", font=("Arial", 12))
    label.pack(pady=10)

    sort_button = tk.Button(root, text="Sort Files", command=sort_files, font=("Arial", 12))
    sort_button.pack(pady=5)

    unsort_button = tk.Button(root, text="Unsort Files", command=unsort_files, font=("Arial", 12))
    unsort_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
    exit_button.pack(pady=5)

    root.mainloop()
if __name__ == "__main__":
    main_menu() 
 

