import json
import pickle
import random

import numpy as np
from nltk_functions import *
with open('data.json' , 'r', encoding="cp437", errors='ignore') as f:
    data= json.load(f)

ignore_words = [',','?','!','.',"'"]

all_words = []
tags = []
pair = []   #tag+mot
for info in data['data'] :
    tag = info['tag'] #gives the value of the tag
    tags.append(tag)
    for pattern in info['patterns']:
        #tokenize chaque mot de la phrase
        s = tokenize(pattern)
        #ajouter dans la liste des mots
        for i in s :
            all_words.append(i)
        #liste des pairs tag+mot
        pair.append((s,tag))

#lemmatize the words
mot_lem = []
for m in all_words:
    if m not in ignore_words:
        mot_lem.extend(lemmatize(m))

mot_lem = sorted(list(set(mot_lem)))
tags = sorted(list(set(tags)))

pickle.dump(mot_lem,open('words.pkl','wb'))   #save  into a file
pickle.dump(tags,open('tags.pkl','wb'))
# on est pret pour construire notre DL model

BoW = []   #liste des bag of words des phrases
t = []

#create train and test lists. X - patterns, Y - intents
train_x = []
train_y = []

for p in pair:
    #bag of words de chaque phrase dans patterns
    bag = bag_of_words(p[0] , mot_lem)
    BoW.append(bag)
    i = tags.index(p[1])
    tag_index = [0] * len(tags)
    tag_index[i] = 1
    t.append([bag,tag_index])
    train_x.append(bag)
    train_y.append(tag_index)









