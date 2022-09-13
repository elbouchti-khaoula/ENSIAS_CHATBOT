import json
import pickle
from nltk_functions import *
import numpy as np
import random
from tensorflow.keras.models import load_model

with open('data.json' , 'r', encoding="cp437", errors='ignore') as f:
    data= json.load(f)

words = pickle.load(open('words.pkl','rb'))
tags = pickle.load(open('tags.pkl','rb'))
model = load_model('model.h5')


import pyttsx3
from speech_recognition import Recognizer, Microphone

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def predire_tag(sentence):
    p = tok_and_lem(sentence)
    bow = np.array(bag_of_words(p,words))
    res = model.predict(np.array([bow]))[0]  #Generates output predictions for the input samples
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': tags[r[0]], 'probability': str(r[1])})
    return return_list

def reponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['data']
    flag = 0
    for i in list_of_intents:
        if i['tag']  == tag:
            result = random.choice(i['responses'])
            flag = 1
            break
    if flag == 0:
        result = "Je m'excuse j'ai pas compris ta question. Peut tu la reformuler?"
    return result



def audio():
    l = ['','']
    recognizer = Recognizer()
    # On enregistre le son
    with Microphone() as source:
        print("Réglage du bruit ambiant... Patientez...")
        recognizer.adjust_for_ambient_noise(source)
        print("Vous pouvez parler...")
        recorded_audio = recognizer.listen(source)
        print("Enregistrement terminé !")

    # Reconnaissance de l'audio
    try:
        print("Reconnaissance du texte...")
        l[0] = recognizer.recognize_google(
            recorded_audio,
            language="fr-FR"
        )
        print("Vous avez dit : {}".format(l[0]))
        l[1] = reponse_chatbot(l[0])
        print(l[1])

    except Exception as ex:
        print(ex)
    return l

def reponse_chatbot(message):
    tag = predire_tag(message)
    res = reponse(tag , data)
    return res






