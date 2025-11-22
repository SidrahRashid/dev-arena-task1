def grade_from_marks(marks):
    if marks < 0 or marks > 100:
        return None, "Invalid marks! Must be between 0 and 100."

    if marks >= 90:
        return "A+", "Outstanding! You're performing at the highest level!"
    elif marks >= 80:
        return "A", "Great job! Keep up this excellent performance!"
    elif marks >= 70:
        return "B", "Well done! You're doing good—aim a little higher!"
    elif marks >= 60:
        return "C", "Not bad! You can definitely improve with a little more effort."
    elif marks >= 50:
        return "D", "You're close! Put in a bit more work and you'll do much better."
    else:
        return "F", "Don't be discouraged! Every failure is a step towards success. Try again!"

GRADE_POINTS = {
    "A+": 4.0,
    "A": 3.7,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

def grade_point_from_grade(grade):
    return GRADE_POINTS.get(grade, 0.0)

def calculate_gpa(marks_list):
    if not marks_list:
        return 0.0, 0.0, []

    per_subject = []
    total_points = 0.0
    total_marks = 0.0

    for m in marks_list:
        grade, msg = grade_from_marks(m)
        gp = grade_point_from_grade(grade)
        per_subject.append({
            "marks": m,
            "grade": grade,
            "grade_point": gp,
            "message": msg
        })
        total_points += gp
        total_marks += m

    gpa = total_points / len(marks_list)
    avg_marks = total_marks / len(marks_list)
    return gpa, avg_marks, per_subject

def overall_grade_from_average(avg_marks):
    return grade_from_marks(avg_marks)[0]  # returns letter only

def pretty_print_results(gpa, avg_marks, per_subject):
    print("\n--- Results ---")
    print(f"Subjects: {len(per_subject)}")
    print(f"Average marks: {avg_marks:.2f}")
    overall_grade = overall_grade_from_average(avg_marks)
    print(f"Overall Grade (from average): {overall_grade}")
    print(f"GPA: {gpa:.2f}\n")

    print("Per-subject breakdown:")
    for i, s in enumerate(per_subject, start=1):
        print(f" {i}. Marks: {s['marks']:.2f}  | Grade: {s['grade']:>2}  | "
              f"GP: {s['grade_point']:.2f}  — {s['message']}")

def main():
    print("Simple Student Grade + GPA Calculator")
    print("Enter marks for each subject (0-100). Type 'done' when finished.\n")

    marks = []
    subject_counter = 1
    while True:
        val = input(f"Subject {subject_counter} marks (or 'done'): ").strip()
        if val.lower() == 'done':
            break
        try:
            m = float(val)
        except ValueError:
            print("Please enter a number between 0 and 100, or 'done'.")
            continue
        if not (0 <= m <= 100):
            print("Marks must be between 0 and 100. Try again.")
            continue
        marks.append(m)
        subject_counter += 1

    if not marks:
        print("No marks entered. Exiting.")
        return

    gpa, avg_marks, per_subject = calculate_gpa(marks)
    pretty_print_results(gpa, avg_marks, per_subject)

if __name__ == "__main__":
    main()
