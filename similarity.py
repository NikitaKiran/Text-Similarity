from tkinter import *
import gensim
import numpy as np
from gensim.models import Word2Vec
model = Word2Vec.load("word2vec.model")
i=0
def close():
    output=Entry(root, width=200)
    output.insert(0, 'GOODBYE !')
    output.pack()
    root.after(2000, root.destroy)
    global i
    i=1
    
def callsimilar():
    similar(str(input_para.get()),input_sent.get())

def refresh():
    root.destroy()
    

def similar(sentences, mainsen):
    endings=['?','!','\n']
    for ch in endings:
            sentences = sentences.replace(ch,'.')
    sentences = sentences.split('.')
    similarsen={}  #dictionary to store the sentence:similarity
    text=''
    mainsen = mainsen.split()
    c1=0
    vec1=[0]*250
    for word in mainsen:
        c1+=1
        if model.wv.__contains__(word):        
            vec1+=model.wv[word]
    vec1/=c1
    a = np.array(vec1)
    if sentences[-1] == '':
        sentences.pop()


    for sen in sentences:
        sen2= sen.split()
        vec2=[0]*250
        c2=0
        for word in sen2:
            c2+=1
            if model.wv.__contains__(word):
                vec2+=model.wv[word]
        
        vecfin=vec2/c2
        b = np.array(vecfin) 
        ma = np.linalg.norm(a)
        mb = np.linalg.norm(b)
        sim = (np.matmul(a,b))/(ma*mb)
        if sim > 0.75:
            similarsen[sen]=sim
    if mainsen != 'Enter sentence':
        if len(similarsen)==0:
            text='There are no sentences similar to what you are looking for'
        else:
            output_text=Entry(root, width=200)
            output_text.insert(0, 'The similar sentences are :')
            output_text.pack()
            for el in similarsen:
                text += el+' ( '+ str(similarsen[el])+ ')'        
    output_sent=Entry(root, width=200)
    output_sent.insert(0, text)
    output_sent.pack()
    submitbutton.destroy()
    refresh_program = Button(root,text="Once more",command= refresh)
    refresh_program.pack()
    quit_program=Button(root,text="Exit Program",command=close)
    quit_program.pack()

while(i==0):
    root=Tk()
    root.title("Text Similarity")
    root.iconbitmap(r'text filter logo.ico')

    introtext=Label(root,text="Welcome to Text Similarity!\n Enter any sentence and we will find all sentences similar to that in the text entered.")
    introtext.pack()

    input_sent=Entry(root, width=200)
    input_sent.insert(0, "Enter sentence you want to search for")
    input_sent.pack()   

    input_para=Entry(root, width=200)
    input_para.insert(0, "Enter text to search from")
    input_para.pack()  
  
    submitbutton=Button(root, text="Submit", command=callsimilar)
    submitbutton.pack()

    root.mainloop() 
    



