# import packages
import PyPDF2
import re
import os

'''
Programma per la ricerca di parole nei PDF, inserire la parola da cercare e il path nel quale
ci sono i file PDF. il programma cercherà le parole all'interno di tutti i file ritornando il
nome dei PDF in cui ha ottenuto dei risultati e il numero di pagine in cui ha riscontrato la parola

N.B. non funziona per tutti i file PDF, con alcuni da problemi la libreria PyPDF2. ci si aspetta dei
miglioramenti da parte dei creatori in futuro
'''

#inserire il path che identifica la cartella di ricerca
#my_dir="D:/Nine/UNI/ProvaPdf"

#inserire la parola che si desidera cercare
#word = "Amministrazione"

# searches the word iin the specific pdf_object, gives bakc the number of results
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

# searches pdf files in the directory and gives back the results of the searched word
def analize_pdfs(my_dir, word_to_search):
    for file in os.listdir(my_dir):
        if file.endswith(".pdf"):
            pdf_object = PyPDF2.PdfFileReader(my_dir + "/" + file)
            # get number of pages
            num_pages = pdf_object.getNumPages()
            results=search_word(pdf_object, word_to_search, num_pages)
            if(results!=0):
                print("\n" + file +  "; Number of results: " + str(results))


print("\n--------------------------------------------------------------------------------\n")
print("DISCLAIMER: il programma è CASE SENTISIVE. Il numero di risultati identifica " +
      "il numero di pagine pdf in cui compare la parola cercata. La ricerca potrebbe " +
      "risultare nulla per alcuni file PDF, in base al modo in cui sono stati generati " +
      "se succede per un file PDF succederà molto probabilmente per tutti gli altri " +
      "dello stesso *pacchetto*")
print("\n--------------------------------------------------------------------------------\n")

quit=1
while(quit==1):
    my_dir=input("inserire il path della directory: ")
    word=input("inserire parola da cercare: ")
    analize_pdfs(my_dir, word)
    if (not(input("continuare la ricerca? (y/n) ")=="y")):
        quit=0
        print("ciao ciao!")
    print("\n")
