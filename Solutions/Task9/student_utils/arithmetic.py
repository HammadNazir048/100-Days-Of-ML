def calculate_percentage(obtained_marks, total_marks):
    if not isinstance(obtained_marks, (int, float)) or not isinstance(total_marks, (int, float)):
        raise TypeError("Both obtained_marks and total_marks must be numeric.")
    if total_marks <= 0:
        return 0.0 
    if obtained_marks < 0:
        raise ValueError("Obtained marks cannot be negative.")
    if total_marks < 0:
        raise ValueError("Total marks cannot be negative.")
    if obtained_marks > total_marks:
        raise ValueError("Obtained marks cannot be greater than total marks.")


    percentage = (obtained_marks / total_marks) * 100
    return round(percentage, 2)


def classify_grade(percentage):
    """
    Classifies a grade based on the given percentage.

    Grade classification scale:
        >= 90%:  A+
        >= 80% and < 90%: A
        >= 70% and < 80%: B
        >= 60% and < 70%: C
        >= 50% and < 60%: D
        < 50%:   Fail

    Args:
        percentage (float): Percentage to classify.

    Returns:
        str: Grade classification (e.g., 'A+', 'B', 'Fail').
        Raises:
            TypeError: if percentage is not numeric.
            ValueError: if percentage is outside the range [0, 100].
    """
    if not isinstance(percentage, (int, float)):
        raise TypeError("Percentage must be numeric.")
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100.")


    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'Fail'

if __name__ == "__main__":
    print("--- Percentage Calculation ---")
    marks_obtained = 75
    total_marks_exam = 100
    try:
        percentage_result = calculate_percentage(marks_obtained, total_marks_exam)
        print(f"Percentage for {marks_obtained}/{total_marks_exam}: {percentage_result}%") # Output: 75.0%
    except Exception as e:
        print(f"Error calculating percentage: {e}")

    try:
        percentage_zero_total = calculate_percentage(60, 0)
        print(f"Percentage with zero total marks: {percentage_zero_total}%") # Output: 0.0%
    except Exception as e:
        print(f"Error calculating percentage: {e}")

    try:
        calculate_percentage("abc", 100)
    except TypeError as e:
        print(f"TypeError example: {e}") 

    print("\n--- Grade Classification ---")
    percentage_grade_A_plus = 92
    grade_A_plus = classify_grade(percentage_grade_A_plus)
    print(f"Grade for {percentage_grade_A_plus}%: {grade_A_plus}") 

    percentage_grade_C = 65
    grade_C = classify_grade(percentage_grade_C)
    print(f"Grade for {percentage_grade_C}%: {grade_C}") 


    percentage_fail = 45
    grade_fail = classify_grade(percentage_fail)
    print(f"Grade for {percentage_fail}%: {grade_fail}") 

    try:
        classify_grade(110)
    except ValueError as e:
        print(f"ValueError example: {e}") 
    try:
        classify_grade("invalid")
    except TypeError as e:
        print(f"TypeError example: {e}") 