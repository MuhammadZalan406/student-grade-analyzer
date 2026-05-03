def get_grade(marks):
    
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 40:
        return 'D'
    else:
        return 'F'

def get_grade_meaning(grade):
    
    meanings = {
        'A': 'Excellent (90-100)',
        'B': 'Very Good (75-89)',
        'C': 'Good (60-74)',
        'D': 'Average (40-59)',
        'F': 'Fail (Below 40)'
    }
    return meanings.get(grade, '')

def main():
    print("=" * 50)
    print("    STUDENT GRADE CALCULATOR & ANALYZER")
    print("=" * 50)
    
    students = {}
    
    # Input loop
    while True:
        name = input("\nEnter student name (or type 'done' to exit): ")
        if name.lower() == 'done':
            break
        marks = float(input(f"Enter marks for {name} (0-100): "))
        students[name] = marks
    
    if not students:
        print("No student data entered!")
        return
    
    num_students = len(students)
    
    # Calculate statistics
    total_marks = sum(students.values())
    average = total_marks / num_students
    topper = max(students, key=students.get)
    lowest = min(students, key=students.get)
    
    # Pass/Fail
    passed_count = len([m for m in students.values() if m >= 40])
    failed_count = num_students - passed_count
    
    # Grade distribution
    grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for marks in students.values():
        grade = get_grade(marks)
        grades[grade] += 1
    
    # Display results
    print("\n" + "=" * 50)
    print("               ANALYSIS REPORT")
    print("=" * 50)
    
    print(f"\n Total Students: {num_students}")
    print(f" Class Average: {average:.2f}")
    print(f" Top Performer: {topper} ({students[topper]} marks)")
    print(f" Lowest Performer: {lowest} ({students[lowest]} marks)")
    
    print(f"\n Passed Students: {passed_count}")
    print(f" Failed Students: {failed_count}")
    print(f" Pass Percentage: {(passed_count/num_students)*100:.1f}%")
    
    print("\n GRADE DISTRIBUTION:")
    print("-" * 30)
    for grade in ['A', 'B', 'C', 'D', 'F']:
        count = grades[grade]
        if count > 0:
            bar = "▓" * (count * 2)
            print(f"  {grade} ({get_grade_meaning(grade)}): {bar} ({count} students)")
        else:
            print(f"  {grade} ({get_grade_meaning(grade)}): - (0 students)")
    
    # Individual report
    print("\n" + "=" * 50)
    print("          INDIVIDUAL STUDENT REPORT")
    print("=" * 50)
    for name, marks in students.items():
        grade = get_grade(marks)
        status = "PASS " if marks >= 40 else "FAIL "
        print(f"  {name:15} | {marks:5} marks | Grade: {grade} | {status}")

# Run program
if __name__ == "__main__":
    main()
    print("\n" + "=" * 50)
    print(" THANK YOU FOR USING STUDENT GRADE ANALYZER!")
    print("=" * 50)
