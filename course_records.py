# Application to keep track of your own course records
class Course:
    def __init__(self):
        self.courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.courses:
            self.courses[name] = {"grade": grade, "credits": credits}
        else:
            if self.courses[name]["grade"] < grade:
                self.courses[name]["grade"] = grade
                self.courses[name]["credits"] = credits
            else:
                None

    
    def get_course_data(self, name):
        if name not in self.courses:
            return "no entry for this course"

        self.name = name
        self.credits = self.courses[name]["credits"]
        self.grade = self.courses[name]["grade"]
        return f"{self.name} ({self.credits} cr) grade {self.grade}"

    def statistics(self):
        total_courses = len(self.courses)
        total_credits = sum(course["credits"] for course in self.courses.values())
        total_grades = sum(course["grade"] for course in self.courses.values())
        print(f"{total_courses} completed courses, a total of {total_credits} credits")

        mean = total_grades / total_courses
        print(f"mean {mean:.1f}")

        print("grade distribution")

    def grade_distribution(self):
        counts = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}

        for course in self.courses.values():
            grade = int(course["grade"])
            if grade in counts:
                counts[grade] += 1

        x5 = counts[5] * "x"
        x4 = counts[4] * "x"
        x3 = counts[3] * "x"
        x2 = counts[2] * "x"
        x1 = counts[1] * "x"

        print(f"5: {x5}")
        print(f"4: {x4}")
        print(f"3: {x3}")
        print(f"2: {x2}")
        print(f"1: {x1}")
    

            
class CourseRecordsApplication:
    def __init__(self):
        self.course = Course()

    def help(self):
        print("commands: ")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        cr = int(input("credits: "))
        self.course.add_course(name, grade, cr)

    def get_course_data(self):
        name = input("course: ")
        print(self.course.get_course_data(name))
    
    def statistics(self):
        self.course.statistics()
        self.course.grade_distribution()


    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()

application = CourseRecordsApplication()
application.execute()


