import pandas
from hazm import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer


class TfidfSearcher:
    def __init__(self):
        self.tf_idf_vector_maker = TfidfVectorizer(norm='l2', tokenizer=word_tokenize)
        self.data_frame = None
        self.query_tokenize = None
        self.documents = None

    def add_documents(self, documents):
        self.documents = documents
        contents = [doc.content for doc in documents]
        tf_idf = self.tf_idf_vector_maker.fit_transform(contents)
        self.data_frame = pandas.DataFrame(tf_idf.todense(), columns=self.tf_idf_vector_maker.get_feature_names_out())
        self.query_tokenize = self.tf_idf_vector_maker.build_tokenizer()

    def search(self, query_text, result_limit=10):
        query_tokens = self.query_tokenize(query_text)
        query_data_frame = self.data_frame[query_tokens].copy()
        query_data_frame.loc[:, "sum"] = query_data_frame.sum(axis=1).array
        result = query_data_frame.nlargest(result_limit, "sum")
        return [self.documents[i] for i in result.index]
