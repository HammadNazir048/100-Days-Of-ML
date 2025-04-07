# student_utils/attendance.py - Attendance functions for student utilities

def calculate_attendance_percentage(present_days, total_days):
    """
    Calculates the attendance percentage.

    Args:
        present_days (int): Number of days the student was present.
        total_days (int): Total number of working days.

    Returns:
        float: Attendance percentage, rounded to two decimal places.
               Returns 0.0 if total_days is zero to avoid division by zero.
        Raises:
            TypeError: if present_days or total_days are not integers.
            ValueError: if total_days is negative or present_days is negative or greater than total_days.
    """
    if not isinstance(present_days, int) or not isinstance(total_days, int):
        raise TypeError("Both present_days and total_days must be integers.")
    if total_days <= 0:
        return 0.0  # Avoid division by zero
    if present_days < 0:
        raise ValueError("Present days cannot be negative.")
    if total_days < 0:
        raise ValueError("Total days cannot be negative.")
    if present_days > total_days:
        raise ValueError("Present days cannot be greater than total days.")


    percentage = (present_days / total_days) * 100
    return round(percentage, 2)


def is_attendance_sufficient(attendance_percentage, required_percentage=75.0):
    """
    Checks if the attendance percentage is sufficient based on a required percentage.

    Args:
        attendance_percentage (float): Student's attendance percentage.
        required_percentage (float, optional): Minimum required attendance percentage. Defaults to 75.0%.

    Returns:
        bool: True if attendance is sufficient, False otherwise.
        Raises:
            TypeError: if attendance_percentage or required_percentage are not numeric.
            ValueError: if attendance_percentage or required_percentage are outside the range [0, 100].
    """
    if not isinstance(attendance_percentage, (int, float)) or not isinstance(required_percentage, (int, float)):
        raise TypeError("Both attendance_percentage and required_percentage must be numeric.")
    if not 0 <= attendance_percentage <= 100:
        raise ValueError("Attendance percentage must be between 0 and 100.")
    if not 0 <= required_percentage <= 100:
        raise ValueError("Required percentage must be between 0 and 100.")


    return attendance_percentage >= required_percentage



# Example Usage and Demonstrations:
if __name__ == "__main__":
    # 1. Attendance Percentage Calculation Examples
    print("--- Attendance Percentage Calculation ---")
    days_present = 45
    total_days_class = 60
    try:
        attendance_percent = calculate_attendance_percentage(days_present, total_days_class)
        print(f"Attendance for {days_present}/{total_days_class} days: {attendance_percent}%") # Output: 75.0%
    except Exception as e:
        print(f"Error calculating attendance percentage: {e}")


    try:
        attendance_zero_days = calculate_attendance_percentage(0, 50)
        print(f"Attendance for 0 present days: {attendance_zero_days}%") # Output: 0.0%
    except Exception as e:
        print(f"Error calculating attendance percentage: {e}")


    # Example of invalid input (non-integer)
    try:
        calculate_attendance_percentage(45.5, 60) # Non-integer present_days
    except TypeError as e:
        print(f"TypeError example: {e}") # Output: TypeError: Both present_days and total_days must be integers.


    # 2. Attendance Sufficiency Check Examples
    print("\n--- Attendance Sufficiency Check ---")
    sufficient_attendance_percent = 80.0
    is_sufficient = is_attendance_sufficient(sufficient_attendance_percent) # Default required percentage (75%)
    print(f"Is {sufficient_attendance_percent}% attendance sufficient? {is_sufficient}") # Output: True


    marginal_attendance_percent = 70.0
    is_sufficient_marginal = is_attendance_sufficient(marginal_attendance_percent)
    print(f"Is {marginal_attendance_percent}% attendance sufficient? {is_sufficient_marginal}") # Output: False


    custom_required_percent = 85.0
    attendance_percent_custom = 90.0
    is_sufficient_custom = is_attendance_sufficient(attendance_percent_custom, custom_required_percent)
    print(f"Is {attendance_percent_custom}% sufficient with required {custom_required_percent}%? {is_sufficient_custom}") # Output: True


    # Example of invalid percentage (out of range)
    try:
        is_attendance_sufficient(120)
    except ValueError as e:
        print(f"ValueError example: {e}") # Output: ValueError: Attendance percentage must be between 0 and 100.

    # Example of invalid percentage (non-numeric)
    try:
        is_attendance_sufficient("invalid")
    except TypeError as e:
        print(f"TypeError example: {e}") # Output: TypeError: Both attendance_percentage and required_percentage must be numeric.
