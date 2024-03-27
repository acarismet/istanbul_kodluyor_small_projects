class Teacher:
    def __init__(self, id, first_name, last_name, field):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.field = field

    def update(self, first_name=None, last_name=None, field=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if field:
            self.field = field

    def __str__(self): # For list display
        return f"Teacher ID: {self.id}, Name: {self.first_name} {self.last_name}, Field: {self.field}"
