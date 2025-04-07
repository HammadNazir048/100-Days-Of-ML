from student_utils.arithmetic import calculate_percentage, classify_grade
from student_utils.attendance import calculate_attendance_percentage, is_attendance_sufficient
from student_utils.performance import evaluate_performance, get_performance_summary

def demonstrate_arithmetic():
    part = 80
    whole = 120
    percentage = calculate_percentage(part, whole)
    print("Percentage of {} out of {}: {:.2f}%".format(part, whole, percentage))
    grade = classify_grade(percentage)
    print("Grade for {:.2f}%: {}".format(percentage, grade))

def demonstrate_attendance():
    attended_days = 85
    total_days = 100
    attendance_percentage = calculate_attendance_percentage(attended_days, total_days)
    print("Attendance Percentage for {} attended days out of {}: {:.2f}%".format(attended_days, total_days, attendance_percentage))
    is_sufficient = is_attendance_sufficient(attendance_percentage)
    print("Is attendance sufficient? {}".format(is_sufficient))

def demonstrate_performance():
    gpa = 3.6
    attendance_percentage = 92
    performance_level = evaluate_performance(gpa, attendance_percentage)
    print("Performance Level for GPA {} and Attendance {:.2f}%: {}".format(gpa, attendance_percentage, performance_level))
    performance_summary = get_performance_summary(performance_level)
    print("Performance Summary: {}".format(performance_summary))

def main():
    print("Demonstrating student_utils Package")
    demonstrate_arithmetic()
    demonstrate_attendance()
    demonstrate_performance()

if __name__ == "__main__":
    main()
