class Student:
    def __init__(self, name, grade, enrollment_list):
        self.name = name
        self.grade = grade
        self.enrollment_list = enrollment_list
    
    def add_class(self, class_name):
        self.enrollment_list.append(class_name)

    def get_num_classes(self):
        return len(self.enrollment_list)
    def summary(self):
        return(f"{})