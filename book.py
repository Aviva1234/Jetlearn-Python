class Book:
    def __init__(self, title, author, pages=100):
        self.title = title
        self.author = author
        self.pages = pages

    def show_details(self):
        print("Title: "+self.title+", Author: "+self.author+", Pages: "+str(self.pages))
    
b1 = Book("Treasure Island", "Robert L. Stevenson")
b1.show_details()
b2 = Book("Harry Potter", "J.K. Rowling", 585)
b2.show_details()
    