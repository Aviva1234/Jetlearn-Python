class student:
    def __init__(self,name,rollno):
        self.name = name #instance method
        self.rollno = rollno
    #instance method
    def introduction(self):
        print(f"My name is {self.name}, and my roll number is {self.rollno}.")

s1 = student("Lily", 123)
s2 = student("James", 456)

s1.introduction()
s2.introduction()