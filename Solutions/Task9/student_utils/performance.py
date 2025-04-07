# student_utils/performance.py - Performance evaluation functions for student utilities

def evaluate_performance(gpa):
    """
    Evaluates student performance based on GPA.

    Performance scale:
        GPA >= 3.8:  Excellent
        GPA >= 3.5 and < 3.8: Very Good
        GPA >= 3.0 and < 3.5: Good
        GPA >= 2.5 and < 3.0: Average
        GPA < 2.5:  Below Average

    Args:
        gpa (float): Student's GPA.

    Returns:
        str: Performance evaluation (e.g., 'Excellent', 'Good', 'Below Average').
        Raises:
            TypeError: if gpa is not numeric.
            ValueError: if gpa is outside the valid GPA range [0.0, 4.0].
    """
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA must be numeric.")
    if not 0.0 <= gpa <= 4.0:
        raise ValueError("GPA must be between 0.0 and 4.0.")


    if gpa >= 3.8:
        return 'Excellent'
    elif gpa >= 3.5:
        return 'Very Good'
    elif gpa >= 3.0:
        return 'Good'
    elif gpa >= 2.5:
        return 'Average'
    else:
        return 'Below Average'


def check_academic_standing(gpa, min_gpa_for_standing=2.0):
    """
    Checks if a student is in good academic standing based on their GPA.

    Args:
        gpa (float): Student's GPA.
        min_gpa_for_standing (float, optional): Minimum GPA required for good standing. Defaults to 2.0.

    Returns:
        bool: True if in good standing, False otherwise.
        Raises:
            TypeError: if gpa or min_gpa_for_standing are not numeric.
            ValueError: if gpa or min_gpa_for_standing are outside the valid GPA range [0.0, 4.0].
    """
    if not isinstance(gpa, (int, float)) or not isinstance(min_gpa_for_standing, (int, float)):
        raise TypeError("Both GPA and min_gpa_for_standing must be numeric.")
    if not 0.0 <= gpa <= 4.0:
        raise ValueError("GPA must be between 0.0 and 4.0.")
    if not 0.0 <= min_gpa_for_standing <= 4.0:
        raise ValueError("Minimum GPA for standing must be between 0.0 and 4.0.")


    return gpa >= min_gpa_for_standing



# Example Usage and Demonstrations:
if __name__ == "__main__":
    # 1. Performance Evaluation Examples
    print("--- Performance Evaluation ---")
    excellent_gpa = 3.9
    performance_excellent = evaluate_performance(excellent_gpa)
    print(f"Performance for GPA {excellent_gpa}: {performance_excellent}") # Output: Excellent


    good_gpa = 3.2
    performance_good = evaluate_performance(good_gpa)
    print(f"Performance for GPA {good_gpa}: {performance_good}") # Output: Good


    below_average_gpa = 2.0
    performance_below_average = evaluate_performance(below_average_gpa)
    print(f"Performance for GPA {below_average_gpa}: {performance_below_average}") # Output: Below Average


    # Example of invalid GPA (out of range)
    try:
        evaluate_performance(4.5)
    except ValueError as e:
        print(f"ValueError example: {e}") # Output: ValueError: GPA must be between 0.0 and 4.0.

    # Example of invalid GPA (non-numeric)
    try:
        evaluate_performance("invalid")
    except TypeError as e:
        print(f"TypeError example: {e}") # Output: TypeError: GPA must be numeric.


    # 2. Academic Standing Check Examples
    print("\n--- Academic Standing Check ---")
    standing_gpa_good = 3.0
    is_standing_good = check_academic_standing(standing_gpa_good) # Default min_gpa (2.0)
    print(f"Is GPA {standing_gpa_good} in good standing? {is_standing_good}") # Output: True


    standing_gpa_probation = 1.8
    is_standing_probation = check_academic_standing(standing_gpa_probation)
    print(f"Is GPA {standing_gpa_probation} in good standing? {is_standing_probation}") # Output: False


    custom_min_gpa = 2.5
    standing_gpa_custom_min = 2.7
    is_standing_custom_min = check_academic_standing(standing_gpa_custom_min, custom_min_gpa)
    print(f"Is GPA {standing_gpa_custom_min} in good standing with min GPA {custom_min_gpa}? {is_standing_custom_min}") # Output: True


    # Example with GPA at the minimum limit
    standing_gpa_min_limit = 2.0
    is_standing_min_limit = check_academic_standing(standing_gpa_min_limit)
    print(f"Is GPA {standing_gpa_min_limit} (min limit) in good standing? {is_standing_min_limit}") # Output: True


    # Example of invalid GPA (out of range)
    try:
        check_academic_standing(-0.5)
    except ValueError as e:
        print(f"ValueError example: {e}") # Output: ValueError: GPA must be between 0.0 and 4.0.

    # Example of invalid min_gpa_for_standing (out of range)
    try:
        check_academic_standing(3.0, 5.0)
    except ValueError as e:
        print(f"ValueError example for min_gpa: {e}") # Output: ValueError: Minimum GPA for standing must be between 0.0 and 4.0.
