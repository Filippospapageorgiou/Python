import numpy as np
from typing import List, Dict, Set
from collections import defaultdict

class SearchEvaluator:
    def __init__(self, search_engine, ranking_engine):
        self.search_engine = search_engine
        self.ranking_engine = ranking_engine
        
        # Δημιουργία test queries με τα αναμενόμενα σχετικά έγγραφα
        self.test_queries = {
            "python programming": {
                "relevant_docs": {
                    "Python (programming language) - Wikipedia",
                    "Computer programming - Wikipedia"
                },
                "description": "Basic programming query"
            },
            "machine learning AI": {
                "relevant_docs": {
                    "Machine learning - Wikipedia",
                    "Artificial intelligence - Wikipedia",
                    "Deep learning - Wikipedia"
                },
                "description": "AI-related query"
            },
            "database security": {
                "relevant_docs": {
                    "Database management system - Wikipedia",
                    "Computer security - Wikipedia",
                    "Information security - Wikipedia"
                },
                "description": "Security-focused query"
            },
            "web development": {
                "relevant_docs": {
                    "Web development - Wikipedia",
                    "Software engineering - Wikipedia",
                    "Computer programming - Wikipedia"
                },
                "description": "Web development query"
            },
            "cloud computing networks": {
                "relevant_docs": {
                    "Cloud computing - Wikipedia",
                    "Computer networks - Wikipedia",
                    "Distributed computing - Wikipedia"
                },
                "description": "Network-related query"
            }
        }

    def precision(self, retrieved: Set[str], relevant: Set[str]) -> float:
        """Υπολογίζει την ακρίβεια (precision)"""
        if not retrieved:
            return 0.0
        return len(retrieved.intersection(relevant)) / len(retrieved)

    def recall(self, retrieved: Set[str], relevant: Set[str]) -> float:
        """Υπολογίζει την ανάκληση (recall)"""
        if not relevant:
            return 0.0
        return len(retrieved.intersection(relevant)) / len(relevant)

    def f1_score(self, precision: float, recall: float) -> float:
        """Υπολογίζει το F1-score"""
        if precision + recall == 0:
            return 0.0
        return 2 * (precision * recall) / (precision + recall)

    def average_precision(self, retrieved: List[str], relevant: Set[str]) -> float:
        """Υπολογίζει το average precision για ένα query"""
        hits = 0
        sum_precision = 0.0
        
        for i, doc in enumerate(retrieved, 1):
            if doc in relevant:
                hits += 1
                sum_precision += hits / i
                
        return sum_precision / len(relevant) if relevant else 0.0

    def evaluate_algorithm(self, algorithm: str = 'tfidf', k: int = 10) -> Dict:
        """Αξιολογεί έναν συγκεκριμένο αλγόριθμο κατάταξης"""
        metrics = defaultdict(list)
        
        print(f"\nΛεπτομερή αποτελέσματα για {algorithm}:")
        print("-" * 40)
        
        for query, info in self.test_queries.items():
            print(f"\nQuery: {query}")
            
            # Λήψη αποτελεσμάτων
            if algorithm == 'boolean':
                results = self.search_engine.search(query)
            else:
                query_terms = self.search_engine.preprocess_query(query)
                results = self.ranking_engine.rank_documents(query_terms, algorithm)
            
            # Μετατροπή αποτελεσμάτων σε τίτλους
            retrieved_titles = {self.search_engine.inverted_index.documents[doc_id]['title'] 
                              for doc_id in list(results.keys())[:k]}
            
            print(f"Retrieved titles: {retrieved_titles}")
            print(f"Relevant docs: {info['relevant_docs']}")
            
            # Υπολογισμός μετρικών
            prec = self.precision(retrieved_titles, info['relevant_docs'])
            rec = self.recall(retrieved_titles, info['relevant_docs'])
            f1 = self.f1_score(prec, rec)
            ap = self.average_precision(list(retrieved_titles), info['relevant_docs'])
            
            print(f"Precision: {prec:.4f}")
            print(f"Recall: {rec:.4f}")
            print(f"F1: {f1:.4f}")
            print(f"AP: {ap:.4f}")
            
            metrics['precision'].append(prec)
            metrics['recall'].append(rec)
            metrics['f1'].append(f1)
            metrics['ap'].append(ap)
        
        # Υπολογισμός μέσων τιμών
        return {
            'mean_precision': np.mean(metrics['precision']),
            'mean_recall': np.mean(metrics['recall']),
            'mean_f1': np.mean(metrics['f1']),
            'map': np.mean(metrics['ap']),
            'details': metrics
        }
        """Αξιολογεί έναν συγκεκριμένο αλγόριθμο κατάταξης"""
        metrics = defaultdict(list)
        
        for query, info in self.test_queries.items():
            # Λήψη αποτελεσμάτων
            if algorithm == 'boolean':
                results = self.search_engine.search(query)
            else:
                query_terms = self.search_engine.preprocess_query(query)
                results = self.ranking_engine.rank_documents(query_terms, algorithm)
            
            # Μετατροπή αποτελεσμάτων σε τίτλους
            retrieved_titles = {self.search_engine.inverted_index.documents[doc_id]['title'] 
                              for doc_id in list(results.keys())[:k]}
            
            # Υπολογισμός μετρικών
            prec = self.precision(retrieved_titles, info['relevant_docs'])
            rec = self.recall(retrieved_titles, info['relevant_docs'])
            f1 = self.f1_score(prec, rec)
            ap = self.average_precision(list(retrieved_titles), info['relevant_docs'])
            
            metrics['precision'].append(prec)
            metrics['recall'].append(rec)
            metrics['f1'].append(f1)
            metrics['ap'].append(ap)
            
        # Υπολογισμός μέσων τιμών
        return {
            'mean_precision': np.mean(metrics['precision']),
            'mean_recall': np.mean(metrics['recall']),
            'mean_f1': np.mean(metrics['f1']),
            'map': np.mean(metrics['ap']),  # Mean Average Precision
            'details': metrics
        }

    def compare_algorithms(self, k: int = 10):
        """Συγκρίνει όλους τους διαθέσιμους αλγόριθμους"""
        algorithms = ['boolean', 'tfidf', 'bm25']
        results = {}
        
        for alg in algorithms:
            results[alg] = self.evaluate_algorithm(alg, k)
            
        self.print_evaluation_results(results)
        
    def print_evaluation_results(self, results: Dict):
        """Εκτύπωση των αποτελεσμάτων αξιολόγησης"""
        print("\nΑξιολόγηση Αλγορίθμων Αναζήτησης")
        print("=" * 50)
        
        for alg, metrics in results.items():
            print(f"\nΑλγόριθμος: {alg.upper()}")
            print("-" * 30)
            print(f"Mean Precision: {metrics['mean_precision']:.4f}")
            print(f"Mean Recall: {metrics['mean_recall']:.4f}")
            print(f"Mean F1-Score: {metrics['mean_f1']:.4f}")
            print(f"MAP: {metrics['map']:.4f}")