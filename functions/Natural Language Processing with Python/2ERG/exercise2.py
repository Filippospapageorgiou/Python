from nltk.tokenize import word_tokenize
from collections import defaultdict

sentence1 = "Thomas Jefferson began building Monticello at the age of 26."
sentence2 = "Natural Language Processing enables machines to understand human language."

tokens1_manual = sentence1.split()  # Χωρίζουμε με βάση τα κενά
tokens2_manual = sentence2.split()



tokens1_nltk = word_tokenize(sentence1)
tokens2_nlkt = word_tokenize(sentence2)


def create_cooccurrence_matrix(tokens):
    cooccurrence_matrix = defaultdict(lambda: defaultdict(int))
    for i , word in enumerate(tokens):
        for j in range(max(0,i-1),min(len(tokens),i+2)):
            if i != j:
                cooccurrence_matrix[word][tokens[j]] += 1
    return cooccurrence_matrix



# Πίνακας Συμπτώσεων για κάθε μέθοδο
print("manual : \n")
cooccurrence_manual_1 = create_cooccurrence_matrix(tokens1_manual)
cooccurrence_manual_2 = create_cooccurrence_matrix(tokens2_manual)

print(cooccurrence_manual_1)
print(cooccurrence_manual_2)

print("\ntokens : \n")
cooccurrence_nltk_1 = create_cooccurrence_matrix(tokens1_nltk)
cooccurrence_nltk_2 = create_cooccurrence_matrix(tokens2_nlkt)

print(cooccurrence_nltk_1)
print(cooccurrence_nltk_2)
