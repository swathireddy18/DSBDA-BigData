from sklearn.feature_extraction.text import TfidfVectorizer
def compute_tfidf_from_file(file_path):
with open(file_path, 'r') as file:
documents file.readlines()
vectorizer TfidfVectorizer()
tfidf_matrix vectorizer.fit_transform(documents)
feature_names vectorizer.get_feature_names_out()
for i, doc in enumerate(documents):
print(f"Document (1+1) TF-IDF scores:")
for word, score in zip(feature_names, tfidf_matrix[i].toarray()[0]):
if score > 8: #Only print words with a non-zero score
print(f" (word): (score:.4f)")
print("\n")
file path "doc.txt" # Replace this with the path to your text file
compute_tfidf_from_file(file_path)
