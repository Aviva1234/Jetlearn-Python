class Member:
    def __init__(self, name):
        self.name = name
    def showName(self):
        print(f'My name is {self.name}')
    
class StudentMember(Member):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id
    def showId(self):
        print(f'ID: {self.id}')

s1 = StudentMember('Aarav','S101')
s1.showName()
s1.showId()
