"""
This program is to take any of my favorite online stories and format
 them into a typset so that I can print them and bind them.
"""
import sys
from tkinter import Tk, filedialog

#I want to import an html file
def html_file_read(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Useage: python your_script.py <html_file>")

    else:
        html_path = sys.argv[1]
        html_content = html_file_read(html_path)
        print(html_content)

#I want it in landscape

#I want a justified alignment

# Margins of at least half an inch all around 

# font in Garamond

# font size in 11

# save it as a word document
