"""
This program is to take any of my favorite online stories and format
 them into a typset so that I can print them and bind them.
"""
import sys
#from tkinter import Tk, filedialog
from docx import Document
from docx.enum.section import WD_ORIENT


#I want to import an html file
def html_file_read(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
#I want the html file to be written to a word document
def write_to_word_doc(content, output_path):
    document = Document() #create a new document
    document.add_paragraph(content) #add the content to the document
    document.save(output_path)#save the output in the document

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <html_file>")

    else:
        html_path = sys.argv[1]
        html_content = html_file_read(html_path)
        output_path = 'output.dock'
        write_to_word_doc(html_content, output_path)
        print("HTML content has been written to {output_path}")


#I want it in landscape
"""def landscape_mode():
    section = document.sections[-1]
    section.orientation = WD_ORIENT.LANDSCAPE"""

#I want a justified alignment

# Margins of at least half an inch all around 

# font in Garamond

# font size in 11

# save it as a word document
