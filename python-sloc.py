import os, tkinter, mimetypes
from os import walk
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

print("Please select the directory you'd like to analyze: ")

path = filedialog.askdirectory()
lines = 0

def count_lines(file):
    return len(file.readlines())

def walk_path(path):
    global lines
    for (dirpath, dirnames, filenames) in walk(path):
        for name in filenames:
            filepath = os.path.join(dirpath, name)
            file = open(filepath, 'r')
            print(filepath, end="")
            countedLines = count_lines(file)
            lines += countedLines
            print(" Lines: " + str(countedLines))

walk_path(path)
print("This folder contains " + str(lines) + " lines.")
