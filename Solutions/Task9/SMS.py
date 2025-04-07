class Student:
    
    def __init__(self, name, age, student_id, courses=None):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non empty string.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        if not isinstance(student_id, str) or not student_id:
            raise ValueError("Student ID must be a non empty string.")
        if courses is not None and not isinstance(courses, list):
            raise TypeError("Courses must be a list.")

        self._name = name
        self._age = age
        self._student_id = student_id
        self._courses = courses if courses is not None else []

    # Getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_student_id(self):
        return self._student_id

    def get_courses(self):
        return list(self._courses)

    # Setter methods
    def set_name(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non empty string.")
        self._name = name

    def set_age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        self._age = age

    def set_student_id(self, student_id):
        if not isinstance(student_id, str) or not student_id:
            raise ValueError("Student ID must be a non empty string.")
        self._student_id = student_id

    def set_courses(self, courses):
        if not isinstance(courses, list):
            raise TypeError("Courses must be a list.")
        self._courses = courses

    def enroll_in_course(self, course_name):
        if not isinstance(course_name, str) or not course_name:
            raise ValueError("Course name must be a non empty string.")
        if course_name not in self._courses:
            self._courses.append(course_name)

    def drop_course(self, course_name):
        if course_name in self._courses:
            self._courses.remove(course_name)

    def calculate_gpa(self, grades):
        if not isinstance(grades, dict):
            raise TypeError("Grades must be a dictionary.")
        if not grades:
            return 0.0

        total_grade_points = sum(grades.values())
        gpa = total_grade_points / len(grades)
        return round(gpa, 2)

    def __str__(self):
        return (f"Student Name: {self._name}\n"
                f"Age: {self._age}\n"
                f"Student ID: {self._student_id}\n"
                f"Enrolled Courses: {', '.join(self._courses) if self._courses else 'None'}")


class GraduateStudent(Student):
    
    def __init__(self, name, age, student_id, thesis_title, courses=None):
        if not isinstance(thesis_title, str) or not thesis_title:
            raise ValueError("Thesis title must be a non empty string.")
        super().__init__(name, age, student_id, courses)
        self._thesis_title = thesis_title

    def get_thesis_title(self):
        return self._thesis_title

    def set_thesis_title(self, thesis_title):
        if not isinstance(thesis_title, str) or not thesis_title:
            raise ValueError("Thesis title must be a non empty string.")
        self._thesis_title = thesis_title

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}\nThesis Title: {self._thesis_title}"


if __name__ == "__main__":
    student1 = Student("Hammad Nazir", 21, "48")
    print("--- Student Instance ---")
    print(student1)

    print(f"\nName: {student1.get_name()}")
    print(f"Age: {student1.get_age()}")
    print(f"Student ID: {student1.get_student_id()}")
    print(f"Courses: {student1.get_courses()}")

    student1.set_name("Hammad Nazir")
    student1.set_age(22)
    student1.set_courses(["Data Structures", "Operating Systems"])
    print(student1)

    student1.enroll_in_course("Computer Networks")
    student1.drop_course("Operating Systems")
    print(student1)
   
    grades1 = {'Data Structures': 3.6, 'Computer Networks': 3.7, 'Discrete Math': 3.5}
    gpa1 = student1.calculate_gpa(grades1)
    print(f"\nGPA for {student1.get_name()}: {gpa1}")

    grad_student1 = GraduateStudent("Zain Tariq", 24, "G2001", "Deep Learning", courses=["AI", "Computer Vision"])
    print(grad_student1)

    print(f"\nThesis Title: {grad_student1.get_thesis_title()}")
    grad_student1.set_thesis_title("AI for Healthcare Imaging")
    print(f"Updated Thesis Title: {grad_student1.get_thesis_title()}")
    print(grad_student1)

    try:
        invalid_student = Student("Haseeb", -3, "003")
    except ValueError as e:
        print(f"\nError creating student: {e}")

    try:
        invalid_grad_student = GraduateStudent("Ayesha", 26, "20", "")
    except ValueError as e:
        print(f"Error creating graduate student: {e}")
