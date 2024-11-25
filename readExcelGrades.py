import pandas as pd



def analyze_grades(filepath):
    try:
        # Read the CSV file
        df = pd.read_csv(filepath)
        
        #Remove any rows where NaN
        df_clean = df.dropna()
        #Calculate statistics
        total_students = len(df)
        valid_grades = df_clean.iloc[:,1] # Taking second column as grades
        average_grade = valid_grades.mean()
        

        specific_id = 21390174
        # Search for the specific ID in the "ΑΜ" column
        result = df_clean[df_clean['ΑΜ'] == specific_id]
        if not result.empty:
            print(f"Details for ID {specific_id}:")
            print(result)
        else:
            print(f"Details for ID {specific_id} not found")
                
        #Calculate passing and failing precentages
        passing_grades = valid_grades[valid_grades >= 5]
        failing_grades = valid_grades[valid_grades < 5]
        
        passing_precentage = (len(passing_grades) / len(valid_grades)) * 100
        failing_precentage = (len(failing_grades) / len(valid_grades)) * 100
    
        results = {
            'total_students':total_students,
            'students_with_grades':len(valid_grades),
            'average_grade':round(average_grade),
            'passing_students':len(passing_grades),
            'failing_students':len(failing_grades),
            'passing_percentage':round(passing_precentage),
            'failing_percentage':round(failing_precentage)
        }
        
        return results
        
    except Exception as e:
        print(f"Error analyzing grades: {str(e)}")
        return None

def print_analytics(results):
    if results:
       print("\n=== Grade Analysis Results ===")
       print(f"Total number of students: {results['total_students']}")
       print(f"Students with grades: {results['students_with_grades']}")
       print(f"Average grade: {results['average_grade']}")
       print("\nPass/Fail Statistics:")
       print(f"Passing students (≥5): {results['passing_students']} ({results['passing_percentage']}%)")
       print(f"Failing students (<5): {results['failing_students']} ({results['failing_percentage']}%)")


filepath = "grades.csv"
results = analyze_grades(filepath)
print_analytics(results)
    
    
    