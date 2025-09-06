"""
This program is to take any of my favorite online stories and format
 them into a typset so that I can print them and bind them.
"""
import sys
from docx import Document
from bs4 import BeautifulSoup
from docx.enum.section import WD_ORIENT
from docx.shared import Inches, Pt
# from docx.enum.text import WD_ALIGN_PARAGRAPH
#from tkinter import Tk, filedialog

#I want to import an html file
#this only reads and returns the raw html content.
def html_file_read(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def set_landscape_and_margins(document):
    section = document.sections[0]    #define the section. There is usually only on according to https://python-docx.readthedocs.io/en/latest/user/sections.html

    section.orientation = WD_ORIENT.LANDSCAPE   #set the section to landscape mode

    #match the hieght and width to the landscape layout
    new_width, new_height = section.page_height, section.page_width
    section.page_width = new_width
    section.page_height = new_height
    section.orientation, section.page_width, section.page_height #(LANDSCAPE (1), 10058400, 7772400)

    #Adjust margins 
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)



    
#I want the html file to be written to a word document
def write_to_word_doc(diff_content_blocks, output_path):
    document = Document()   #create a new document

    set_landscape_and_margins(document)


    for blocks in diff_content_blocks:
        if blocks.name in ["h1", "h2"]:    #if it is a title
            heading = document.add_paragraph(blocks.get_text()) #get teh text
            heading.style  = 'Heading 1' if blocks.name == 'h1' else 'Heading 2' #give it a book title style if the name is a h1 tag and Strong if it is an h2 tag
            
        # if it is a paragraph`
        elif blocks.name == 'p':
            document.add_paragraph(blocks.get_text())    #add the text in the paragraphs

    document.save(output_path)  #save the text in the output in the document
    return document

#where all the magic happens
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <html_file>")
    else:
        html_path = sys.argv[1]
        html_content = html_file_read(html_path) #get the raw html
        soup = BeautifulSoup(html_content, 'html.parser') #use beautiful soup to parse the html

       #This is the filter
       #find the chapters in the html
        story_divs = soup.find("div", {"id": "chapters"})
        #find the paragraphs in the chapters
        if story_divs:
            diff_content_blocks = story_divs.find_all(["h1", "h2","p"]) #find the headings 11 headings 2, and paragraphs
            # for p in paragraphs: # for the paragraphs found
            #        print(p.get_text())#print all the found paragraphs
        else:
            print("could not find story content! :(")
            diff_content_blocks = [] # a fallback
         
        #write to the word doc
        output_path = 'output.docx'
        write_to_word_doc(diff_content_blocks, output_path)
        print("HTML content has been written to {output_path}")

#I want it in landscape
"""def landscape_mode():
    section = document.sections[-1]
    section.orientation = WD_ORIENT.LANDSCAPE"""

"""#I want a justified alignment
def paragraph_format(document, content, output_path):
    paragraph = document.add_paragraph("This is a formatted paragraph.")
    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFIED # Justified align
    paragraph_format = paragraph.paragraph_format
    paragraph_format.left_indent = Inches(0.5) # Indent
"""


# Margins of at least half an inch all around 

# font in Garamond

# font size in 11

# save it as a word document
