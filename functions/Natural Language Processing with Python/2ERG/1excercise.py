from nltk.tokenize import word_tokenize
import numpy as np


sentence1 = "Thomas Jefferson began building Monticello at the age of 26."

token_sequence=str.split(sentence1)
print(token_sequence)
#token_sequence
#Αν θέλω ολόκληρο κείμενο...
#token_sequence=text1.tokens
vocab = sorted(set(token_sequence)) #φτιάξε το λεξιλόγιο αφαιρώντας τα tokens που επαναλαμβάνονται
', '.join(vocab) #Ενώνει τις λέξεις του vocab με κόμα απλά για να τις δούμε
print(vocab)


num_tokens = len(token_sequence)
vocab_size = len(vocab)
#φτιάξε με μηδενικά ένα vector με διαστάσεις αρ_tokens X μέγεθος_λεξιλογίου
onehot_vectors = np.zeros((num_tokens, vocab_size), int)

print(onehot_vectors)

for i, word in enumerate(token_sequence):
    onehot_vectors[i, vocab.index(word)] = 1
' '.join(vocab)

print(onehot_vectors)

