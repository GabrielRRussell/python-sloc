import os, tkinter, mimetypes
from os import walk
from tkinter import filedialog

# Setup a hidden Tkinter window for easy directory selection
root = tkinter.Tk()
root.withdraw()
print("Please select the directory you'd like to analyze: ")
path = filedialog.askdirectory()

# Define some variables to use.
# Lines is total lines in folder
# Files is total files in folder
# highestCount is the highest line count
# highestPath is the path to the file that has the highest line count
lines = 0
files = 0
highestCount = 0
highestPath = ""

# .readlines() will return the number of lines in a file
def count_lines(file):
    return len(file.readlines())

def walk_path(path):
    global lines
    global files
    global highestCount
    global highestPath
    # Walk through each folder, file, in given path
    for (dirpath, dirnames, filenames) in walk(path):
        for name in filenames:
            # Get the file path by joining the directory and file name
            filepath = os.path.join(dirpath, name)
            # Open the file, then try to read lines. If it's a non-text format,
            # then readlines() will fail, so I will not count that file
            file = open(filepath, 'r')
            try:
                # This code only executes for text files
                countedLines = count_lines(file)
                lines += countedLines
                # Empty files shouldn't be counted
                if (countedLines > 0):
                    files += 1
                    print(filepath, "Lines: " + str(countedLines))
                # Set the record for largest file
                if (countedLines > highestCount):
                    highestCount = countedLines
                    highestPath = filepath
            # Don't need to handle any exceptions that occur
            except Exception:
                pass

walk_path(path)
average = lines / files
print("This folder contains " + str(lines) + " lines.")
print("The average file contains " + str(average) + " lines of code.")
print("The file with the most code is " + highestPath + " with", str(highestCount), "lines of code.")
