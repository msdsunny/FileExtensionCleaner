from tkinter import *
import os
import shutil
from pathlib import Path
from tkinter import filedialog,messagebox
from pathlib import Path

def uploadFile():
    root.filename = filedialog.askdirectory() #askopenfilename(filetypes= (("how code files",".txt"),("All files","*.*")))
    global dir_name
    dirname = Path(root.filename)


root = Tk()
root.title("File Copier Extension")
root.minsize(300,400)

directory = ""
ext = ""
dir_name = ""


extLabel = Label(root,text="Enter Directory Name",font=("Calibri",20))
extLabel.pack(padx=20, pady=20)

extInput = Entry(root,text="Enter dir Name",font=("Calibri",20))
extInput.pack()

extLabel = Label(root,text="Enter File Extension",font=("Calibri",20))
extLabel.pack(padx=20, pady=20)

extInput = Entry(root,text="Enter Extension:",textvariable=ext,font=("Calibri",20))
extInput.pack()

extLabel = Label(root,text="Set File Directory",font=("Calibri",20))
extLabel.pack(padx=20, pady=20)

directory = Button(root, text="Choose Path",command=uploadFile)
directory.pack()

Path(dir_name)

files_in_directory = os.listdir(Path(dir_name))
filtered_files = [file for file in files_in_directory if file.endswith(f".{extInput.get()}")]

for file in filtered_files:
    # get all but the last 8 characters to remove
    # the index number and extension
    dir_name = os.path.join(directory,f"{directory.get()}")
    print(f'dir_name: {dir_name}')

    dir_path = os.path.join(directory, file)
    print(f'Source dir_path: {dir_path}')

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    if os.path.exists(dir_path):
        file_path = dir_path
        print(f'file_path: {file_path}')

    # move files into created directory
    shutil.move(dir_path,dir_name)
    
print(dir_name)
root.mainloop()
