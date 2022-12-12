#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[91]:


#Import tkinter library
from tkinter import *
from tkinter import ttk
import re
import inflect
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
import requests 
import contractions
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import PyPDF2
from tkinter import filedialog
import lxml
import sys


#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
#Define a new function to open the window



#Text analysis with html web page............................................................................................./

def open_win1():
   new= Toplevel(win)
   new.geometry("750x250")
   new.title("New Window")
   #Create a Label in New window
   Label(new, text="Text Analysis", font=('Helvetica 17 bold')).grid(row=1, column=4)
   Label(new, text="Enter URl", font=('Helvetica 10 bold')).grid(row=2, column=1)
   inputtxt = Text(new,height = 2,width = 50,  bg = "light yellow")
   inputtxt.grid(row=3, column=1)
   gettxt = Button(new,height = 2, width = 20, text ="Show Text", command = lambda:Take_input())
   gettxt.grid(row=4, column=1)
   Displaytxt = Text(new,height = 6,width = 50,bg = "light cyan")
   Displaytxt.grid(row=5, column=1)
   getoutput = Button(new,height = 2, width = 20, text ="Show Result", command = lambda:count_words())
   getoutput.grid(row=6, column=1)
   
   Label(new, text="Number of Words:", font=('Helvetica 10 bold')).grid(row=2, column=3)
   wordstxt =Text(new,height = 2,width = 10,  bg = "light yellow")
   wordstxt.grid(row=2, column=4)
   
   Label(new, text="Number of Sentences:", font=('Helvetica 10 bold')).grid(row=3, column=3)
   sentencestxt =Text(new,height = 2,width = 10,  bg = "light yellow")
   sentencestxt.grid(row=3, column=4)
   
   Label(new, text="Number of Character:", font=('Helvetica 10 bold')).grid(row=4, column=3)
   characterstxt =Text(new,height = 2,width = 10,  bg = "light yellow")
   characterstxt.grid(row=4, column=4)
    
   Label(new, text="Shortest Sentences:", font=('Helvetica 10 bold')).grid(row=8, column=1)
   s_sentencestxt =Text(new,height = 3,width = 50,  bg = "light yellow")
   s_sentencestxt.grid(row=9, column=1)

   Label(new, text="Longest Sentences:", font=('Helvetica 10 bold')).grid(row=10, column=1)
   l_sentencestxt =Text(new,height = 3,width = 50,  bg = "light yellow")
   l_sentencestxt.grid(row=11, column=1)
    
   
   Label(new, text="Enter number to find words:", font=('Helvetica 10 bold')).grid(row=8, column=3)
   takedigit =Text(new,height = 3,width = 5,  bg = "light yellow")
   takedigit.grid(row=9, column=3)
   showresult = Button(new,height = 2, width = 5, text ="Count", command = lambda:exactly_counts())
   showresult.grid(row=10, column=3)
   Label(new, text="Most frequent Word:", font=('Helvetica 10 bold')).grid(row=11, column=3)
   mf_wordtxt =Text(new,height = 4,width = 20,  bg = "light yellow")
   mf_wordtxt.grid(row=12, column=3)

   Label(new, text="Most frequent Noun:", font=('Helvetica 10 bold')).grid(row=12, column=1)
   noun_mftxt =Text(new,height = 4,width = 50,  bg = "light yellow")
   noun_mftxt.grid(row=13, column=1)
   
   Label(new, text="Most frequent Adverb:", font=('Helvetica 10 bold')).grid(row=14, column=1)
   adverb_mftxt =Text(new,height = 4,width = 50,  bg = "light yellow")
   adverb_mftxt.grid(row=15, column=1)
   
   Label(new, text="Most Frequent Adjective:", font=('Helvetica 10 bold')).grid(row=16, column=1)
   adj_mftxt =Text(new,height = 4,width = 50,  bg = "light yellow")
   adj_mftxt.grid(row=17, column=1)
       
  
   def Take_input():
    Displaytxt.delete("1.0","end")
    url = inputtxt.get("1.0", "end-1c")
    print(url)
    # opening the url for reading
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    for para in soup.find_all("p"):
        txt=para.get_text()
        Displaytxt.insert(END, txt)

    
   def exactly_counts():
    mf_wordtxt.delete("1.0","end")
    txt =Displaytxt.get("1.0", "end-1c")
    words= nltk.word_tokenize(txt)
    print(words)
    txt1 = int(takedigit.get("1.0", "end-1c"))      
    exactly_times = list()
    for key, value in Counter(words).items():
            if(value == txt1):
                exactly_times.append(key)

    mf_wordtxt.insert(END, exactly_times)
    print(exactly_times)
    
   def count_words():
    s_sentencestxt.delete("1.0","end")
    l_sentencestxt.delete("1.0","end")
    noun_mftxt.delete("1.0","end")
    adverb_mftxt.delete("1.0","end")
    adj_mftxt.delete("1.0","end")
    wordstxt.delete("1.0","end")
    sentencestxt.delete("1.0","end")   
    characterstxt.delete("1.0","end")
    
    
    
    txt =Displaytxt.get("1.0", "end-1c")
    words_1= nltk.word_tokenize(txt)
    count_w=len(words_1)
    wordstxt.insert(END, count_w)
    print(count_w)
    
    
    
    
    sentense= nltk.sent_tokenize(txt)
    count_s=len(sentense)
    sentencestxt.insert(END, count_s)
    
    # Longest Sentence
    lengths = [len(sentense) for sentense in txt]
    longest_sentence = txt[lengths.index(max(lengths))] 
    l_sen=longest_sentence
    l_sentencestxt.insert(END, l_sen)
    print("Length of the longest sentence: ", max(lengths))
    print("The longest sentence: ", longest_sentence)
    
    raw = nltk.Text(nltk.word_tokenize(txt))
    fdist = nltk.FreqDist(raw)
    print (fdist.N())

    # Shortest Sentence
    shortest_sentence = txt[lengths.index(min(lengths))]
    s_sen=shortest_sentence
    s_sentencestxt.insert(END, str(s_sen))
    print("Length of the Shortest sentence: ", min(lengths))
    print("The shortest sentence: ", shortest_sentence)

    

    words= nltk.word_tokenize(txt)

    pos_tags = nltk.pos_tag(words, tagset='universal', lang='eng')
    
    def findtags(tag_prefix, tagged_text):
        cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                      if tag.startswith(tag_prefix))
        return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

    



    # Count most frequent Noun
    nouns = findtags('NOUN', pos_tags)

    for tag in sorted(nouns):
         print(tag, nouns[tag])
    noun_mftxt.insert(END, nouns)

    # Count most frequent Verb
    verb = findtags('VERB', pos_tags)
    adverb_mftxt.insert(END, verb)
    for tag in sorted(verb):
         print(tag, verb[tag])

    # Count most frequent Adjectives
    Adjectives = findtags('ADJ', pos_tags)
    adj_mftxt.insert(END, Adjectives)
    for tag in sorted(Adjectives):
         print(tag, Adjectives[tag])
    
       
#Text analysis with PDF......................................................................................................./

def open_win12():
   new= Toplevel(win)
   new.geometry("750x250")
   new.title("New Window")
   #Create a Label in New window
   Label(new, text="Text Analysis using PDF", font=('Helvetica 17 bold')).grid(row=1, column=4)
   Label(new, text="Press button to open PDF file", font=('Helvetica 10 bold')).grid(row=2, column=1)
   
   gettxt = Button(new,height = 2, width = 20, text ="Open PDF File", command = lambda:Open_PDF())
   gettxt.grid(row=4, column=1)
   Displaytxt = Text(new,height = 6,width = 50,bg = "light cyan")
   Displaytxt.grid(row=5, column=1)
   getoutput = Button(new,height = 2, width = 20, text ="Show Result", command = lambda:count_words())
   getoutput.grid(row=6, column=1)
   
   Label(new, text="Number of Words:", font=('Helvetica 10 bold')).grid(row=2, column=3)
   wordstxt =Text(new,height = 2,width = 10,  bg = "light yellow")
   wordstxt.grid(row=2, column=4)
   
   Label(new, text="Number of Sentences:", font=('Helvetica 10 bold')).grid(row=3, column=3)
   sentencestxt =Text(new,height = 2,width = 10,  bg = "light yellow")
   sentencestxt.grid(row=3, column=4)
   
   Label(new, text="Number of Character:", font=('Helvetica 10 bold')).grid(row=4, column=3)
   characterstxt =Text(new,height = 2,width = 10,  bg = "light yellow")
   characterstxt.grid(row=4, column=4)
    
   Label(new, text="Shortest Sentences:", font=('Helvetica 10 bold')).grid(row=8, column=1)
   s_sentencestxt =Text(new,height = 3,width = 50,  bg = "light yellow")
   s_sentencestxt.grid(row=9, column=1)

   Label(new, text="Longest Sentences:", font=('Helvetica 10 bold')).grid(row=10, column=1)
   l_sentencestxt =Text(new,height = 3,width = 50,  bg = "light yellow")
   l_sentencestxt.grid(row=11, column=1)
    
   
   Label(new, text="Enter number to find words:", font=('Helvetica 10 bold')).grid(row=8, column=3)
   takedigit =Text(new,height = 3,width = 5,  bg = "light yellow")
   takedigit.grid(row=9, column=3)
   showresult = Button(new,height = 2, width = 5, text ="Count", command = lambda:exactly_counts())
   showresult.grid(row=10, column=3)
   Label(new, text="Most frequent Word:", font=('Helvetica 10 bold')).grid(row=11, column=3)
   mf_wordtxt =Text(new,height = 4,width = 20,  bg = "light yellow")
   mf_wordtxt.grid(row=12, column=3)

   Label(new, text="Most frequent Noun:", font=('Helvetica 10 bold')).grid(row=12, column=1)
   noun_mftxt =Text(new,height = 4,width = 50,  bg = "light yellow")
   noun_mftxt.grid(row=13, column=1)
   
   Label(new, text="Most frequent Adverb:", font=('Helvetica 10 bold')).grid(row=14, column=1)
   adverb_mftxt =Text(new,height = 4,width = 50,  bg = "light yellow")
   adverb_mftxt.grid(row=15, column=1)
   
   Label(new, text="Most Frequent Adjective:", font=('Helvetica 10 bold')).grid(row=16, column=1)
   adj_mftxt =Text(new,height = 4,width = 50,  bg = "light yellow")
   adj_mftxt.grid(row=17, column=1)
   

   def Open_PDF():
    open_file = filedialog.askopenfilename(

        title="Open PDF File",
        filetypes=(
             ("PDF Files", "*.pdf"),))
    
    if open_file:
        #Open the pdf file
        pdf_file =PyPDF2.PdfFileReader(open_file)
        page_stuff=""
        #Set the page to read
        for i in range(0,pdf_file.numPages):
            pageObj = pdf_file.getPage(i)
            page_stuff = page_stuff+ pageObj.extractText()
        #Extract the text from the pdf file
        
        Displaytxt.insert(END, page_stuff)

    
   def exactly_counts():
    mf_wordtxt.delete("1.0","end")
    txt =Displaytxt.get("1.0", "end-1c")
    words= nltk.word_tokenize(txt)
    print(words)
    txt1 = int(takedigit.get("1.0", "end-1c"))      
    exactly_times = list()
    for key, value in Counter(words).items():
            if(value == txt1):
                exactly_times.append(key)

    mf_wordtxt.insert(END, exactly_times)
    print(exactly_times)
    
   def count_words():
    s_sentencestxt.delete("1.0","end")
    l_sentencestxt.delete("1.0","end")
    noun_mftxt.delete("1.0","end")
    adverb_mftxt.delete("1.0","end")
    adj_mftxt.delete("1.0","end")
    wordstxt.delete("1.0","end")
    sentencestxt.delete("1.0","end")   
    characterstxt.delete("1.0","end")
    txt =Displaytxt.get("1.0", "end-1c")
    words_1= nltk.word_tokenize(txt)
    count_w=len(words_1)
    wordstxt.insert(END, count_w)
    print(count_w)
    sentense= nltk.sent_tokenize(txt)
    count_s=len(sentense)
    sentencestxt.insert(END, count_s)
    
    # Longest Sentence
    lengths = [len(sentense) for sentense in txt]
    longest_sentence = txt[lengths.index(max(lengths))] 
    l_sen=longest_sentence
    l_sentencestxt.insert(END, l_sen)
    print("Length of the longest sentence: ", max(lengths))
    print("The longest sentence: ", longest_sentence)
    
    raw = nltk.Text(nltk.word_tokenize(txt))
    fdist = nltk.FreqDist(raw)
    print (fdist.N())

    # Shortest Sentence
    shortest_sentence = txt[lengths.index(min(lengths))]
    s_sen=shortest_sentence
    s_sentencestxt.insert(END, str(s_sen))
    print("Length of the Shortest sentence: ", min(lengths))
    print("The shortest sentence: ", shortest_sentence)
    words= nltk.word_tokenize(txt)

    pos_tags = nltk.pos_tag(words, tagset='universal', lang='eng')
    
    def findtags(tag_prefix, tagged_text):
        cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                      if tag.startswith(tag_prefix))
        return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

    # Count most frequent Noun
    nouns = findtags('NOUN', pos_tags)

    for tag in sorted(nouns):
         print(tag, nouns[tag])
    noun_mftxt.insert(END, nouns)

    # Count most frequent Verb
    verb = findtags('VERB', pos_tags)
    adverb_mftxt.insert(END, verb)
    for tag in sorted(verb):
         print(tag, verb[tag])

    # Count most frequent Adjectives
    Adjectives = findtags('ADJ', pos_tags)
    adj_mftxt.insert(END, Adjectives)
    for tag in sorted(Adjectives):
         print(tag, Adjectives[tag])
    
       
#Text analysis with XML......................................................................................................./

def open_win13():
   new= Toplevel(win)
   new.geometry("750x250")
   new.title("New Window")
   #Create a Label in New window
   Label(new, text="Text Analysis using XML", font=('Helvetica 17 bold')).grid(row=1, column=4)
   Label(new, text="Press button to open PDF file", font=('Helvetica 10 bold')).grid(row=2, column=1)
   
   gettxt = Button(new,height = 2, width = 20, text ="Open PDF File", command = lambda:Open_PDF())
   gettxt.grid(row=4, column=1)
   Displaytxt = Text(new,height = 6,width = 50,bg = "light cyan")
   Displaytxt.grid(row=5, column=1)
   getoutput = Button(new,height = 2, width = 20, text ="Show Result", command = lambda:count_words())
   getoutput.grid(row=6, column=1)
   
   Label(new, text="Number of Words:", font=('Helvetica 10 bold')).grid(row=2, column=3)
   wordstxt =Text(new,height = 2,width = 10,  bg = "light yellow")
   wordstxt.grid(row=2, column=4)
   
   Label(new, text="Number of Sentences:", font=('Helvetica 10 bold')).grid(row=3, column=3)
   sentencestxt =Text(new,height = 2,width = 10,  bg = "light yellow")
   sentencestxt.grid(row=3, column=4)
   
   Label(new, text="Number of Character:", font=('Helvetica 10 bold')).grid(row=4, column=3)
   characterstxt =Text(new,height = 2,width = 10,  bg = "light yellow")
   characterstxt.grid(row=4, column=4)
    
   Label(new, text="Shortest Sentences:", font=('Helvetica 10 bold')).grid(row=8, column=1)
   s_sentencestxt =Text(new,height = 3,width = 50,  bg = "light yellow")
   s_sentencestxt.grid(row=9, column=1)

   Label(new, text="Longest Sentences:", font=('Helvetica 10 bold')).grid(row=10, column=1)
   l_sentencestxt =Text(new,height = 3,width = 50,  bg = "light yellow")
   l_sentencestxt.grid(row=11, column=1)
    
   
   Label(new, text="Enter number to find words:", font=('Helvetica 10 bold')).grid(row=8, column=3)
   takedigit =Text(new,height = 3,width = 5,  bg = "light yellow")
   takedigit.grid(row=9, column=3)
   showresult = Button(new,height = 2, width = 5, text ="Count", command = lambda:exactly_counts())
   showresult.grid(row=10, column=3)
   Label(new, text="Most frequent Word:", font=('Helvetica 10 bold')).grid(row=11, column=3)
   mf_wordtxt =Text(new,height = 4,width = 20,  bg = "light yellow")
   mf_wordtxt.grid(row=12, column=3)

   Label(new, text="Most frequent Noun:", font=('Helvetica 10 bold')).grid(row=12, column=1)
   noun_mftxt =Text(new,height = 4,width = 50,  bg = "light yellow")
   noun_mftxt.grid(row=13, column=1)
   
   Label(new, text="Most frequent Adverb:", font=('Helvetica 10 bold')).grid(row=14, column=1)
   adverb_mftxt =Text(new,height = 4,width = 50,  bg = "light yellow")
   adverb_mftxt.grid(row=15, column=1)
   
   Label(new, text="Most Frequent Adjective:", font=('Helvetica 10 bold')).grid(row=16, column=1)
   adj_mftxt =Text(new,height = 4,width = 50,  bg = "light yellow")
   adj_mftxt.grid(row=17, column=1)
   

   def Open_PDF():
    open_file = filedialog.askopenfilename(

        title="Open PDF File",
        filetypes=(
             ("XML Files", "*.xml"),))
    print(open_file)
    with open (open_file.xml, 'r') as f:
        data =f.read()
    All_data =BeautifulSoup(data,"xml")
    tag_data = All_data.find_all('Any_TAG_NAME')
    Displaytxt.insert(END, tag_data)
        #Extract the text from the pdf file
        
        

    
   def exactly_counts():
    mf_wordtxt.delete("1.0","end")
    txt =Displaytxt.get("1.0", "end-1c")
    words= nltk.word_tokenize(txt)
    print(words)
    txt1 = int(takedigit.get("1.0", "end-1c"))      
    exactly_times = list()
    for key, value in Counter(words).items():
            if(value == txt1):
                exactly_times.append(key)

    mf_wordtxt.insert(END, exactly_times)
    print(exactly_times)
    
   def count_words():
    s_sentencestxt.delete("1.0","end")
    l_sentencestxt.delete("1.0","end")
    noun_mftxt.delete("1.0","end")
    adverb_mftxt.delete("1.0","end")
    adj_mftxt.delete("1.0","end")
    wordstxt.delete("1.0","end")
    sentencestxt.delete("1.0","end")   
    characterstxt.delete("1.0","end")
    txt =Displaytxt.get("1.0", "end-1c")
    words_1= nltk.word_tokenize(txt)
    count_w=len(words_1)
    wordstxt.insert(END, count_w)
    print(count_w)
    sentense= nltk.sent_tokenize(txt)
    count_s=len(sentense)
    sentencestxt.insert(END, count_s)
    
    # Longest Sentence
    lengths = [len(sentense) for sentense in txt]
    longest_sentence = txt[lengths.index(max(lengths))] 
    l_sen=longest_sentence
    l_sentencestxt.insert(END, l_sen)
    print("Length of the longest sentence: ", max(lengths))
    print("The longest sentence: ", longest_sentence)
    
    raw = nltk.Text(nltk.word_tokenize(txt))
    fdist = nltk.FreqDist(raw)
    print (fdist.N())

    # Shortest Sentence
    shortest_sentence = txt[lengths.index(min(lengths))]
    s_sen=shortest_sentence
    s_sentencestxt.insert(END, str(s_sen))
    print("Length of the Shortest sentence: ", min(lengths))
    print("The shortest sentence: ", shortest_sentence)
    words= nltk.word_tokenize(txt)

    pos_tags = nltk.pos_tag(words, tagset='universal', lang='eng')
    
    def findtags(tag_prefix, tagged_text):
        cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                      if tag.startswith(tag_prefix))
        return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

    # Count most frequent Noun
    nouns = findtags('NOUN', pos_tags)

    for tag in sorted(nouns):
         print(tag, nouns[tag])
    noun_mftxt.insert(END, nouns)

    # Count most frequent Verb
    verb = findtags('VERB', pos_tags)
    adverb_mftxt.insert(END, verb)
    for tag in sorted(verb):
         print(tag, verb[tag])

    # Count most frequent Adjectives
    Adjectives = findtags('ADJ', pos_tags)
    adj_mftxt.insert(END, Adjectives)
    for tag in sorted(Adjectives):
         print(tag, Adjectives[tag])
    
         
    
    
    
 #Text Cleaning with PDF....................................................................................................../

def open_win2():
   new= Toplevel(win)
   new.geometry("750x250")
   new.title("New Window")
   #Create a Label in New window
   Label(new, text="Text Cleaning", font=('Helvetica 17 bold')).grid(row=1, column=2,pady=5,padx=5)
   Label(new, text="Press button to open PDF File", font=('Helvetica 10 bold')).grid(row=2, column=1,pady=5,padx=5)
   
   gettxt = Button(new,height = 2, width = 20, text ="Show Text", command = lambda:Open_PDF())
   gettxt.grid(row=4, column=1,pady=5,padx=5)
   Displaytxt = Text(new,height = 8,width = 50,bg = "light cyan")
   Displaytxt.grid(row=5, column=1,pady=5,padx=5)
   getoutput = Button(new,height = 2, width = 20, text ="Show Result", command = lambda:output())
   getoutput.grid(row=6, column=1,pady=5,padx=5)
   
   Label(new, text="Remove Brackets", font=('Helvetica 10 bold')).grid(row=8, column=1)
   r_bracketstxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_bracketstxt.grid(row=9, column=1,pady=5,padx=5)
    
   Label(new, text="Replace Contractions", font=('Helvetica 10 bold')).grid(row=10, column=1)
   r_contractionstxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_contractionstxt.grid(row=11, column=1,pady=5,padx=5)

   Label(new, text="Remove Non_Ascii characters", font=('Helvetica 10 bold')).grid(row=12, column=1)
   r_nonasciitxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_nonasciitxt.grid(row=13, column=1,pady=5,padx=5)
     
   Label(new, text="Convert text to lower case", font=('Helvetica 10 bold')).grid(row=8, column=2)
   r_lowercasetxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_lowercasetxt.grid(row=9, column=2,pady=5,padx=5)

   Label(new, text="Remove Punctuation", font=('Helvetica 10 bold')).grid(row=10, column=2)
   r_punctuationtxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_punctuationtxt.grid(row=11, column=2,pady=5,padx=5)
    
   Label(new, text="Replace number", font=('Helvetica 10 bold')).grid(row=12, column=2)
   r_numberstxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_numberstxt.grid(row=13, column=2,pady=5,padx=5)
   
   Label(new, text="Remove Stop words", font=('Helvetica 10 bold')).grid(row=8, column=3,)
   r_stopwordstxt =Text(new,height = 8, width = 50,  bg = "light yellow")
   r_stopwordstxt.grid(row=9, column=3,pady=5,padx=5)
   
   Label(new, text="Final Clean text", font=('Helvetica 10 bold')).grid(row=10, column=3)
   resulttxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   resulttxt.grid(row=11, column=3,pady=5,padx=5)
   
  
   def Open_PDF():
        open_file = filedialog.askopenfilename(

            title="Open PDF File",
            filetypes=(
                 ("PDF Files", "*.pdf"),))

        if open_file:
            #Open the pdf file
            pdf_file =PyPDF2.PdfFileReader(open_file)
            page_stuff=""
            #Set the page to read
            for i in range(0,pdf_file.numPages):
                pageObj = pdf_file.getPage(i)
                page_stuff = page_stuff+ pageObj.extractText()
            #Extract the text from the pdf file

            Displaytxt.insert(END, page_stuff)

   def remove_between_square_brackets(text):
        """ Use regular expressions to clean brackets """
        return re.sub('\[[^]]*\]', '', text)

   def denoise_text(text):
        """ denoise text """
        txt = Displaytxt.get("1.0", "end-1c")
        text = txt
        text = remove_between_square_brackets(text)
        r_bracketstxt.insert(END, text)
        return text
        

   def replace_contractions(text):
        """Replace contractions in string of text"""
        return contractions.fix(text)
    
   def remove_non_ascii(words):
        """Remove non-ASCII characters from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 
        'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
            
        return new_words
   def to_lowercase(words):
        """Convert all characters to lowercase from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = word.lower()
            new_words.append(new_word)
        return new_words
   def remove_punctuation(words):
        """Remove punctuation from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words
   def replace_numbers(words):
        """Replace all integer occurrences in list of tokenized words with textual 
    representation"""
        p = inflect.engine()
        new_words = []
        for word in words:
            if word.isdigit():
                new_word = p.number_to_words(word)
                new_words.append(new_word)
            else:
                new_words.append(word)
        return new_words
   def remove_stopwords(words):
        """Remove stop words from list of tokenized words"""
        new_words = []
        for word in words:
            if word not in stopwords.words('english'):
                new_words.append(word)
        return new_words
   def stem_words(words):
        """Stem words in list of tokenized words"""
        stemmer = LancasterStemmer()
        stems = []
        for word in words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems
   def lemmatize_verbs(words):
        """Lemmatize verbs in list of tokenized words"""
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for word in words:
            lemma = lemmatizer.lemmatize(word, pos='v')
            lemmas.append(lemma)
        return lemmas
   def normalize(words):
        words = remove_non_ascii(words)
        r_nonasciitxt.result(END,words)
        words = to_lowercase(words)
        r_lowercasetxt.result(END,words)
        words = remove_punctuation(words)
        r_punctuation.result(END,words)
        words = replace_numbers(words)
        r_numberstxt.result(END,words)
        words = remove_stopwords(words)
        r_stopwordstxt.result(END,words)
        return words
    
   def output():
        r_bracketstxt.delete("1.0","end")
        r_contractionstxt.delete("1.0","end")
        r_nonasciitxt.delete("1.0","end")
        r_lowercasetxt.delete("1.0","end")
        r_punctuationtxt.delete("1.0","end")
        r_numberstxt.delete("1.0","end")
        r_stopwordstxt.delete("1.0","end")   
        txt = Displaytxt.get("1.0", "end-1c")
        sample = denoise_text(txt)
        sample = replace_contractions(sample)
        r_contractionstxt.insert(END, sample)
        words = nltk.word_tokenize(sample)
        words = to_lowercase(words)
        r_lowercasetxt.insert(END,words)
        words = remove_punctuation(words)
        r_punctuationtxt.insert(END,words)
        words = replace_numbers(words)
        r_numberstxt.insert(END,words)
        words = remove_stopwords(words)
        r_stopwordstxt.insert(END,words)
        resulttxt.insert(END, words)
   
   
#Text Cleaning with html web site....................................................................................................../

def open_win22():
   new= Toplevel(win)
   new.geometry("750x250")
   new.title("New Window")
   #Create a Label in New window
   Label(new, text="Text Cleaning", font=('Helvetica 17 bold')).grid(row=1, column=2,pady=5,padx=5)
   Label(new, text="Enter URL", font=('Helvetica 10 bold')).grid(row=2, column=1,pady=5,padx=5)
   inputtxt = Text(new,height = 2,width = 50,  bg = "light yellow")
   inputtxt.grid(row=3, column=1,pady=5,padx=5)
   gettxt = Button(new,height = 2, width = 20, text ="Show Text", command = lambda:Take_input())
   gettxt.grid(row=4, column=1,pady=5,padx=5)
   Displaytxt = Text(new,height = 8,width = 50,bg = "light cyan")
   Displaytxt.grid(row=5, column=1,pady=5,padx=5)
   getoutput = Button(new,height = 2, width = 20, text ="Show Result", command = lambda:output())
   getoutput.grid(row=6, column=1,pady=5,padx=5)
   
   Label(new, text="Remove Brackets", font=('Helvetica 10 bold')).grid(row=8, column=1,)
   r_bracketstxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_bracketstxt.grid(row=9, column=1,padx = 5, pady=5)
    
   Label(new, text="Replace Contractions", font=('Helvetica 10 bold')).grid(row=10, column=1,)
   r_contractionstxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_contractionstxt.grid(row=11, column=1,padx = 5, pady=5)

   Label(new, text="Remove Non_Ascii characters", font=('Helvetica 10 bold')).grid(row=12, column=1)
   r_nonasciitxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_nonasciitxt.grid(row=13, column=1,padx = 5, pady=5)
     
   Label(new, text="Convert text to lower case", font=('Helvetica 10 bold')).grid(row=8, column=2)
   r_lowercasetxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_lowercasetxt.grid(row=9, column=2,padx = 5, pady=5)

   Label(new, text="Remove Punctuation", font=('Helvetica 10 bold')).grid(row=10, column=2)
   r_punctuationtxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_punctuationtxt.grid(row=11, column=2,padx = 5, pady=5)
    
   Label(new, text="Replace number", font=('Helvetica 10 bold')).grid(row=12, column=2)
   r_numberstxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_numberstxt.grid(row=13, column=2,padx = 5, pady=5)
   
   Label(new, text="Remove Stop words", font=('Helvetica 10 bold')).grid(row=8, column=3,)
   r_stopwordstxt =Text(new,height = 8, width = 50,  bg = "light yellow")
   r_stopwordstxt.grid(row=9, column=3,padx = 5, pady=5)
   
   Label(new, text="Final Clean text", font=('Helvetica 10 bold')).grid(row=10, column=3)
   resulttxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   resulttxt.grid(row=11, column=3,padx = 5, pady=5)
   
  
   def Take_input():
    Displaytxt.delete("1.0","end")
    url = inputtxt.get("1.0", "end-1c")
    print(url)
    # opening the url for reading
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    for para in soup.find_all("p"):
        txt=para.get_text()
        Displaytxt.insert(END, txt)
   def remove_between_square_brackets(text):
        """ Use regular expressions to clean brackets """
        return re.sub('\[[^]]*\]', '', text)

   def denoise_text(text):
        """ denoise text """
        txt = Displaytxt.get("1.0", "end-1c")
        text = txt
        text = remove_between_square_brackets(text)
        r_bracketstxt.insert(END, text)
        return text
        

   def replace_contractions(text):
        """Replace contractions in string of text"""
        return contractions.fix(text)
    
   def remove_non_ascii(words):
        """Remove non-ASCII characters from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 
        'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
            
        return new_words
   def to_lowercase(words):
        """Convert all characters to lowercase from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = word.lower()
            new_words.append(new_word)
        return new_words
   def remove_punctuation(words):
        """Remove punctuation from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words
   def replace_numbers(words):
        """Replace all integer occurrences in list of tokenized words with textual 
    representation"""
        p = inflect.engine()
        new_words = []
        for word in words:
            if word.isdigit():
                new_word = p.number_to_words(word)
                new_words.append(new_word)
            else:
                new_words.append(word)
        return new_words
   def remove_stopwords(words):
        """Remove stop words from list of tokenized words"""
        new_words = []
        for word in words:
            if word not in stopwords.words('english'):
                new_words.append(word)
        return new_words
   def stem_words(words):
        """Stem words in list of tokenized words"""
        stemmer = LancasterStemmer()
        stems = []
        for word in words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems
   def lemmatize_verbs(words):
        """Lemmatize verbs in list of tokenized words"""
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for word in words:
            lemma = lemmatizer.lemmatize(word, pos='v')
            lemmas.append(lemma)
        return lemmas
   def normalize(words):
        words = remove_non_ascii(words)
        r_nonasciitxt.result(END,words)
        words = to_lowercase(words)
        r_lowercasetxt.result(END,words)
        words = remove_punctuation(words)
        r_punctuation.result(END,words)
        words = replace_numbers(words)
        r_numberstxt.result(END,words)
        words = remove_stopwords(words)
        r_stopwordstxt.result(END,words)
        return words
    
   def output():
        r_bracketstxt.delete("1.0","end")
        r_contractionstxt.delete("1.0","end")
        r_nonasciitxt.delete("1.0","end")
        r_lowercasetxt.delete("1.0","end")
        r_punctuationtxt.delete("1.0","end")
        r_numberstxt.delete("1.0","end")
        r_stopwordstxt.delete("1.0","end")   
        txt = Displaytxt.get("1.0", "end-1c")
        sample = denoise_text(txt)
        sample = replace_contractions(sample)
        r_contractionstxt.insert(END, sample)
        words = nltk.word_tokenize(sample)
        words = to_lowercase(words)
        r_lowercasetxt.insert(END,words)
        words = remove_punctuation(words)
        r_punctuationtxt.insert(END,words)
        words = replace_numbers(words)
        r_numberstxt.insert(END,words)
        words = remove_stopwords(words)
        r_stopwordstxt.insert(END,words)
        resulttxt.insert(END, words)
        
        

 #Text Cleaning with XML....................................................................................................../

def open_win23():
   new= Toplevel(win)
   new.geometry("750x250")
   new.title("New Window")
   #Create a Label in New window
   Label(new, text="Text Cleaning with XML ", font=('Helvetica 17 bold')).grid(row=1, column=2,pady=5,padx=5)
   Label(new, text="Press button to open PDF File", font=('Helvetica 10 bold')).grid(row=2, column=1)
   
   gettxt = Button(new,height = 2, width = 20, text ="Show Text", command = lambda:Open_PDF())
   gettxt.grid(row=4, column=1,pady=5,padx=5)
   Displaytxt = Text(new,height = 8,width = 50,bg = "light cyan")
   Displaytxt.grid(row=5, column=1,pady=5,padx=5)
   getoutput = Button(new,height = 2, width = 20, text ="Show Result", command = lambda:output())
   getoutput.grid(row=6, column=1,pady=5,padx=5)
   
   Label(new, text="Remove Brackets", font=('Helvetica 10 bold')).grid(row=8, column=1)
   r_bracketstxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_bracketstxt.grid(row=9, column=1,pady=5,padx=5)
    
   Label(new, text="Replace Contractions", font=('Helvetica 10 bold')).grid(row=10, column=1)
   r_contractionstxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_contractionstxt.grid(row=11, column=1,pady=5,padx=5)

   Label(new, text="Remove Non_Ascii characters", font=('Helvetica 10 bold')).grid(row=12, column=1)
   r_nonasciitxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_nonasciitxt.grid(row=13, column=1,pady=5,padx=5)
     
   Label(new, text="Convert text to lower case", font=('Helvetica 10 bold')).grid(row=8, column=2)
   r_lowercasetxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_lowercasetxt.grid(row=9, column=2,pady=5,padx=5)

   Label(new, text="Remove Punctuation", font=('Helvetica 10 bold')).grid(row=10, column=2)
   r_punctuationtxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_punctuationtxt.grid(row=11, column=2,pady=5,padx=5)
    
   Label(new, text="Replace number", font=('Helvetica 10 bold')).grid(row=12, column=2)
   r_numberstxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   r_numberstxt.grid(row=13, column=2,pady=5,padx=5)
   
   Label(new, text="Remove Stop words", font=('Helvetica 10 bold')).grid(row=8, column=3,)
   r_stopwordstxt =Text(new,height = 8, width = 50,  bg = "light yellow")
   r_stopwordstxt.grid(row=9, column=3,pady=5,padx=5)
   
   Label(new, text="Final Clean text", font=('Helvetica 10 bold')).grid(row=10, column=3)
   resulttxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   resulttxt.grid(row=11, column=3,pady=5,padx=5)
   
  
   def Open_PDF():
    open_file = filedialog.askopenfilename(

        title="Open PDF File",
        filetypes=(
             ("XML Files", "*.xml"),))
    print(open_file)
    with open (open_file.xml, 'r') as f:
        data =f.read()
    All_data =BeautifulSoup(data,"xml")
    tag_data = All_data.find_all('Any_TAG_NAME')
    Displaytxt.insert(END, tag_data)
        #Extract the text from the pdf file

   def remove_between_square_brackets(text):
        """ Use regular expressions to clean brackets """
        return re.sub('\[[^]]*\]', '', text)

   def denoise_text(text):
        """ denoise text """
        txt = Displaytxt.get("1.0", "end-1c")
        text = txt
        text = remove_between_square_brackets(text)
        r_bracketstxt.insert(END, text)
        return text
        

   def replace_contractions(text):
        """Replace contractions in string of text"""
        return contractions.fix(text)
    
   def remove_non_ascii(words):
        """Remove non-ASCII characters from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 
        'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
            
        return new_words
   def to_lowercase(words):
        """Convert all characters to lowercase from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = word.lower()
            new_words.append(new_word)
        return new_words
   def remove_punctuation(words):
        """Remove punctuation from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words
   def replace_numbers(words):
        """Replace all integer occurrences in list of tokenized words with textual 
    representation"""
        p = inflect.engine()
        new_words = []
        for word in words:
            if word.isdigit():
                new_word = p.number_to_words(word)
                new_words.append(new_word)
            else:
                new_words.append(word)
        return new_words
   def remove_stopwords(words):
        """Remove stop words from list of tokenized words"""
        new_words = []
        for word in words:
            if word not in stopwords.words('english'):
                new_words.append(word)
        return new_words
   def stem_words(words):
        """Stem words in list of tokenized words"""
        stemmer = LancasterStemmer()
        stems = []
        for word in words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems
   def lemmatize_verbs(words):
        """Lemmatize verbs in list of tokenized words"""
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for word in words:
            lemma = lemmatizer.lemmatize(word, pos='v')
            lemmas.append(lemma)
        return lemmas
   def normalize(words):
        words = remove_non_ascii(words)
        r_nonasciitxt.result(END,words)
        words = to_lowercase(words)
        r_lowercasetxt.result(END,words)
        words = remove_punctuation(words)
        r_punctuation.result(END,words)
        words = replace_numbers(words)
        r_numberstxt.result(END,words)
        words = remove_stopwords(words)
        r_stopwordstxt.result(END,words)
        return words
    
   def output():
        r_bracketstxt.delete("1.0","end")
        r_contractionstxt.delete("1.0","end")
        r_nonasciitxt.delete("1.0","end")
        r_lowercasetxt.delete("1.0","end")
        r_punctuationtxt.delete("1.0","end")
        r_numberstxt.delete("1.0","end")
        r_stopwordstxt.delete("1.0","end")   
        txt = Displaytxt.get("1.0", "end-1c")
        sample = denoise_text(txt)
        sample = replace_contractions(sample)
        r_contractionstxt.insert(END, sample)
        words = nltk.word_tokenize(sample)
        words = to_lowercase(words)
        r_lowercasetxt.insert(END,words)
        words = remove_punctuation(words)
        r_punctuationtxt.insert(END,words)
        words = replace_numbers(words)
        r_numberstxt.insert(END,words)
        words = remove_stopwords(words)
        r_stopwordstxt.insert(END,words)
        resulttxt.insert(END, words)
   
   
# Text Matching with PDF................................................................................................../   


def open_win3():
   new= Toplevel(win)
   new.geometry("750x250")
   new.title("New Window")
   #Create a Label in New window
   Label(new, text="Text Matching", font=('Helvetica 17 bold')).grid(row=1, column=2)
   Label(new, text="Press button to open PDF File", font=('Helvetica 10 bold')).grid(row=2, column=1)
   
   gettxt = Button(new,height = 2, width = 20, text ="Show Text", command = lambda:Open_PDF())
   gettxt.grid(row=4, column=1)
   Displaytxt = Text(new,height = 8,width = 50,bg = "light cyan")
   Displaytxt.grid(row=5, column=1)
   
   
   
   Label(new, text="Enter the regular expressing that you want to match in text", font=('Helvetica 12 bold')).grid(row=7, column=1) 
   
   take_retxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   take_retxt.grid(row=8, column=1)
    
   

   getoutput = Button(new,height = 2, width = 20, text ="Show Result", command = lambda:matchstring())
   getoutput.grid(row=9, column=1)

   Label(new, text="Match Display", font=('Helvetica 10 bold')).grid(row=10, column=1)
   match_displaytxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   match_displaytxt.grid(row=11, column=1)
    
    
   Label(new, text="Enter the replacement string array Like [(r'won\'t', 'will not'),(r'can\'t', 'cannot'), ]", 
         font=('Helvetica 12 bold')).grid(row=7, column=3) 
   
   take_retxt1 =Text(new,height = 8,width = 50,  bg = "light yellow")
   take_retxt1.grid(row=8, column=3)
    
   

   getoutput1 = Button(new,height = 2, width = 20, text ="Show Result", command = lambda:matchstring1())
   getoutput1.grid(row=9, column=3)

   Label(new, text="Match Display", font=('Helvetica 10 bold')).grid(row=10, column=3)
   match_displaytxt1 =Text(new,height = 8,width = 50,  bg = "light yellow")
   match_displaytxt1.grid(row=11, column=3)
    
    
    
    
    
   def Open_PDF():
        open_file = filedialog.askopenfilename(

            title="Open PDF File",
            filetypes=(
                 ("PDF Files", "*.pdf"),))

        if open_file:
            #Open the pdf file
            pdf_file =PyPDF2.PdfFileReader(open_file)
            page_stuff=""
            #Set the page to read
            for i in range(0,pdf_file.numPages):
                pageObj = pdf_file.getPage(i)
                page_stuff = page_stuff+ pageObj.extractText()
            #Extract the text from the pdf file

            Displaytxt.insert(END, page_stuff)
    
   

   replacement_patterns = [
    (r'won\'t', 'will not'),
    (r'can\'t', 'cannot'),
    (r'i\'m', 'i am'),
    (r'ain\'t', 'is not'),
    (r'(\w+)\'ll', '\g<1> will'),
    (r'(\w+)n\'t', '\g<1> not'),
    (r'(\w+)\'ve', '\g<1> have'),
    (r'(\w+)\'s', '\g<1> is'),
    (r'(\w+)\'re', '\g<1> are'),
    (r'(\w+)\'d', '\g<1> would')
    ]
   txt = Displaytxt.get("1.0", "end-1c")
   class RegexpReplacer(object):
    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]
        
    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
            s = re.sub(pattern, repl, s)

        return s
   def matchstring1():
        replacer = RegexpReplacer()
        result= replacer.replace(txt)
        match_displaytxt1.insert(END,result)
    
   def matchstring():
        line = Displaytxt.get("1.0", "end-1c")
        match = take_retxt.get("1.0", "end-1c")
        r1 = re.findall(r'match',line)
        match_displaytxt.insert(END,result)
        
        
# Text Matching with Html Web Site................................................................................................../   


def open_win32():
   new= Toplevel(win)
   new.geometry("750x250")
   new.title("New Window")
   #Create a Label in New window
   Label(new, text="Text Matching", font=('Helvetica 17 bold')).grid(row=1, column=2)
   Label(new, text="Enter URL", font=('Helvetica 10 bold')).grid(row=2, column=1)
   inputtxt = Text(new,height = 2,width = 50,  bg = "light yellow")
   inputtxt.grid(row=3, column=1)
   gettxt = Button(new,height = 2, width = 20, text ="Show Text", command = lambda:Take_input())
   gettxt.grid(row=4, column=1)
   Displaytxt = Text(new,height = 8,width = 50,bg = "light cyan")
   Displaytxt.grid(row=5, column=1)
   
   
   
   Label(new, text="Enter the regular expressing that you want to match in text", font=('Helvetica 12 bold')).grid(row=7, column=1) 
   
   take_retxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   take_retxt.grid(row=8, column=1)
    
   

   getoutput = Button(new,height = 2, width = 20, text ="Show Result", command = lambda:matchstring())
   getoutput.grid(row=9, column=1)

   Label(new, text="Match Display", font=('Helvetica 10 bold')).grid(row=10, column=1)
   match_displaytxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   match_displaytxt.grid(row=11, column=1)
    
    
   Label(new, text="Enter the replacement string array Like [(r'won\'t', 'will not'),(r'can\'t', 'cannot'),]", font=('Helvetica 17 bold')).grid(row=7, column=2) 
   
   take_retxt1 =Text(new,height = 8,width = 50,  bg = "light yellow")
   take_retxt1.grid(row=8, column=3)
    
   

   getoutput1 = Button(new,height = 2, width = 20, text ="Show Result", command = lambda:matchstring1())
   getoutput1.grid(row=9, column=3)

   Label(new, text="Replace Display", font=('Helvetica 10 bold')).grid(row=10, column=3)
   match_displaytxt1 =Text(new,height = 8,width = 50,  bg = "light yellow")
   match_displaytxt1.grid(row=11, column=3)
    
    
    
    
    
   def Take_input():
    Displaytxt.delete("1.0","end")
    url = inputtxt.get("1.0", "end-1c")
    print(url)
    # opening the url for reading
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    for para in soup.find_all("p"):
        txt=para.get_text()
        Displaytxt.insert(END, txt)
    
   

   replacement_patterns = [
    (r'won\'t', 'will not'),
    (r'can\'t', 'cannot'),
    (r'i\'m', 'i am'),
    (r'ain\'t', 'is not'),
    (r'(\w+)\'ll', '\g<1> will'),
    (r'(\w+)n\'t', '\g<1> not'),
    (r'(\w+)\'ve', '\g<1> have'),
    (r'(\w+)\'s', '\g<1> is'),
    (r'(\w+)\'re', '\g<1> are'),
    (r'(\w+)\'d', '\g<1> would')
    ]
   txt = Displaytxt.get("1.0", "end-1c")
   class RegexpReplacer(object):
    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]
        
    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
            s = re.sub(pattern, repl, s)

        return s
   def matchstring1():
        replacer = RegexpReplacer()
        result= replacer.replace(txt)
        match_displaytxt1.insert(END,result)
    
   def matchstring():
        line = Displaytxt.get("1.0", "end-1c")
        match = take_retxt.get("1.0", "end-1c")
        r1 = re.findall(r'match',line)
        match_displaytxt.insert(END,result)
        
# Text matching with XML ............................................................................../       
def open_win33():
   new= Toplevel(win)
   new.geometry("750x250")
   new.title("New Window")
   #Create a Label in New window
   Label(new, text="Text Matching", font=('Helvetica 17 bold')).grid(row=1, column=2)
   Label(new, text="Press button to open XML File", font=('Helvetica 10 bold')).grid(row=2, column=1)
   
   gettxt = Button(new,height = 2, width = 20, text ="Show Text", command = lambda:Open_XML())
   gettxt.grid(row=4, column=1)
   Displaytxt = Text(new,height = 8,width = 50,bg = "light cyan")
   Displaytxt.grid(row=5, column=1)
   
   
   
   Label(new, text="Enter the regular expressing that you want to match in text", font=('Helvetica 12 bold')).grid(row=7, column=1) 
   
   take_retxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   take_retxt.grid(row=8, column=1)
    
   

   getoutput = Button(new,height = 2, width = 20, text ="Show Result", command = lambda:matchstring())
   getoutput.grid(row=9, column=1)

   Label(new, text="Match Display", font=('Helvetica 12 bold')).grid(row=10, column=1)
   match_displaytxt =Text(new,height = 8,width = 50,  bg = "light yellow")
   match_displaytxt.grid(row=11, column=1)
    
    
   Label(new, text="Enter the replacement string array Like [(r'won\'t', 'will not'),    (r'can\'t', 'cannot'),]", 
         font=('Helvetica 12 bold')).grid(row=7, column=3) 
   
   take_retxt1 =Text(new,height = 8,width = 50,  bg = "light yellow")
   take_retxt1.grid(row=8, column=3)
    
   

   getoutput1 = Button(new,height = 2, width = 20, text ="Show Result", command = lambda:matchstring1())
   getoutput1.grid(row=9, column=3)

   Label(new, text="Replacement Display", font=('Helvetica 10 bold')).grid(row=10, column=3)
   match_displaytxt1 =Text(new,height = 8,width = 50,  bg = "light yellow")
   match_displaytxt1.grid(row=11, column=3)
    
    
    
    
    
   def Open_XML():
    open_file = filedialog.askopenfilename(

        title="Open PDF File",
        filetypes=(
             ("XML Files", "*.xml"),))
    print(open_file)
    with open (open_file.xml, 'r') as f:
        data =f.read()
    All_data =BeautifulSoup(data,"xml")
    tag_data = All_data.find_all('Any_TAG_NAME')
    Displaytxt.insert(END, tag_data)
    
   

   replacement_patterns = [
    (r'won\'t', 'will not'),
    (r'can\'t', 'cannot'),
    (r'i\'m', 'i am'),
    (r'ain\'t', 'is not'),
    (r'(\w+)\'ll', '\g<1> will'),
    (r'(\w+)n\'t', '\g<1> not'),
    (r'(\w+)\'ve', '\g<1> have'),
    (r'(\w+)\'s', '\g<1> is'),
    (r'(\w+)\'re', '\g<1> are'),
    (r'(\w+)\'d', '\g<1> would')
    ]
   txt = Displaytxt.get("1.0", "end-1c")
   class RegexpReplacer(object):
        def __init__(self, patterns=replacement_patterns):
            self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]
        
        def replace(self, text):
            s = text
            for (pattern, repl) in self.patterns:
                s = re.sub(pattern, repl, s)

            return s
   

   def matchstring1():
        replacer = RegexpReplacer()
        result= replacer.replace(txt)
        match_displaytxt1.insert(END,result)
   
   def matchstring():
        line = Displaytxt.get("1.0", "end-1c")
        match = take_retxt.get("1.0", "end-1c")
        r1 = re.findall(r'match',line)
        match_displaytxt.insert(END,result) 
    
   
    
    
    
    
    

#Create a label
Label(win, text= "Click the below button to Open a New Window", font= ('Helvetica 24 bold')).grid(row=2, column=4)
#Create a button to open a New Window
ttk.Button(win, text="Text Analysis with PDF", command=open_win12).grid(row=5, column=4,padx=10,pady=10)
ttk.Button(win, text="Text Analysis with HTML", command=open_win1).grid(row=6, column=4,padx=10,pady=10)
ttk.Button(win, text="Text Analysis with XML", command=open_win13).grid(row=7, column=4,padx=10,pady=10)
ttk.Button(win, text="Text Cleaning with PDF", command=open_win2).grid(row=8, column=4,padx=10,pady=10)
ttk.Button(win, text="Text Cleaning with HTML", command=open_win22).grid(row=9, column=4,padx=10,pady=10)
ttk.Button(win, text="Text Cleaning with XML", command=open_win23).grid(row=10, column=4,padx=10,pady=10)
ttk.Button(win, text="Text Matching with PDF", command=open_win3).grid(row=11, column=4,padx=10,pady=10)
ttk.Button(win, text="Text Matching with HTML", command=open_win32).grid(row=12, column=4,padx=10,pady=10)
ttk.Button(win, text="Text Matching with XML", command=open_win33).grid(row=13, column=4,padx=10,pady=10)
win.mainloop()


# In[ ]:





# ### 

# In[36]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[41]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:





# In[ ]:




