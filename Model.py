#Code to create model

import gensim
file = open("Code.txt", "r")
text=file.read()

#Tokenization
text= text.replace('\n',' ')
text=text.lower()
extrachars=['-','_','(',')',':',':','\"','\'','=','/','[',']',',','!','?','+','*']
for ch in extrachars:
    text=text.replace(ch,'')
for dig in range(10):
    text=text.replace(str(dig),'')    
sen=text.split('.')
words=[sentence.split(' ') for sentence in sen]

#Creating and saving the model
from gensim.models import Word2Vec
model = Word2Vec(words, min_count=7,window =6, size=250)
model.save("word2vec.model")


file.close()
print("Model is trained")

