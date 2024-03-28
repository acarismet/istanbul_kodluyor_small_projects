# Student and Teacher Registration System

This Python project allows you to manage student and teacher registrations. You can add, remove, and update student and teacher information.

## Features

- Add new students and teachers
- Remove existing students and teachers
- Update student and teacher information
- View list of registered students and teachers

## Usage

1. Clone this repository or download the files.
2. Install any required dependencies (there are currently none).
3. Run python main.py to start the program.

**Note:** This program uses the os module to clear the console screen. This functionality might not work on all operating systems.

## How it works

### The program utilizes three main Python files:

- main.py: This is the main script that drives the program. It provides a user interface for interacting with the student and teacher data.
- students.py: This file defines the Student class, which represents a student record with attributes like ID, name, and grade.
- teachers.py: This file defines the Teacher class, which represents a teacher record with attributes like ID, name, and field.

The program maintains separate lists for students and teachers. Users can choose to work with either list and perform CRUD (Create, Read, Update, Delete) operations on the respective data.

## Contributing

Feel free to fork this repository and contribute improvements!
