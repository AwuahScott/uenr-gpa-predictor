from data_handler import load_data, save_data
from gpa_calc import calculate_cgpa, predict_target

def convert_grade_to_point(grade):
    """Maps standard UENR letter grades to credit points."""
    mapping = {'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0}
    return mapping.get(grade.upper(), -1.0)

def main():
    print("=== UENR Student CGPA & Target Predictor ===")
    records = load_data()
    
    while True:
        print("\n1. Add Course Grade\n2. View Academic Progress & CGPA\n3. Run Graduation Target Predictor\n4. Exit")
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            sem = input("Enter Semester (e.g., Sem1, Sem2): ")
            course_name = input("Enter Course Code/Name: ")
            try:
                credits = int(input("Enter Credit Hours (e.g., 2, 3): "))
            except ValueError:
                print("Invalid input. Credit hours must be a number.")
                continue
                
            grade = input("Enter Grade Obtained (A, B+, B, C+, C, D+, D, F): ").upper()
            gp = convert_grade_to_point(grade)
            
            if gp == -1.0:
                print("Invalid UENR grade entered.")
                continue
                
            if sem not in records:
                records[sem] = []
            
            records[sem].append({"course": course_name, "credits": credits, "grade_point": gp, "grade": grade})
            save_data(records)
            print(f"Successfully added {course_name} to {sem}!")
            
        elif choice == "2":
            if not records:
                print("No academic records found. Add courses first.")
                continue
            
            for sem, courses in records.items():
                print(f"\n--- {sem} ---")
                for c in courses:
                    print(f"  * {c['course']} | Credits: {c['credits']} | Grade: {c['grade']}")
            
            cgpa, total_cr = calculate_cgpa(records)
            print(f"\n👉 Current Total Credits: {total_cr}")
            print(f"👉 Current Cumulative GPA (CGPA): {cgpa}")
            
        elif choice == "3":
            cgpa, total_cr = calculate_cgpa(records)
            if total_cr == 0:
                print("Please add your current grades first to run a prediction.")
                continue
                
            try:
                target = float(input("Enter your target graduation CGPA (e.g., 3.60 for First Class): "))
                rem_credits = int(input("Enter total remaining credits left to graduate: "))
            except ValueError:
                print("Invalid numerical inputs.")
                continue
                
            req_gpa = predict_target(cgpa, total_cr, target, rem_credits)
            
            if req_gpa is None:
                print("Error calculating remaining credits.")
            elif req_gpa > 4.0:
                print(f"⚠️ Target mathematically impossible. Required GPA is {req_gpa} (Max UENR GPA is 4.0).")
            elif req_gpa <= 0:
                print(f"🎉 Excellent! You have already met your target thresholds. Keep up your current pace.")
            else:
                print(f"🎯 To graduate with a CGPA of {target}, you must average a **{req_gpa} GPA** over your remaining {rem_credits} credits.")
                
        elif choice == "4":
            print("Exiting application. Best of luck with your studies at UENR!")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()
