%pprint
from nltk.book import *
from nltk.probability import FreqDist
import matplotlib.pyplot as plt



# Δημιουργία κατανομής συχνότητας για το text1
fdist1 = FreqDist(text1)

# Εμφάνιση της κατανομής συχνότητας (απλά εκτυπώνει το αντικείμενο)
print(fdist1)

# Εμφάνιση των 50 πιο κοινών tokens με τις συχνότητές τους
print(fdist1.most_common(50))

# Σχεδίαση γραφήματος για τα 50 πιο κοινά tokens
fdist1.plot(50)
plt.show()


