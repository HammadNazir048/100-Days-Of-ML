class StudentListIterator:
    def __init__(self, student_list):
        self._students = student_list.get_students()
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._students):
            student = self._students[self._index]
            self._index += 1
            return student
        else:
            raise StopIteration


class StudentList:
    def __init__(self, students=None):
        self._students = students if students is not None else []

    def add_student(self, student):
        if not isinstance(student, object) or not hasattr(student, 'get_name'):
            raise TypeError("Invalid input: Must be a Student object.")
        self._students.append(student)

    def get_students(self):
        return list(self._students)

    def __iter__(self):
        return StudentListIterator(self)


def attendance_generator(student_names, total_days):
    import random

    if not isinstance(student_names, list):
        raise TypeError("Student names must be a list.")
    if not isinstance(total_days, int) or total_days <= 0:
        raise ValueError("Total days must be a positive integer.")

    attendance_statuses = ['Present', 'Absent', 'Late']
    for day in range(1, total_days + 1):
        daily_attendance = {}
        for name in student_names:
            daily_attendance[name] = random.choice(attendance_statuses)
        yield day, daily_attendance


def random_marks_generator(course_names, num_students):
    import random

    if not isinstance(course_names, list):
        raise TypeError("Course names must be a list.")
    if not isinstance(num_students, int) or num_students <= 0:
        raise ValueError("Number of students must be a positive integer.")

    for course in course_names:
        course_marks = {}
        for i in range(1, num_students + 1):
            student_id = f"S{1000 + i}"
            course_marks[student_id] = random.randint(0, 100)
        yield course, course_marks


if __name__ == "__main__":
    class MockStudent:
        def __init__(self, name, student_id):
            self._name = name
            self._student_id = student_id
        def get_name(self):
            return self._name
        def get_student_id(self):
            return self._student_id
        def __str__(self):
            return f"Student(Name={self._name}, ID={self._student_id})"

    student_list = StudentList()
    student_list.add_student(MockStudent("Alice", "S1048"))
    student_list.add_student(MockStudent("Bob", "S1042"))
    student_list.add_student(MockStudent("Charlie", "S1003"))

    print("--- Iterating through StudentList ---")
    for student in student_list:
        print(student)

    student_names_attendance = ["Alice", "Bob", "Charlie"]
    total_days_attendance = 5
    print(f"\n--- Attendance for {total_days_attendance} days ---")
    for day, daily_attendance in attendance_generator(student_names_attendance, total_days_attendance):
        print(f"Day {day}: {daily_attendance}")

    course_list_marks = ["Math", "Science", "English"]
    num_students_marks = 4
    print(f"\n--- Random Marks for {num_students_marks} students in courses {course_list_marks} ---")
    for course, marks in random_marks_generator(course_list_marks, num_students_marks):
        print(f"Course: {course}, Marks: {marks}")

    print("\n--- Explicitly using StudentListIterator ---")
    student_iterator = StudentListIterator(student_list)
    try:
        while True:
            student = next(student_iterator)
            print(student)
    except StopIteration:
        print("End of StudentList")

    try:
        for day, attendance in attendance_generator(["Student1"], -5):
            pass
    except ValueError as e:
        print(f"\nAttendance Generator Error: {e}")

    try:
        for course, marks in random_marks_generator("Not a list", 3):
            pass
    except TypeError as e:
        print(f"Marks Generator Error: {e}")