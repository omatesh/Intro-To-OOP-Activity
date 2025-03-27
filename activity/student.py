class Student:
    def __init__(self, name, grade, enrollment_list):
        self.name = name
        self.grade = grade
        self.enrollment_list = enrollment_list
    
    def add_class(self, class_name):
        self.enrollment_list.append(class_name)

    def get_num_classes(self):
        num_enrollment = len(self.enrollment_list)
        return num_enrollment
    
    def summary(self, name, grade, num_enrollment):
        return(f"{self.name} is a {self.grade} enrolled in {num_enrollment} classes")