class student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display_details(self):
        print("Name:",self.name)
        print("Roll_No:",self.roll_no)
        print("Marks:",self.marks)
    def grade(self):
        if self.marks >= 90:
            print("Grade A")
        elif self.marks >= 75:
            print("Grade B")
        elif self.marks >= 50:
            print("Grade C")
        else:
            print("Fail")


    def update_mark(self,new_marks):
        self.marks = new_marks
        print("Marks updated successfully")



# creating object
s1= student("aman",39,10)
#update marks
s1.update_mark(50)


#calling method
s1.display_details()
s1.grade()
 
    