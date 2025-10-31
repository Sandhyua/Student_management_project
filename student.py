class Student:
    all_students=[]
    def __init__(self,name,roll_no,marks,age,city,gender,contact):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        self.age=age
        self.city=city
        self.gender=gender
        self.contact=contact

    @classmethod
    def add_student(cls): 
        name=input("Enter Student Name:")
        roll_number=input("Enter Student Roll Number:")
        marks=int(input("Enter Student Marks:"))
        age=int(input("Enter Student Age:"))
        city=input("Enter Student City:")
        gender=input("Enter Student Gender:")
        contact=int(input("Enter Student Contact Number:"))
        Students=cls(name,roll_number,marks,age,city,gender,contact)
        cls.all_students.append(Students)
        print(f"Student{name} Addes Successfully!")

    @classmethod
    def View_all_students(cls):
        if not cls.all_students:
            print("No Students Found!")
            return 
        for student in cls.all_students:
            print(f"Name:{student.name},Roll Number:{student.roll_no},marks:{student.marks},Age:{student.age},city:{student.city},Gender:{student.gender},Contact:{student.contact}")

    @classmethod
    def serch_student(cls):
        roll_no=input("Enter Roll Number to Search Student:")
        for student in cls.all_students:
            if student.roll_no==roll_no:
                 print(f"Name:{student.name},Roll Number:{student.roll_no},marks:{student.marks},Age:{student.age},city:{student.city},Gender:{student.gender},Contact:{student.contact}")
            return
        print("Student Not Found!")
    @classmethod
    def Update_student(cls):
        roll_no=input("Enter Roll Number to Update Student:")
        for student in cls.all_students:
            if student.roll_no==roll_no:
                name=input("Enter New Student Name:")
                marks=int(input("Enter New Student Marks:"))
                age=int(input("Enter New Student Age:"))
                city=input("Enter New Student City:")
                gender=input("Enter New Student Gender:")
                Contact=int(input("Enter New student Contact Number:"))
                student.name=name
                student.marks=marks
                student.age=age
                student.city=city
                student.gender=gender
                student.contact=Contact
                print(f"Student with Roll Number {roll_no} Updated Sucessfully!")
                return
        print("Student Not Found!")
    @classmethod
    def Delete_student(cls):
            roll_no=input("Enter Roll Number to Delete Student:")
            for student in cls.all_students:
               if student.roll_no==roll_no:
                   cls.all_students.remove(student)
                   print(f"Student with Roll Number {roll_no} Deleted Successfully!")
                   return
            print("Student Not Found!")

def Menu() -> None:
     
     while True:
            print("\n =================**Student Management System**=================")    
            print("1. Add Student")
            print("2. View All Students")
            print("3. Serch Student by Roll Number")
            print("4. Update Student by Roll Number")
            print("5. Delete Student by Roll Number")
            print("6. Exit")
            # print("=========================================================\n")
            choice=int(input("Enter Your Choice(1-6): "))
            if choice==1:
                Student.add_student()
            elif choice==2:
                Student.View_all_students()
            elif choice==3:
                Student.serch_student()
            elif choice==4:
                Student.Update_student()
            elif choice==5:
                Student.Delete_student()
            elif choice==6:
                print("Exiting Student Management System. Goodbye!")
                break
            else:
                print("Invalid Choice! Please Enter a Valid Choice(1-6)! Try Again.")

if __name__=="__main__":
    Menu()
   

