from keras.models import load_model
import pickle
import numpy as np
from pymorphy2 import MorphAnalyzer
import re

print("""
your_name = KeLoss()
your_name.predict(msg_text, wlen=min_word_len(default 3)) to get class of msg.
    will return (class_name, class_id) tuple
your_name.remorph(msg_text, wlen=min_word_len(default 3)) to get lemmatized msg_text
    useable for w2v ranging =)
"""

class KeLoss:
    def __init__(self, model='model/model.h5', vectr='model/tfidf.sav', id2nam='model/id2name.sav', nam2id='model/name2id.sav'):
        self.model = load_model(model)
        with open(vectr, 'rb') as f:
            self.vectr = pickle.load(f)
            print("Loaded vectorizer")
        with open(id2nam, 'rb') as f:
            self.id2nam = pickle.load(f)
            print("Loaded id2name")
        with open(nam2id, 'rb') as f:
            self.nam2id = pickle.load(f)
            print("Loaded name2id")
        self.morph = MorphAnalyzer()

    def remorph(self, text, wlen=3):
        text = text.lower()
        text = re.sub('[^a-zа-я]', ' ', text)
        return ' '.join([self.morph.parse(i)[0].normal_form for i in text.split(' ') if len(i) > wlen])

    def predict(self, text, wlen=3):
        text = self.remorph(text, wlen)
        print(text)
        text = self.vectr.transform([text]).toarray()
        predicted = self.id2nam[np.argmax(self.model.predict(text))]
        return (predicted, self.nam2id[predicted])
