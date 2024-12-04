from project import InvertedIndex
from searchEngine import SearchEngine
from ranking_engine import RankingEngine
from evaluation import SearchEvaluator

def main():
    # Αρχικοποίηση των απαραίτητων components
    inverted_index = InvertedIndex()
    inverted_index.load_processed_data('processed_webpage_data.json')
    inverted_index.build_index()
    
    search_engine = SearchEngine(inverted_index)
    ranking_engine = RankingEngine(inverted_index)
    
    # Δημιουργία του evaluator
    evaluator = SearchEvaluator(search_engine, ranking_engine)
    
    # Εκτέλεση της αξιολόγησης
    print("Εκτέλεση αξιολόγησης συστήματος...")
    evaluator.compare_algorithms(k=10)

if __name__ == "__main__":
    main()