import re
from typing import List ,Dict ,Any
from project import  InvertedIndex
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class SearchEngine:
    def __init__(self, inverted_index:InvertedIndex):
        self.inverted_index = inverted_index
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.operators = {'AND','OR','NOT','(',')'}
        
    def preprocess_query(self, query: str) -> List[str]:
        query = query.replace('(', ' ( ').replace(')', ' ) ')
        tokens = query.split()
        
        processed_tokens = []
        
        
        for i,token in enumerate(tokens):
            if token.upper() in self.operators:
                processed_tokens.append(token.upper())
            else:
                token = re.sub(r'[^a-zA-Z0-9\s]', '', token.lower())
                if len(token)>1 and token not in self.stop_words:
                    processed_tokens.append(self.lemmatizer.lemmatize(token,'v'))
                    if i + 1 < len(tokens) and tokens[i + 1].upper() not in self.operators:
                        processed_tokens.append('AND')

         
        return processed_tokens
    
    def search(self, query: str) -> Dict[int, Dict[str, Any]]:
        tokens = self.preprocess_query(query)
    
        if not tokens:
            return {}

        # Αν έχουμε μόνο μία λέξη
        if len(tokens) == 1:
            result = self.inverted_index.get_format_for_term(tokens[0])
            return result.get('documents', {})

    
        current_docs = None
        current_op = None
        i = 0

        while i < len(tokens):
            token = tokens[i]
        
            if token in {'AND', 'OR', 'NOT'}:
                current_op = token
                i += 1
                continue

            term_docs = set(self.inverted_index.get_format_for_term(token).get('documents', {}).keys())

            if current_docs is None:
                current_docs = term_docs
            else:
                if current_op == 'AND':
                    current_docs = current_docs & term_docs
                elif current_op == 'OR':
                    current_docs = current_docs | term_docs
                elif current_op == 'NOT':
                    current_docs = current_docs - term_docs

            i += 1

        results = {}
        if current_docs:
            for doc_id in current_docs:
                results[doc_id] = {
                    'title': self.inverted_index.documents[doc_id]['title'],
                    'count': 1
                    }   

        return results
            
        
    
    def run(self):  
        while True:
            query = input("\nΕρώτημα: ").strip()
            if query.lower() == 'exit':
                break
            
            results = self.search(query)
            if results:
                print(f"\nΒρέθηκαν {len(results)} αποτελέσματα:")
                for doc_id, doc_info in results.items():
                    print(f"- {doc_info['title']}")
            else:
                print("Δεν βρέθηκαν αποτελέσματα.")
                
            
                
                
                
                
                
                
                
                
                