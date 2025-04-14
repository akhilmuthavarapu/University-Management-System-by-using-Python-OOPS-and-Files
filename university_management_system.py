"""
UNIVERSITY MANAGEMENT SYSTEM :-
Colleges
|
|--> Add Student
     |--> College Name -x->does not exist
                   |--> Roll no
                   |--> Name
                   |--> Branch
|--> Add Teacher
     |--> College Name -x->does not exist
                   |--> Roll no
                   |--> Name
                   |--> Subject    
|--> Display Students
     |--> College Name -x->does not exist
                   |--> Display students exist 
|--> Display Teachers
     |--> College Name -x->does not exist
                   |--> Display Teachers exist in college

"""
#code structure:
"""
class --> college
            |-->constructor
                |--> name[obj]
                |--> students[]
                |--> Teachers
            |--> Add_Student
                 |-->self.students.append(details)
            |--> Add_Teachers
                 |--> self.Teachers.append(details)
            |--> Display students
                 |-->for loop to extract data of students
            |--> Display Teachers
                 |-->for loop to extract data of Teachers
"""

"""
object criteria:-
store colleges in a list for future use
"""
# Additional operations need to be included [TASK] given by Sai Vardhan Sir
"""
Search a  Student based on the student rollno ---> o/p college name
Search a teacher based on the teacher rollno  --->o/p college name
"""

# OWN CHALLENGE FOR MYSELF
"""
---> CHANGE THE CODE STRUCTURE FOR DICTIONARY RATHER THAN LIST

--->ONCE A DATA IS STORED AND IT SHOULD BE STORED IN A .TXT FILE
    THAT ACTS AS A DATABASE FOR THE PROJECT
"""

f=open("database.txt","r")
class Person:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
class Student(Person):
    def __init__(self,rollno,name,branch):
        super().__init__(rollno,name)
        self.branch=branch
class Teacher(Person):
    def __init__(self,rollno,name,subject):
        super().__init__(rollno,name)
        self.subject=subject
class college:
    def __init__(self,college_name):
        self.college_name=college_name
        self.students=[]
        self.teachers=[]
    def add_student(self,student):
        self.students.append(student)
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    def display_students(self):
        for i in self.students:
            print(f"Student Roll no:{i.rollno}")
            print(f"Student name   :{i.name}")
            print(f"Student branch :{i.branch}")
            print()
            print()
        
    def display_teachers(self):
        for i in self.teachers:
            print(f"Teacher Roll no:{i.rollno}")
            print(f"Teacher name   :{i.name}")
            print(f"Teacher subject:{i.subject}")
            print()
            print()
    
def search(ch):
    if ch.lower()=="s":
        rollno=input("Enter student rollno: ")
        B=False
        for i in filedict.keys():
            for j in sorted(filedict[i]["Students"].keys()):
                if j==rollno:
                    print(f"student found in {i}")
                    B=True
                    break
            if B:
                break
        else:
            print("student not found")
        print("searching is completed.....")
    elif ch.lower()=="t":
        rollno=input("Enter Teacher rollno: ")
        B=False
        for i in filedict.keys():
            for j in sorted(filedict[i]["Teachers"].keys()):
                if j==rollno:
                    print(f"Teacher found in {i}")
                    B=True
                    break
            if B:
                break
        else:
            print("student not found")
        print()
        print("⭐"*30)
        print()
        print("searching is completed.....")
        print()
            



university={}
try:
    filedict=eval(f.read())
except:
    filedict={}
f.close()
while True:
    print("⭐"*30)
    print("Welcome to University Management System: ")
    print("1.Create College")
    print("2.Add Student")
    print("3.Add Teacher")
    print("4.Display Students")
    print("5.Display Teachers")
    print("6.Search a Student / Teacher")
    print("7.Exit")
    print()
    try:
        choice=int(input("Enter your choice :"))
    except:
        print("enter correct choice")
        choice=int(input("Enter your choice: "))
    if choice==1:
        cname=input("Enter College Name:")
        if cname in filedict or cname in university:
            print()
            print("Your college is existed in the university list")
            print()
        else:
            print("College is Not Existed so create college")
            clg=input("Enter the College Name to Create:")
            c=college(clg)
            university[clg]=c
            
            filedict[clg]={"Students":{},"Teachers":{}}
            
            print()
            print("College Created Successfully")
            print()
        print("Exiting from the College Cretion Window!!!!!!")
        print("⭐"*30)
    elif choice==2:
        cname=input("Enter College Name:")
        if cname in filedict:
            print("Your College is Existed in the University List")
            print("Welcome to Student Register window to add students:")
            rollno=input("Enter the Student Rollno: ")
            name=input("Enter the student name: ")
            branch=input("Enter the Branch name: ")
            s=Student(rollno,name,branch)
            try:
                university[cname].students.append(s)
                filedict[cname]["Students"][rollno]=[cname,rollno,name,branch]
            except:
                filedict[cname]["Students"][rollno]=[cname,rollno,name,branch]

            print(f"SUCCESSFULLY STORED THE {name} DETAILS!!!!!!")
            print()
            
        else:
            print()
            print("College is not existed so please go for the college creation ")
            print()
        print("Exiting from the Student Profile Creation Window!!!!!!\n")
        print("⭐"*30)
        print()
            
    elif choice==3:
        cname=input("Enter College Name:")
        if cname in filedict:
            print("your colleges is existed in the university list")
            print("Welcome to Teachers Register Window to add Teachers:")
            rollno=input("Enter the Teacher Rollno: ")
            name=input("Enter the Teacher name: ")
            subject=input("Enter the Subject name: ")
            s=Teacher(rollno,name,subject)
            try:
                university[cname].teachers.append(s)
                filedict[cname]["Teachers"][rollno]=[cname,rollno,name,subject]
            except:
                filedict[cname]["Teachers"][rollno]=[cname,rollno,name,subject]
            
            print()
            print("Successfully stored the teacher details!!!!")
            print()
        else:
            print()
            print("College is not existed so please go for the college creation ")
            print()
        print("Exiting from the Teachers Profile Creation Window!!!!!!\n")
        print("⭐"*30)
    elif choice==4:
        cname=input("Enter College Name:")
        if cname in filedict:
            print("Students Existed in the college: ")
            print()
            try:
                university[cname].display_students()
            except:
                for i in list(filedict[cname]["Students"].items()):
                    print("Roll No :",i[1][1])
                    print("Name    :",i[1][2])
                    print("Branch  :",i[1][3])
                    
                
        else:
            print()
            print("College is not existed so please go for the college creation ")
            print()
        print("Exiting from the Students Displaying Window!!!!!!\n")
        print("⭐"*30)
        print()
    elif choice==5:
        cname=input("Enter College Name:")
        if cname in filedict:
            print("Teachers Existed in the college: ")
            print()
            try:
                university[cname].display_teachers()
            except:
                for i in list(filedict[cname]["Teachers"].items()):
                    print("Roll No :",i[1][1])
                    print("Name    :",i[1][2])
                    print("Subject :",i[1][3])
                                 
                    
        else:
            print()
            print("College is not existed so please go for the college creation ")
            print()
        print("Exiting from the Teachers Displaying Window!!!!!!")
        print("⭐"*30)
        
        
    elif choice ==6:
        print("searching window opened...")
        ch=input("whom do you want search student or teacher [s/t]: ")
        search(ch)
        
    elif choice==7:
        print()
        print("Exiting from the Main window .....")
        print()
        break
    else:
        print()
        print("Please Enter Correct choice")
        print()
        print("⭐"*30)
        print()
f=open("database.txt","w")
f.write(f"{filedict}")

f.close()
            
        
        
        
        
