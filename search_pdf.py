# import packages
import PyPDF2
import re
import os

'''
This program is used to search words in PDF files, insert the word you want to searche and the path
in which are stored the PDF files. The program will search words inside all files giving back the
name of the PDF files in which it has found results, and the number of times the word appeard.

DISCLAIMER: this doesn't work for all type of PDF files, some have troubles with the library PyPDF2, depending
on which generator system has been used to create the PDF file. 
'''


# searches the word in the specific pdf_object, gives back the number of results
def search_word(pdf_object, word_to_search, num_pages):
    results=0
    # extract text and do the search
    for i in range(0, num_pages):
        PageObj = pdf_object.getPage(i)
        Text = PageObj.extractText()
        # print(Text)
        # print("this is page " + str(i+1))
        ResSearch = re.search(word_to_search, Text)
        if(ResSearch!=None):
            #print("this is page " + str(i+1))
            #print(ResSearch)
            results=results+1
        ResSearch=None
    return results

# searches PDF files in the directory and gives back the results of the searched word
def analize_pdfs(my_dir, word_to_search):
    for file in os.listdir(my_dir):
        if file.endswith(".pdf"):
            pdf_object = PyPDF2.PdfFileReader(my_dir + "/" + file)
            # get number of pages
            num_pages = pdf_object.getNumPages()
            results=search_word(pdf_object, word_to_search, num_pages)
            if(results!=0):
                print("\n" + file +  "; Number of results: " + str(results))


quit=1
while(quit==1):
    my_dir=input("Insert the dircetory path: ")
    word=input("Insert the word you want to search: ")
    analize_pdfs(my_dir, word)
    if (not(input("continue searching? (y/n) ")=="y")):
        quit=0
        print("bye bye!")
    print("\n")
