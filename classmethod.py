class student:
    school_name = 'Greenwood High'

    def __init__(self,name):
        self.name = name
    
    @classmethod
    def change_school(cls,new_school):
        cls.school_name = new_school
    
    def show(self):
        print(f"Name: {self.name}, School: {student.school_name}")

s1 = student('Lily')
s2 = student('James')
student.change_school("NYU")
s1.show()
s2.show()