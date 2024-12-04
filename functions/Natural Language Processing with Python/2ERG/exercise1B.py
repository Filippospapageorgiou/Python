from nltk.book import text4, text7
from nltk import FreqDist

text4_first50 = text4[:50]
text7_first50 = text7[:50]
# Παίρνουμε τις πρώτες 50 λέξεις από κάθε κείμενο


# Μετατρέπουμε σε σύνολα για να βρούμε τις κοινές λέξεις
set_text4 = set(text4_first50)
set_text7 = set(text7_first50)

#βρισκούμε τις κοινές λεξείς 
common_words = set_text4.intersection(set_text7)

#υπολογιζούμε την ομοιότητα Jaccard
jaccard_similarity = len(common_words) / len(set_text4.union(set_text7))
print(jaccard_similarity)

print("Πρώτες 50 λέξεις του text4:")
print(text4_first50)
print("\nΠρώτες 50 λέξεις του text7:")
print(text7_first50)
print("\nΚοινές λέξεις:")
print(common_words)
print(f"\nΟμοιότητα Jaccard: {jaccard_similarity:.4f}")

# Εμφάνιση συχνότητας κοινών λέξεων
print("\nΣυχνότητα εμφάνισης κοινών λέξεων:")
freq_text4 = FreqDist(text4_first50)
freq_text7 = FreqDist(text7_first50)

for word in common_words:
    print(f"Λέξη '{word}':")
    print(f"  Συχνότητα στο text4: {freq_text4[word]}")
    print(f"  Συχνότητα στο text7: {freq_text7[word]}")