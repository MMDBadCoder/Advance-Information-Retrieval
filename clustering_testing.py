import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from hazm import word_tokenize
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import seaborn

from commons.documents_reader import get_documents


def get_stopwords():
    file_path = '/home/mohammad/Desktop/Advanced_Information_Retrieval/hw3/hw3_project/commons/stopwords.txt'
    with open(file_path, 'r') as file:
        return list(set([line.replace('\n', '') for line in file.readlines()]))


def print_top_features_of_clusters(prediction, n_features):
    plt.figure(figsize=(8, 4))
    labels = np.unique(prediction)
    for label in labels:
        cluster_features = np.where(prediction == label)
        x_means = np.mean(tf_idf_array[cluster_features], axis=0)  # returns average score across cluster
        sorted_means = np.argsort(x_means)[::-1][:n_features]  # indices with top 20 scores
        best_features = [(all_features[i], x_means[i]) for i in sorted_means]
        df = pd.DataFrame(best_features, columns=['features', 'score'])
        plt.title(("Most occurred words of cluster " + str(label)), fontsize=10, fontweight='bold')
        seaborn.barplot(x='score', y='features', orient='h', data=df[:n_features])
        print(df[:n_features])
        plt.show()


titles = [document.content.split('\n')[0] for document in get_documents()]
stopwords = get_stopwords()

tf_idf_vectorizor = TfidfVectorizer(norm='l2', tokenizer=word_tokenize, stop_words=stopwords)
tf_idf = tf_idf_vectorizor.fit_transform(titles)
tf_idf_array = tf_idf.toarray()
all_features = tf_idf_vectorizor.get_feature_names_out()
final_df_array = pd.DataFrame(data=tf_idf_array, columns=all_features).to_numpy()

kmeans = KMeans(n_clusters=8, random_state=13, max_iter=2000, verbose=False)
kmeans.fit(tf_idf_array)

prediction = kmeans.predict(final_df_array)
print_top_features_of_clusters(prediction, 10)
