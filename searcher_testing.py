from commons.documents_reader import get_documents
from commons.hazm_tokenizer import HazmTokenizer
from searchers.boolean_sercher import BooleanSearcher
from searchers.fasttext_searcher import FasttextSearcher
from searchers.tfidf_searcher import TfidfSearcher
from searchers.transformer_searcher import TransformerSearcher

documents = get_documents()

queries = open('queries.txt').readlines()


def search_queries_by_searcher(test_searcher, test_queries):
    test_searcher.add_documents(documents)
    for query in test_queries:
        print("Query:")
        print(query)

        print("Results:")
        result = test_searcher.search(query)
        for doc in result:
            print(doc.id + ": " + doc.content[:120].replace('\n', ''))


# testing boolean searcher
# tokenizer = HazmTokenizer()
# searcher = BooleanSearcher(tokenizer)
# search_queries_by_searcher(searcher, queries[:10])

# testing tfidf searcher
# searcher = TfidfSearcher()
# search_queries_by_searcher(searcher, queries[:10])


# testing fasttext searcher
searcher = FasttextSearcher()
search_queries_by_searcher(searcher, queries[:10])

# testing transformer searcher
# searcher = TransformerSearcher()
# search_queries_by_searcher(searcher, queries[:5])
