from commons.document import Document


class BooleanSearcher:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.documents_by_tokens = {}

    def add_documents(self, documents):
        for document in documents:
            self.__add_document(document)

    def __add_document(self, document):
        tokens = self.tokenizer.tokenize(document.content)
        for token in tokens:
            if not self.documents_by_tokens.__contains__(token):
                self.documents_by_tokens[token] = set()
            self.documents_by_tokens[token].add(document.id)

    def get_included_documents_set(self, token):
        if self.documents_by_tokens.__contains__(token):
            return self.documents_by_tokens[token]
        else:
            return set()

    def search(self, query_text, result_limit=10):
        query_tokens = self.tokenizer.tokenize(query_text)
        query_tokens_included_sets = [self.get_included_documents_set(qt) for qt in query_tokens]
        result_doc_ids = list(set.intersection(*query_tokens_included_sets)) + \
                         list(set.union(*query_tokens_included_sets))
        result_doc_ids = result_doc_ids[:result_limit]
        return [Document.get_document_by_id(doc_id) for doc_id in result_doc_ids]
