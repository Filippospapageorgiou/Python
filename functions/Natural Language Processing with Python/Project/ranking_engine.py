import math
from typing import List, Dict, Any
from collections import defaultdict

class RankingEngine:
    def __init__(self, inverted_index):
        self.inverted_index = inverted_index
        self.doc_lengths = self._calculate_doc_lengths()
        
        # Λεξικό με τους διαθέσιμους αλγόριθμους κατάταξης
        self.ranking_algorithms = {
            'boolean': self.boolean_search,
            'tfidf': self.tfidf_search,
            'bm25': self.bm25_search
        }
    
    def _calculate_doc_lengths(self) -> Dict[int, int]:
        """Υπολογίζει το μήκος (αριθμό λέξεων) κάθε εγγράφου"""
        doc_lengths = defaultdict(int)
        for word in self.inverted_index.index:
            for doc_id, info in self.inverted_index.index[word]['documents'].items():
                doc_lengths[doc_id] += info['count']
        return doc_lengths

    def calculate_tf(self, term: str, doc_id: int) -> float:
        """Υπολογίζει το term frequency ενός όρου σε ένα έγγραφο"""
        if term not in self.inverted_index.index:
            return 0.0
        
        doc_info = self.inverted_index.index[term]['documents'].get(doc_id, {})
        if not doc_info:
            return 0.0
        
        return doc_info['count'] / self.doc_lengths[doc_id]

    def calculate_idf(self, term: str) -> float:
        """Υπολογίζει το inverse document frequency ενός όρου"""
        if term not in self.inverted_index.index:
            return 0.0
        
        total_docs = len(self.inverted_index.documents)
        docs_with_term = len(self.inverted_index.index[term]['documents'])
        
        return math.log(total_docs / (1 + docs_with_term))

    def tfidf_search(self, query_terms: List[str]) -> Dict[int, float]:
        """Υπολογίζει το TF-IDF score για κάθε έγγραφο"""
        scores = defaultdict(float)
        
        for term in query_terms:
            idf = self.calculate_idf(term)
            for doc_id in self.inverted_index.index.get(term, {}).get('documents', {}):
                tf = self.calculate_tf(term, doc_id)
                scores[doc_id] += tf * idf
        
        return dict(scores)

    def boolean_search(self, query_terms: List[str]) -> Dict[int, float]:
        """Boolean αναζήτηση (για συμβατότητα με το υπάρχον σύστημα)"""
        # Χρησιμοποιεί την υπάρχουσα boolean αναζήτηση και επιστρέφει 1.0 για κάθε έγγραφο
        results = {}
        for term in query_terms:
            docs = self.inverted_index.get_format_for_term(term).get('documents', {})
            for doc_id in docs:
                results[doc_id] = 1.0
        return results

    def bm25_search(self, query_terms: List[str]) -> Dict[int, float]:
        """
        Υλοποίηση του BM25 αλγορίθμου.
        BM25 παράμετροι: k1 = 1.5, b = 0.75 (τυπικές τιμές)
        """
        k1 = 1.5  # term frequency saturation parameter
        b = 0.75  # length normalization factor

        # Υπολογισμός του μέσου μήκους εγγράφων
        avg_doc_length = sum(self.doc_lengths.values()) / \
        len(self.doc_lengths) if self.doc_lengths else 0

        scores = defaultdict(float)
        N = len(self.inverted_index.documents)  # συνολικός αριθμός εγγράφων

        for term in query_terms:
            if term not in self.inverted_index.index:
                continue

            # Αριθμός εγγράφων που περιέχουν τον όρο
            n = len(self.inverted_index.index[term]['documents'])

            # Υπολογισμός IDF για BM25
            idf = math.log((N - n + 0.5) / (n + 0.5) + 1)

            for doc_id, doc_info in self.inverted_index.index[term]['documents'].items():
                # Term frequency στο τρέχον έγγραφο
                tf = doc_info['count']

                # Μήκος του τρέχοντος εγγράφου
                doc_length = self.doc_lengths[doc_id]

                # Υπολογισμός του BM25 score για τον όρο
                numerator = tf * (k1 + 1)
                denominator = tf + k1 * (1 - b + b * doc_length / avg_doc_length)

                score = idf * numerator / denominator
                scores[doc_id] += score

        return dict(scores)


    def rank_documents(self, query_terms: List[str], algorithm:str) -> Dict[int, Dict[str, Any]]:
        """
        Κατατάσσει τα έγγραφα με βάση τον επιλεγμένο αλγόριθμο
        """
        if algorithm not in self.ranking_algorithms:
            raise ValueError(f"Μη έγκυρος αλγόριθμος: {algorithm}")
            
        # Παίρνουμε τα scores από τον επιλεγμένο αλγόριθμο
        scores = self.ranking_algorithms[algorithm](query_terms)
        
        # Δημιουργούμε τα αποτελέσματα με τους τίτλους και τα scores
        results = {}
        for doc_id, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
            results[doc_id] = {
                'title': self.inverted_index.documents[doc_id]['title'],
                'score': score
            }
            
        return results