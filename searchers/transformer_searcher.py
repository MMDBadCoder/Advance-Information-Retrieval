from sentence_transformers import SentenceTransformer, util

from commons.document import Document


class TransformerSearcher:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.vector_by_document = {}

    def add_documents(self, documents):
        for document in documents:
            self.vector_by_document[document.id] = self.model.encode(document.content)

    def search(self, query_text, result_limit=10):
        query_vector = self.model.encode(query_text)
        distances = []
        for doc_id, doc_vector in self.vector_by_document.items():
            distances.append((doc_id, util.cos_sim(query_vector, doc_vector)))
        distances.sort(key=lambda x: x[1], reverse=True)
        return [Document.get_document_by_id(item[0]) for item in distances[:min(result_limit, len(distances))]]
