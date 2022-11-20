import os
import pandas as pd
from pandas.core.indexes.range import RangeIndex

# Stopwords
from nltk.corpus import stopwords # nltk.download('stopwords')
from spacy.lang.en.stop_words import STOP_WORDS
stop_words = set(stopwords.words('english')) | set(STOP_WORDS) ## Cem: Here i comine to sets of stopwords to get a bigger list

# Lemmatizer
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

# Supress FutureWarning
import warnings; warnings.simplefilter(action='ignore', category=FutureWarning)
import warnings; warnings.simplefilter(action='ignore', category=UserWarning)

class ComplexEngine:

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.df['placeDescX'] = self.preprocess_column(self.df['placeDesc'])
        None


    def search(self, query: dict) -> pd.DataFrame:
        '''
        A MORE complex search engine that uses multiple queries to filter the data.

        Parameters
        ----------
        query : dict
            A dictionary that contains the queries. The allowed keys are:
            - name: str
            - desc: str
            - address: str
            - usernames: list
            - tags: list
            - num_visits: list
            - lists_appearences: list

        Returns
        -------
        pd.DataFrame
            A dataframe that contains the filtered data.
        '''

        copy = self.df.copy()
        for k, v in query.items():
            if k == 'name':
                copy = copy.loc[self.filter_by_name(v, copy)]
            elif k == 'desc':
                copy = copy.loc[self.filter_by_description(v, copy)]
            elif k == 'address':
                copy = copy.loc[self.filter_by_address(v, copy)]
            elif k == 'usernames':
                copy = copy.loc[self.filter_by_usernames(v, copy)]
            elif k == 'tags':
                copy = copy.loc[self.filter_by_tags(v, copy)]
            elif k == 'num_visits':
                copy = copy.loc[self.filter_by_num_visits(v[0], v[1], copy)]
            elif k == 'lists_appearences':
                copy = copy.loc[self.filter_by_lists_appearences(v, copy)]
            elif k == 'text':
                None
            else:
                raise ValueError(f'Invalid key: {k}')

        if copy.empty:
            print('No results found. Please try less restrictive queries s\'il vous plait.')
            print('ᕕ(ಥʖ̯ಥ) ᕗ')
        else:
            return copy[['placeName', 'placeURL']]

    
    def filter_by_name(self, name: str, data: pd.DataFrame) -> RangeIndex:
        return data[data['placeName'].apply(lambda x: name.lower() in x.lower() if x else False)].index
    
    def filter_by_description(self, query: str, data: pd.DataFrame) -> RangeIndex:

        query = self.preprocess_str(query)

        for q in query:
            data = data[data['placeDescX'].apply(lambda x: q in x if x else False)]

        return data.index

    def filter_by_address(self, address: str, data: pd.DataFrame) -> RangeIndex:

        for a in address.split():
            data = data[data['placeAddress'].apply(lambda x: a.lower() in x.lower() if x else False)]

        return data.index

    # Returns index based on the query
    def filter_by_usernames(self, usernames: list, data: pd.DataFrame) -> RangeIndex:
        # only keep rows that have the usernames (placeEditors)
        placeEditors = data['placeEditors']

        for user in usernames:
            data = data[placeEditors.apply(lambda x: len([user.lower() in y.lower() for y in x]) > 0 if x else False)]
        return data.index

    def filter_by_tags(self, tags: list, data: pd.DataFrame) -> RangeIndex:
        # only keep rows that have the tags (placeTags)
        placeTags = data['placeTags']

        for tag in tags:
            data = data[placeTags.apply(lambda x: tag in x if x else False)]
        
        return data.index

    def filter_by_num_visits(self, ub: int, lb: int, data: pd.DataFrame) -> RangeIndex:
        # only keep rows that have the num_visits (placeVisits)
        numPeopleVisited = data['numPeopleVisited']

        if ub:
            data = data[numPeopleVisited.apply(lambda x: x <= ub)]
        if lb:
            data = data[numPeopleVisited.apply(lambda x: x >= lb)]
        
        return data.index

    def filter_by_lists_appearences(self, lists: list, data: pd.DataFrame) -> RangeIndex:
        # only keep rows that have the lists (placeLists)
        placeRelatedLists = data['placeRelatedLists']

        # TODO: make a list of lists so that only valid lists are accepted

        for l in lists:
            data = data[placeRelatedLists.apply(lambda x: l in x if x else False)]
        
        return data.index

    def preprocess_column(self, text_column: pd.Series) -> pd.Series:
        # Step 1: Lowercase
        text_column = text_column.str.lower()
        # Step 2.1: Remove all spaces, i.e., \n
        text_column = text_column.str.replace('\n', ' ')
        # Step 2.2: Remove all punctuation
        text_column = text_column.str.replace('[^\w\s]', '')
        # Step 3: Remove stopwords
        text_column = text_column.apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))
        # Lemmatize
        text_column = text_column.apply(lambda x: ' '.join([wnl.lemmatize(word) for word in x.split()]))

        return text_column

    def preprocess_str(self, text: str) -> str:
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


if __name__ == "__main__":
    print(os.getcwd())
    df = pd.read_pickle('places.pkl')
    usernames = ['nick']
    ce = ComplexEngine(df)

    query = {
        'usernames': ['nick'],
        'tags': ['graffiti'],
        'address': 'prague',
    }


    print(ce.search(query))