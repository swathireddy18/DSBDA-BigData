from sklearn.feature_extraction.text import TfidfVectorizer

def compute_tfidf_from_file(file_path):
    # Read file content
    with open(file_path, 'r') as file:
        documents = file.readlines()  # wrap in a list if it’s a single document

    # Create the vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()

    # Print out the TF-IDF score for each word
    for i, doc in enumerate(documents):
        print(f"Document {i + 1} TF-IDF scores:")
        for word, score in zip(feature_names, tfidf_matrix[i].toarray()[0]):
            if score > 0:
                print(f"{word}: {score:.4f}")
        print("\n")

# Example usage
file_path = "/content/demo.txt"
compute_tfidf_from_file(file_path)
