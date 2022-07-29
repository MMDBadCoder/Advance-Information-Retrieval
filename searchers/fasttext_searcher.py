import fasttext
from scipy import spatial

from commons.document import Document


class FasttextSearcher:
    def __init__(self):
        self.model = fasttext.load_model(
            '/home/mohammad/Desktop/Advanced_Information_Retrieval/hw3/hw3_project/fasttext_model/mmd-model.bin')
        self.vector_by_document = {}

    def add_documents(self, documents):
        for document in documents:
            content = document.content.replace('\n', ' ')
            self.vector_by_document[document.id] = self.model.get_sentence_vector(content)

    def search(self, query_text, result_limit=10):
        query_text = query_text.replace('\n', ' ')
        query_vector = self.model.get_sentence_vector(query_text)
        distances = []
        for doc_id, doc_vector in self.vector_by_document.items():
            distances.append((doc_id, 1 - spatial.distance.cosine(query_vector, doc_vector)))
        distances.sort(key=lambda x: x[1], reverse=True)
        return [Document.get_document_by_id(item[0]) for item in distances[:min(result_limit, len(distances))]]
