import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

def clean_text(text , language='english'):
    tokens = word_tokenize(text)
    
    # Αφαίρεση σημείων στίξης
    tokens_no_punct = [token for token in tokens if token not in string.punctuation]
    
    # Αφαίρεση stopwords
    stop_words = set(stopwords.words(language))
    clean_tokens = [token for token in tokens_no_punct if token.lower() not in stop_words]
    
    return clean_tokens

# Ερώτηση 7: Πλήθος stopwords
print("=== Πλήθος Stopwords ===")
print(f"Αγγλικά stopwords: {len(stopwords.words('english'))}")
print(f"Ελληνικά stopwords: {len(stopwords.words('greek'))}")

# Ερώτηση 8: Δοκιμή με διάφορα κείμενα
# 1. Αγγλικό κείμενο
english_text = """The family of Dashwood had long been settled in Sussex. Their estate was large, 
                 and their residence was at Norland Park, in the centre of their property, where, 
                 for many generations, they had lived in so respectable a manner as to engage the 
                 general good opinion of their surrounding acquaintance."""


# 2. Ελληνικό κείμενο
greek_text = """Η Αθήνα είναι η πρωτεύουσα της Ελλάδας και μία από τις αρχαιότερες πόλεις 
                στον κόσμο. Η ιστορία της ξεκινά από την αρχαιότητα και συνεχίζεται μέχρι σήμερα."""

print("\n=== Καθαρισμός Κειμένων ===")
print("Αγγλικό κείμενο:")
print("Πριν:", word_tokenize(english_text)[:10], "...")
print("Μετά:", clean_text(english_text)[:10], "...")

print("\nΕλληνικό κείμενο:")
print("Πριν:", word_tokenize(greek_text)[:10], "...")
print("Μετά:", clean_text(greek_text, 'greek')[:10], "...")


# Ερώτηση 9: Κατανομή συχνότητας
def plot_frequency_distribution(tokens, title):
    fdist = FreqDist(tokens)
    fdist.plot(20, title=title)

# Για το αγγλικό κείμενο
original_tokens = word_tokenize(english_text)
clean_tokens = clean_text(english_text)

print("\n=== Κατανομή Συχνότητας ===")
plot_frequency_distribution(original_tokens, "Original Text Frequency")
plot_frequency_distribution(clean_tokens, "Clean Text Frequency")


plt.show()