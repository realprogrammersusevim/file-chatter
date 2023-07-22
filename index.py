import pickle
from collections import Counter
from glob import glob

import numpy as np
from nltk.tokenize import word_tokenize

from utils import preprocess

dataset = []

for file in glob(
    "/Users/jonathanmilligan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Zettelkasten/*.md"
):
    with open(file) as f:
        text = f.read().strip()

    dataset.append((file, text))


N = len(dataset)


processed_title = []
processed_text = []

for i in dataset:
    processed_title.append(word_tokenize(str(preprocess(i[0]))))
    processed_text.append(word_tokenize(str(preprocess(i[1]))))


DF = {}

for i in range(N):
    tokens = processed_text[i]

    for w in tokens:
        try:
            DF[w].add(i)
        except:
            DF[w] = {i}

    tokens = processed_title[i]
    for w in tokens:
        try:
            DF[w].add(i)
        except:
            DF[w] = {i}

for i in DF:
    DF[i] = len(DF[i])


def doc_freq(word):
    c = 0

    try:
        c = DF[word]
    except:
        pass

    return c


doc = 0

tf_idf = {}

for i in range(N):
    tokens = processed_text[i]

    counter = Counter(tokens + processed_title[i])
    words_count = len(tokens + processed_title[i])

    for token in np.unique(tokens):
        tf = counter[token] / words_count
        df = doc_freq(token)
        idf = np.log((N + 1) / (df + 1))

        tf_idf[doc, token] = tf * idf

    doc += 1

doc = 0

tf_idf_title = {}

for i in range(N):
    tokens = processed_title[i]
    counter = Counter(tokens + processed_text[i])
    words_count = len(tokens + processed_text[i])

    for token in np.unique(tokens):
        tf = counter[token] / words_count
        df = doc_freq(token)
        idf = np.log(
            (N + 1) / (df + 1)
        )  # numerator is added 1 to avoid negative values

        tf_idf_title[doc, token] = tf * idf

    doc += 1

alpha = 0.3

for i in tf_idf:
    tf_idf[i] *= alpha

for i in tf_idf_title:
    tf_idf[i] = tf_idf_title[i]

with open("dataset.pickle", "wb") as d:
    pickle.dump(dataset, d)

with open("tfidf.pickle", "wb") as t:
    pickle.dump(tf_idf, t)
