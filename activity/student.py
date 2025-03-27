class Student:
    def __init__(self, name, grade, enrollment_list):
        self.name = name
        self.grade = grade
        self.enrollment_list = enrollment_list
    
    def add_class(self, class_name):
        self.enrollment_list.append(class_name)
        return self.enrollment_list

    def get_num_classes(self):
        num_enrollment = len(self.enrollment_list)
        return num_enrollment
    
    def summary(self):
        num_enrollment = self.get_num_classes()
        return(f"{self.name} is a {self.grade} enrolled in {num_enrollment} classes")