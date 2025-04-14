# University-Management-System-by-using-Python-OOPS-and-Files

# University Management System

This is a Python-based University Management System that allows you to manage colleges, students, and teachers with basic CRUD operations. Data is persistently stored in a `.txt` file (`database.txt`) that acts as a lightweight database.

---

## Features

- Create and manage multiple colleges
- Add students and teachers to specific colleges
- Display all students or teachers of a selected college
- Search for a student or teacher by roll number
- Data is saved and loaded from `database.txt` for persistence

---

## Class Overview

### Person (Base Class)
- `rollno`
- `name`

### Student (Inherits from Person)
- `branch`

### Teacher (Inherits from Person)
- `subject`

### College
- `college_name`
- `students` list
- `teachers` list
- `add_student()`
- `add_teacher()`
- `display_students()`
- `display_teachers()`

---

## Data Structure

Colleges and their data are stored in a dictionary called `filedict`:

```python
filedict = {
    "CollegeName": {
        "Students": {
            "RollNo": [college, rollno, name, branch]
        },
        "Teachers": {
            "RollNo": [college, rollno, name, subject]
        }
    }
}
```

This dictionary is written to and read from `database.txt`.

---

## Functionalities

1. **Create College**  
   Add a new college to the system if it doesn't already exist.

2. **Add Student**  
   Add a student to a college by providing roll number, name, and branch.

3. **Add Teacher**  
   Add a teacher to a college by providing roll number, name, and subject.

4. **Display Students**  
   View all students of a specified college.

5. **Display Teachers**  
   View all teachers of a specified college.

6. **Search Student/Teacher by Roll Number**  
   Search across all colleges and display the college where the student or teacher is found.

7. **Exit**  
   Save all data to `database.txt` and close the program.

---

## How It Works

- When the program starts, it attempts to read data from `database.txt`.
- All changes during execution are made to the in-memory `filedict` dictionary.
- On exiting, the updated `filedict` is saved back to `database.txt`.

---

## Future Improvements

- Replace `.txt` with `.json` or a real database (SQLite/MySQL)
- Build a graphical user interface (GUI) or web interface
- Add login/authentication system
- Export data to Excel or PDF formats

---

## Files

- `main.py`: Main program logic and CLI interface
- `database.txt`: Stores all college, student, and teacher data persistently

---

## Author

Developed by Muthavarapu Venkata Akhil 
Additional suggestions by Sai Vardhan Sir
```

---

