from nltk.book import text4, text7
from collections import Counter
from nltk import FreqDist

# 1. Εύρεση των 3 πιο συχνών λέξεων στις πρώτες 50 λέξεις κάθε βιβλίου
text4_first50 = text4[:50]
text7_first50 = text7[:50]

# Χρήση FreqDist για την εύρεση συχνοτήτων
freq_dist_text4 = FreqDist(text4_first50)
freq_dist_text7 = FreqDist(text7_first50)


# Εύρεση των 3 πιο συχνών λέξεων
most_common_text4 = freq_dist_text4.most_common(3)
most_common_text7 = freq_dist_text7.most_common(3)

def creating_posting_list(text):
    posting_dict = {}
    for i , word in enumerate(text):
        if word not in posting_dict:
            posting_dict[word] = []
        posting_dict[word].append(i)
    return posting_dict

#Η posting list είναι μια λίστα που δείχνει σε ποιες θέσεις εμφανίζεται κάθε λέξη στο κείμενο.
posting_list_text4 = creating_posting_list(text4_first50)
posting_list_text7 = creating_posting_list(text7_first50)

print("\nPosting lists για τις 3 ποιο συχνές λεξείς του text4:")
for word , _ in most_common_text4:
    print(f"'{word}': {posting_list_text4[word]}")

print("\nPosting lists για τις 3 πιο συχνές λέξεις του text7:")
for word, _ in most_common_text7:
    print(f"'{word}': {posting_list_text7[word]}")


sentence2 = "Natural Language Processing enables machines to understand human language"
words_sentence2 = sentence2.lower().split()
bow_sentence2 = Counter(words_sentence2)


print("\nBag-of-words για sentence2:")
print(dict(bow_sentence2))

# 4. Bag-of-words για τα πρώτα 50 tokens των text4 και text7
bow_text4 = Counter(text4_first50)
bow_text7 = Counter(text7_first50)

print("\nBag-of-words για τις πρώτες 50 λέξεις του text4:")
print(dict(bow_text4))

print("\nBag-of-words για τις πρώτες 50 λέξεις του text7:")
print(dict(bow_text7))