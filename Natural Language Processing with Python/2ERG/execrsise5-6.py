from nltk.book import text4, text7
from sklearn.feature_extraction.text import CountVectorizer
import math

def cosine_similarity(vec1,vec2):
    # Υπολογισμός ομοιότητας συνημίτονων
    dot_product = sum(v1 * v2 for v1,v2 in zip(vec1,vec2))
    norm1 = math.sqrt(sum(v1 * v1 for v1 in vec1))
    norm2 = math.sqrt(sum(v2 * v2 for v2 in vec2))
    return dot_product/ (norm1 * norm2) if norm1 and norm2 else 0

# 1. Ομοιότητα για τις πρώτες 50 λέξεις
text4_first50 = text4[:50]
text7_first50 = text7[:50]

# Μετατροπή σε strings
text4_str_50 = ' '.join(text4_first50)
text7_str_50 = ' '.join(text7_first50)

vectorizer_50 = CountVectorizer()
vectors_50 = vectorizer_50.fit_transform([text4_str_50, text7_str_50])
feature_names_50 = vectorizer_50.get_feature_names_out()


# Μετατροπή σε arrays
arr4_50 = vectors_50[0].toarray()[0]
arr7_50 = vectors_50[1].toarray()[0]


# Υπολογισμός ομοιότητας συνημίτονων για τις προτάσεις
similarity_50 = cosine_similarity(arr4_50, arr7_50)

print("Ομοιότητα συνημίτονων για τις πρώτες 50 λέξεις:")
print(f"Cosine Similarity = {similarity_50:.4f}")

# 2. Ομοιότητα για ολόκληρα τα βιβλία
text4_full = ' '.join(text4)
text7_full = ' '.join(text7)

# Δημιουργία vectorizer για τα πλήρη κείμενα
vectorizer_full = CountVectorizer()
vectors_full = vectorizer_full.fit_transform([text4_full, text7_full])
feature_names_full = vectorizer_full.get_feature_names_out()

# Μετατροπή σε arrays
arr4_full = vectors_full[0].toarray()[0]
arr7_full = vectors_full[1].toarray()[0]

# Υπολογισμός ομοιότητας συνημίτονων για τα πλήρη κείμενα
similarity_full = cosine_similarity(arr4_full, arr7_full)

print("\nΟμοιότητα συνημίτονων για ολόκληρα τα βιβλία:")
print(f"Cosine Similarity = {similarity_full:.4f}")

# Επιπλέον ανάλυση
print("\nΣτατιστικά στοιχεία:")
print(f"Αριθμός μοναδικών λέξεων στις πρώτες 50 λέξεις: {len(feature_names_50)}")
print(f"Αριθμός μοναδικών λέξεων σε ολόκληρα τα βιβλία: {len(feature_names_full)}")