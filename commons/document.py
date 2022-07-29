class Document:
    document_by_id = {}

    def __init__(self, id, content):
        self.id = id
        self.content = content
        Document.document_by_id[id] = self

    def read_document_from_file(file_path: str):
        with open(file_path, 'r') as file:
            file_name = file_path.split('/')[-1]
            return Document(file_name, '\n'.join(file.readlines()))

    def get_document_by_id(id):
        return Document.document_by_id[id]
