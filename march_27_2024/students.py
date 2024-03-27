class Student:
    def __init__(self, id, first_name, last_name, grade):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def update(self, first_name=None, last_name=None, grade=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if grade:
            self.grade = grade

    def __str__(self):
        return f"Student ID: {self.id}, Name: {self.first_name} {self.last_name}, Grade: {self.grade}"
