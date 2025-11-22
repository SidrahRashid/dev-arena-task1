def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks! Please enter a value between 0 and 100."

    if marks >= 90:
        grade = "A+"
        msg = "Outstanding! You're performing at the highest level!"
    elif marks >= 80:
        grade = "A"
        msg = "Great job! Keep up this excellent performance!"
    elif marks >= 70:
        grade = "B"
        msg = "Well done! You're doing good—aim a little higher!"
    elif marks >= 60:
        grade = "C"
        msg = "Not bad! You can definitely improve with a little more effort."
    elif marks >= 50:
        grade = "D"
        msg = "You're close! Put in a bit more work and you'll do much better."
    else:
        grade = "F"
        msg = "Don't be discouraged! Every failure is a step towards success. Try again!"

    return f"Grade: {grade}\nMessage: {msg}"

marks = int(input("Enter your marks (0-100): "))
print(calculate_grade(marks))
