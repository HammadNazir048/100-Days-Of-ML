def read_student_records(filepath):
   
    student_records = []
    total_students = 0 # Initialize student counter

    try:
        with open(filepath, 'r') as file:
            for line_number, line in enumerate(file, 1): #enumerate to track line numbers for error reporting
                line = line.strip() # Remove leading/trailing whitespace
                if not line: # Skip empty lines
                    continue

                parts = line.split(',')
                if len(parts) < 3: # Minimum: name, age, student_id
                    print(f"Warning: Skipping line {line_number} due to insufficient data: {line}")
                    continue # Skip to next line

                try:
                    name = parts[0]
                    age = int(parts[1]) # Try converting age to integer
                    student_id = parts[2]
                    courses = [course.strip() for course in parts[3:]] # List of courses, stripping whitespace

                    record = {
                        'name': name,
                        'age': age,
                        'student_id': student_id,
                        'courses': courses
                    }
                    student_records.append(record)
                    total_students += 1 # Increment student counter

                except ValueError as ve:
                    print(f"Error on line {line_number}: Invalid data format - {ve}. Line skipped: {line}")
                except Exception as e:
                    print(f"Unexpected error on line {line_number}: {e}. Line skipped: {line}")

    except FileNotFoundError:
        print(f"Error: File not found at path: {filepath}")
        return [], 0 
    except Exception as e:
        print(f"Error reading file: {e}")
        return [], 0 

    print(f"Successfully read {total_students} student records from {filepath}.") 
    return student_records, total_students 

def write_student_records(filepath, records):
    try:
        with open(filepath, 'w') as file:
            for record in records:
                if not isinstance(record, dict):
                    print("Warning: Skipping invalid record (not a dictionary).")
                    continue # Skip if record is not a dictionary

                name = record.get('name', 'N/A')
                age = record.get('age', 'N/A')
                student_id = record.get('student_id', 'N/A')
                courses = record.get('courses', [])

                # Ensure name, age, student_id are converted to string
                name_str = str(name).strip()
                age_str = str(age).strip()
                student_id_str = str(student_id).strip()
                course_str = ','.join(map(str.strip, courses)) # Convert courses to comma-separated string

                line = f"{name_str},{age_str},{student_id_str},{course_str}\n"
                file.write(line)
        return True # Indicate successful write

    except Exception as e:
        print(f"Error writing to file: {e}")
        return False # Indicate write failure


if __name__ == "__main__":
    example_records = [
        {'name': 'Hammad', 'age': 20, 'student_id': '48', 'courses': ['Math', 'Physics']},
        {'name': 'Haseeb', 'age': 22, 'student_id': '42', 'courses': ['Computer Science', 'Data Analysis', 'Statistics']},
        {'name': 'Zain', 'age': 21, 'student_id': '02', 'courses': []},
    ]

    input_file = 'students.txt' 
    output_file = 'student_output.txt' 

    write_successful = write_student_records(output_file, example_records)
    if write_successful:
        print(f"Successfully wrote student records to '{output_file}'.")
    else:
        print(f"Failed to write student records to '{output_file}'.")


    sample_student_data = """Hammad,20,48,Math,Physics
Haseeb,22,42,Computer Science,Data Analysis,Statistics
Zain,21,30
Invalid Data,Twenty,S1004,History # Will cause a ValueError
"""
    with open(input_file, 'w') as f:
        f.write(sample_student_data)
    print(f"\nCreated sample input file '{input_file}' for reading demonstration.\n")


    read_records, student_count = read_student_records(input_file)
    if read_records:
        print(f"\n--- Student Records Read from '{input_file}' ({student_count} students) ---")
        for record in read_records:
            print(record)
    else:
        print(f"No student records read from '{input_file}'.")

    non_existent_file = 'non_existent_students.txt'
    read_records_non_existent, count_non_existent = read_student_records(non_existent_file)
    if not read_records_non_existent:
        print(f"\nAttempted to read from non-existent file '{non_existent_file}'. Expectedly, no records were read.")
        print(f"Student count from non-existent file: {count_non_existent}") # Should be 0


    example_records_updated = [
        {'name': 'Hammad', 'age': 21, 'student_id': 'S1001', 'courses': ['Advanced Math', 'Physics II']},
        {'name': 'Haseeb', 'age': 22, 'student_id': 'S1002', 'courses': ['Computer Science', 'Data Analysis', 'Machine Learning']},
        {'name': 'Zain', 'age': 21, 'student_id': 'S1003', 'courses': []},
    ]
    write_successful_updated = write_student_records(output_file, example_records_updated)
    if write_successful_updated:
        print(f"\nSuccessfully updated student records in '{output_file}'.")
    else:
        print(f"Failed to update student records in '{output_file}'.")
