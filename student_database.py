#Add students and courses and find student with most courses and highest average grade. Do not accept courses with grade 0.
def add_student(students: dict, name: str):
    students[name] = {"completed_courses": []}

def print_student(students: dict, name: str):
        if name in students:
            print(name + ":")
            if students[name]["completed_courses"]:
                length = len(students[name]["completed_courses"])
                print(f" {length} completed courses:")
                add_grade = 0
                for course_info in students[name]["completed_courses"]:
                    course_name, grade = course_info
                    print(f"  {course_name} {grade}")
                    add_grade = add_grade + grade
                average_grade = add_grade / len(students[name]["completed_courses"])
                print(f" average grade {average_grade:.1f}")
        
            else: 
                print(" no completed courses")
        else:
            print(f"{name}: no such person in the database")

def add_course(students: dict, name: str, course: tuple):
    if name in students:
        new_course_name, new_grade = course
        if new_grade !=0:
            for i, (existing_name, existing_grade) in enumerate(students[name]["completed_courses"]):
                if existing_name == new_course_name:
                    if new_grade > existing_grade:
                        students[name]["completed_courses"][i] = course
                    return
            students[name]["completed_courses"].append(course)

def summary(students:dict):
    number = len(students)
    print(f"students {number}")
    max_courses = 0
    top_student = ""

    for name, info in students.items():
        num_courses = len(info["completed_courses"])
        if num_courses > max_courses:
            max_courses = num_courses
            top_student = name
    
    print(f"most courses completed {max_courses} {top_student}")

    best_avg = 0
    best_student =""
    for name, info in students.items():
        courses = info["completed_courses"]
        if not courses:
            continue

        total = 0
        for course in courses:
            grade = course[1]
            total += grade
        
        average = total / len(courses)
        
        if average > best_avg:
            best_avg = average
            best_student = name
    print(f"best average grade {best_avg:.1f} {best_student}")





# Testing
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)   
