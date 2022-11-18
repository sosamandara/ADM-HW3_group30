import pandas as pd
# Stopwords
from nltk.corpus import stopwords # nltk.download('stopwords')
from spacy.lang.en.stop_words import STOP_WORDS

stop_words = set(stopwords.words('english')) | set(STOP_WORDS) ## Cem: Here i comine to sets of stopwords to get a bigger list

# Lemmatizer
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

# Supress FutureWarning
import warnings; warnings.simplefilter(action='ignore', category=FutureWarning)


class Preprocessor():
    def __init__(self):
        None

    def preprocess_column(self, text_column: pd.Series) -> pd.Series:
        # Step 1: Lowercase
        text_column = text_column.str.lower()
        # Step 2.1: Remove all spaces, i.e., \n
        text_column = text_column.str.replace('\n', ' ').replace('\t', ' ')
        # Step 2.2: Remove all punctuation
        text_column = text_column.str.replace('[^\w\s]', '')
        # Step 3: Remove stopwords
        text_column = text_column.apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))
        # Lemmatize
        text_column = text_column.apply(lambda x: ' '.join([wnl.lemmatize(word) for word in x.split()]))

        return text_column

    def preprocess_str(self, text: str) -> list:
        # Step 1: Lowercase
        text = text.lower()
        # Step 2.1: Remove all spaces, i.e., \n
        text = text.replace('\n', ' ')
        # Step 2.2: Remove all punctuation
        text = text.replace('[^\w\s]', '')
        # Step 3: Remove stopwords
        text = ([word for word in text.split() if word not in stop_words])
        # Lemmatize
        text = ([wnl.lemmatize(word, 'v') for word in text])

        return text