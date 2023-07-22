import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from num2words import num2words


def preprocess(data):
    # Convert to lower case
    data = np.char.lower(data)

    # Remove stop words
    stop_words = stopwords.words("english")
    words = word_tokenize(str(data))
    new_text = ""

    for w in words:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w

    data = new_text

    # Remove punctuation
    symbols = '!"#$%&()*+-./:;<=>?@[\]^_`{|}~\n'

    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], " ")
        data = np.char.replace(data, " ", " ")

    data = np.char.replace(data, ",", "")

    # Remove apostrophes
    np.char.replace(data, "'", "")

    # Stem everything
    stemmer = PorterStemmer()
    tokens = word_tokenize(str(data))
    stem_text = ""

    for w in tokens:
        stem_text = stem_text + " " + stemmer.stem(w)

    data = stem_text

    # Convert numbers
    num_tokens = word_tokenize(str(data))
    num_text = ""

    for w in num_tokens:
        try:
            w = num2words(int(w))
        except:
            a = 0

        num_text = num_text + " " + w

    num_text = np.char.replace(num_text, "-", " ")
    data = num_text

    return data
