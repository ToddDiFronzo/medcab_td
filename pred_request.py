import pickle
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from pydantic import BaseModel


# Load in pickle_tfidf
tfidf_pickle = open('./pickles/pickle_tfidf', 'rb')
tfidf = pickle.load(tfidf_pickle)
tfidf_pickle.close()
# Load in pickle_nn
nn_pickle = open('./pickles/pickle_nn', 'rb')
nn = pickle.load(nn_pickle)
nn_pickle.close()
# Load in pickle_nn
dataset_pickle = open('./pickles/pickle_dataset', 'rb')
df = pickle.load(dataset_pickle)
dataset_pickle.close()

class PredRequest(BaseModel):
    user_input: str

    class Config:
        schema_extra = {
            "example": {
                "user_input": "happy, relaxed"
            }
        }
    def pred(self):
        user_input = self.user_input

        # pre-process new data
        new_dtm = tfidf.transform([user_input])
        new_dtm = pd.DataFrame(new_dtm.todense(), columns=tfidf.get_feature_names())
        distance, indices = nn.kneighbors(new_dtm, n_neighbors=10)
        indices_final = indices[0]
        rec_strains = []
        for x in indices_final:
            print(df['Strain'][x])
            rec_strains.append(df['Strain'][x])
        return rec_strains