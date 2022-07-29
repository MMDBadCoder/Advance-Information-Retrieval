import glob

from commons.document import Document


def get_documents():
    dataset_path = '/home/mohammad/Desktop/Advanced_Information_Retrieval/hw3/hw3_project/dataset'
    files = glob.glob(dataset_path + '/**/*.ham', recursive=True)
    documents = []
    for file_path in files:
        document = Document.read_document_from_file(file_path)
        if document is not None:
            documents.append(document)
    return documents
