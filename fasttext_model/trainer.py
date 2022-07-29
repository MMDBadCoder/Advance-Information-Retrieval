import fasttext

from commons.documents_reader import get_documents

current_path = '/home/mohammad/Desktop/Advanced_Information_Retrieval/hw3/hw3_project/fasttext_model'

all_contents_file_path = current_path + '/all_contents.txt'
documents = get_documents()
with open(all_contents_file_path, 'w') as file:
    for document in documents:
        file.write(document.content)

model = fasttext.train_supervised(all_contents_file_path)
model.save_model(current_path + '/mmd-model.bin')
