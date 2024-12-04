%pprint
from nltk.book import *
from nltk.tokenize import word_tokenize
from collections import Counter

#Ασκήση 1.
#Ερώτηση 1α:

def vocabulary_richness(text):
    tokens = text.tokens
    unique_tokens = set(tokens)
    vocabulary_size = len(unique_tokens)
    totak_tokens = len(tokens)
    
    return vocabulary_size , totak_tokens

# Υπολογισμός για το "Monty Python and the Holy Grail" (text6)
monty_vocabulary_size, monty_total_tokens = vocabulary_richness(text6)



launcelot_count = text6.count("LAUNCELOT")
launcelot_perc = ( launcelot_count / monty_total_tokens ) * 100
print(f"Monty Python - Tokens Size: {monty_total_tokens}")
print(f"Monty Python - Vocabulary Size: {monty_vocabulary_size}")
print(f"LAUNCELOT Count: {launcelot_count}, Percentage: {launcelot_perc:.2f}%\n")



chat_vocab_size , chat_total_tokens = vocabulary_richness(text5)

omg_count = text5.count("omg") + text5.count("OMG")
lol_count = text5.count("lol")

omg_perc = (omg_count / chat_total_tokens ) * 100
lol_perc = (lol_count / chat_total_tokens ) * 100

print(f"Chat Corpus - Vocabulary Size: {chat_vocab_size}")
print(f"OMG Count: {omg_count}, Percentage: {omg_perc:.2f}%")
print(f"lol Count: {lol_count}, Percentage: {lol_perc:.2f}%")


fdist6 = FreqDist(text6)

print(fdist6.most_common(50))

fdist5 = FreqDist(text5)


