%pprint
import nltk
from nltk.book import *
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer


sent1 #εμφάνισε την sent1 του βιβλίου 1 
tokens1=sent1 #βάλε την sent1 στην μεταβλητή token1 
normalized_sent1=[x.lower() for x in tokens1] #για κάθε x που υπάρχει 
#στο token1 κάνε "μικρά" τα γράμματα 
print(normalized_sent1)
print("\n")


# Αρχικό κείμενο
text = "The quick brown foxes jump quickly over the lazy dogs. The dogs are very lazy today running proggraming."

# Tokenization
tokens = nltk.word_tokenize(text)

# Αφαίρεση stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

print("Αρχικά tokens:", filtered_tokens)
print("\n")
porter = PorterStemmer()
stemmed_tokens = [porter.stem(word) for word in filtered_tokens]


print("Stemmed tokens:", stemmed_tokens)

print("\n")

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

print("Lemmatized tokens:", lemmatized_tokens)

#lemmatization αντιστοιχίζει τις λέξεις στη βασική τους μορφή (λήμμα). Αυτές οι τεχνικές μπορούν να βελτιώσουν την απόδοση σε εφαρμογές επεξεργασίας φυσικής γλώσσας, καθώς μειώνουν την πολυπλοκότητα των κειμένων.