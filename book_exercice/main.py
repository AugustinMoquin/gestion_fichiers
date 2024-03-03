import re
from word_count import *
from image_proccessing import *
from display_text import *
from pivot_image import *
from doc_word import *

def extract_title(text):
    # Define a regular expression pattern to match the title
    title_pattern = re.compile(r'Title:\s*(.*)', re.IGNORECASE)
    author_pattern = re.compile(r'Author:\s*(.*)', re.IGNORECASE)

    # Search for the pattern in the text
    match_title = title_pattern.search(text)
    match_auth = author_pattern.search(text)

    if match_title:
        title = match_title.group(1).strip()
    else:
        return None
    
    if match_auth:
        auth = match_auth.group(1).strip()
    else:
        return None
    
    return title, auth
    
with open("book.txt", 'r', encoding='utf-8') as f:
    book = f.read()
    

def get_paragraphe(book):

    start_pattern = re.escape("*** START OF THE PROJECT GUTENBERG EBOOK THE SOUL OF HENRY JONES ***")
    end_pattern = re.escape("*** END OF THE PROJECT GUTENBERG EBOOK THE SOUL OF HENRY JONES ***")

    start_match = re.search(start_pattern, book)
    end_match = re.search(end_pattern, book)

    if start_match and end_match:
        start_index = start_match.end()
        end_index = end_match.start()
        content_between = book[start_index:end_index].strip()

        return content_between
        # print("Start Pattern Matched at Index:", start_match.start())
        # print("End Pattern Matched at Index:", end_match.start())
        # print("Content between Start and End Patterns:", content_between)
    else:
        print("Start or End pattern not found in the given text.")
        
    return None

def main():
    #get the content of the chapter
    content = get_paragraphe(book)
    # get the name and author of the book
    title, auth = extract_title(book)
    # print(f"Title : {title} \nAuth : {auth}")
    #get the nb of words in the paragraphe round to the nearest ten
    word_count_list = word_count(content)
    display(content)
    graph(word_count_list)
    
    main_image()
    main_rotate()
    
    doc_main(title, auth, word_count_list)
    
main()
    
    
    

