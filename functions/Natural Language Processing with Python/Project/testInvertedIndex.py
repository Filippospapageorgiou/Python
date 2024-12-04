from project import InvertedIndex
from searchEngine import SearchEngine
from ranking_engine import RankingEngine

def main():
    # Αρχικοποίηση του inverted index
    inverted_index = InvertedIndex()
    inverted_index.load_processed_data('processed_webpage_data.json')
    inverted_index.build_index()
    
    # Αρχικοποίηση της μηχανής αναζήτησης
    search_engine = SearchEngine(inverted_index)
    
    # Αρχικοποίηση της μηχανής κατάταξης
    ranking_engine = RankingEngine(inverted_index)
    
    print("\nΔιαθέσιμοι αλγόριθμοι αναζήτησης:")
    print("1. Boolean Search")
    print("2. TF-IDF Ranking")
    print("3. BM25 Ranking")
    
    while True:
        try:
            choice = input("\nΕπιλέξτε αλγόριθμο (1-3) ή 'exit' για έξοδο: ")
            
            if choice.lower() == 'exit':
                break
                
            if choice == '1':
                search_engine.run()  # Χρήση του υπάρχοντος boolean search
            elif choice == '2':
                algorithm = 'tfidf'
                query = input("\nΕρώτημα: ").strip()
                
                if query.lower() == 'exit':
                    break
                    
                # Προεπεξεργασία του ερωτήματος
                query_terms = search_engine.preprocess_query(query)
                results = ranking_engine.rank_documents(query_terms, algorithm)
                
                if results:
                    print(f"\nΒρέθηκαν {len(results)} αποτελέσματα:")
                    for doc_id, info in results.items():
                        print(f"- {info['title']} (score: {info['score']:.4f})")
                else:
                    print("Δεν βρέθηκαν αποτελέσματα.")
            elif choice =='3':
                algorithm = 'bm25'
                query = input("\nΕρώτημα: ").strip()
                
                if query.lower() == 'exit':
                    break
                    
                # Προεπεξεργασία του ερωτήματος
                query_terms = search_engine.preprocess_query(query)
                results = ranking_engine.rank_documents(query_terms, algorithm)
                
                if results:
                    print(f"\nΒρέθηκαν {len(results)} αποτελέσματα:")
                    for doc_id, info in results.items():
                        print(f"- {info['title']} (score: {info['score']:.4f})")
                else:
                    print("Δεν βρέθηκαν αποτελέσματα.")
            else:
                continue
        except KeyboardInterrupt:
            print("\nΈξοδος από το πρόγραμμα...")
            break
        except Exception as e:
            print(f"Σφάλμα: {e}")

if __name__ == "__main__":
    main()