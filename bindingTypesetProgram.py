"""
This program is to take any of my favorite online stories and format
 them into a typset so that I can print them and bind them.
"""
import sys
#from tkinter import Tk, filedialog
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from bs4 import BeautifulSoup



#I want to import an html file
#this only reads and returns the raw html content.
def html_file_read(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
    
"""#I want the html file to be written to a word document
def write_to_word_doc(content, output_path):
    document = Document() #create a new document
    document.add_paragraph(content) #add the content to the document
    document.save(output_path)#save the output in the document
    return document

#I want a justified alignment
def paragraph_format(document, content, output_path):
    paragraph = document.add_paragraph("This is a formatted paragraph.")
    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFIED # Justified align
    paragraph_format = paragraph.paragraph_format
    paragraph_format.left_indent = Inches(0.5) # Indent"""


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <html_file>")
    else:
        html_path = sys.argv[1]
        html_content = html_file_read(html_path) #get the raw html
        soup = BeautifulSoup(html_content, 'html.parser') #use beautiful soup to parse the html

        #find the chapters in the html
        story_divs = soup.find("div", {"id": "chapters"})
        #find the paragraphs in the chapters
        if story_divs:
            paragraphs = story_divs.find_all("p") #find the paragraphs
            for p in paragraphs: # for the paragraphs found
                   print(p.get_text())#print all the found paragraphs
         

        #output_path = 'output.docx'
        #write_to_word_doc(html_content, output_path)
        #print("HTML content has been written to {output_path}")
        #print(soup)


#I want it in landscape
"""def landscape_mode():
    section = document.sections[-1]
    section.orientation = WD_ORIENT.LANDSCAPE"""


# Margins of at least half an inch all around 

# font in Garamond

# font size in 11

# save it as a word document
