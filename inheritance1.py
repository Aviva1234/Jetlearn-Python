class Writer:
    def write(self):
        print('Writing content')
class Speaker:
    def speak(self):
        print('Speaking publicly')
class Author(Writer, Speaker):
    pass


a = Author()
a.write()
a.speak()

    

