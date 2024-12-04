%pprint
import nltk
from nltk.tokenize import word_tokenize
from nltk.book import text2  # Sense and Sensibility

# 1. Απλές προτάσεις στα αγγλικά
english_sentence = "Monticello wasn't designated as UNESCO World Heritage Site until 1987."
greek_sentence = "Η Αθήνα είναι η πρωτεύουσα της Ελλάδας από το 1834!"

# Σύγκριση split() και word_tokenize() για αγγλική πρόταση
print("=== Αγγλική πρόταση ===")
print("Αρχική πρόταση:", english_sentence)
print("split():", english_sentence.split())
print("word_tokenize():", word_tokenize(english_sentence))


# Σύγκριση για ελληνική πρόταση
print("\n=== Ελληνική πρόταση ===")
print("Αρχική πρόταση:", greek_sentence)
print("split():", greek_sentence.split())
print("word_tokenize():", word_tokenize(greek_sentence))


# 2. Πρώτες 200 λέξεις του Sense and Sensibility
sense_text = ' '.join([str(word) for word in text2[:200]])
print("\n=== Απόσπασμα από Sense and Sensibility ===")
print(f"split(): and len : {len(sense_text.split())} ", sense_text.split())
print(f"word_tokenize() and len : {len(word_tokenize(sense_text))}:", word_tokenize(sense_text))



# 3. Πιο περίπλοκη πρόταση με σημεία στίξης και αριθμούς
complex_sentence = "Mr. Smith earned $5,000.50 in 2023! He said: 'That's great...' (but was it?)"
print("\n=== Περίπλοκη πρόταση ===")
print("Αρχική πρόταση:", complex_sentence)
print(f"split(): len:{len(complex_sentence.split())}", complex_sentence.split())
print(f"word_tokenize(): and len:{len(word_tokenize(complex_sentence))}", word_tokenize(complex_sentence))
