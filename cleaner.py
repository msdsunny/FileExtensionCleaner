#!/usr/bin/env python3

from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import os
import shutil
from pathlib import Path
from tkinter import filedialog,messagebox
from pathlib import Path

directory = ""  # customize directory name 
ext = ""        # extension of the file
dir_name = ""   # source folder path

def uploadFile():
    root.filename = filedialog.askdirectory() #askopenfilename(filetypes= (("how code files",".txt"),("All files","*.*")))
    global dir_name
    dirname = Path(root.filename)
    return dirname
    
def filter_files(directory_path, extension):
    files_in_directory = os.listdir(directory_path)
    return [file for file in files_in_directory if file.endswith(f".{extension}")]

def copy_files(directory_path, files, extension):
    # if cutomize name given generate target directory by that name
    if(len(directory) > 0):
    	destination_dir = os.path.join(directory_path, f"{directory}")
    else:
    	destination_dir = os.path.join(directory_path, f"{extension}_files")
    os.makedirs(destination_dir, exist_ok=True)
    for file in files:
        try:
            source_path = os.path.join(directory_path, file)
            shutil.move(source_path, destination_dir)
        except Exception as e:
            print(f"Failed to move {file}. Error: {str(e)}")
    return destination_dir

def process_files(): 
    global directory 
    global ext
    directory = extInput1.get()
    ext = extInput2.get()
 
    dir_name = uploadFile()
    filtered_files = filter_files(dir_name, ext)
    copied_files_dir = copy_files(dir_name, filtered_files, ext)
    print(f"Files in directory: {os.listdir(dir_name)}")
    print(f"Filtered files: {filtered_files}")
    print(f"Copied files directory: {copied_files_dir}")
    messagebox.showinfo("File Copier Extension", "Files copied successfully!")
    

root = Tk()

root.title("File Type Organizer")
root.minsize(300,400)

# set the font and size for the label
bold_font = ('TkDefaultFont', 10, 'bold')

# create a label with text 'File Type Organizer' and font 'bold_font'
label = Label(root, text='Version: 1.0.0', font=bold_font)

# add 20% margin top to the label
label.pack(pady=(int(root.winfo_screenheight() * 0.02), 0))

extLabel = Label(root,text="Enter a custom name for the destination directory",font=("Calibri",14))
extLabel.pack(padx=20, pady=20)

extInput1 = Entry(root,text="Enter dir Name",font=("Calibri",14))
extInput1.pack()


extLabel = Label(root,text="Enter File Extension",font=("Calibri",14))
extLabel.pack(padx=20, pady=20)

extInput2 = Entry(root,text="Enter Extension:",textvariable=ext,font=("Calibri",14))
extInput2.pack()


extLabel = Label(root,text="Choose source directory",font=("Calibri",14))
extLabel.pack(padx=20, pady=20)

process_button = Button(root, text="Copy Files", command=process_files)
process_button.pack()

print(dir_name)
root.mainloop()
