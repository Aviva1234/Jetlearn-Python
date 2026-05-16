public class Library{
    private String name;
    private ArrayList<Book> books;

    public Library(String name){
        this.name = name;
    }
    public ArrayList<Book> getBooks(){
        return books;
    }

}

public class Book{
    private String title;
    private Student currentStudent;
    private boolean isOut;

    public Book(String title){
        this.title = title;
    }
    public void setCurrentStudent(Student stu){
        currentStudent = stu;
    }
    public boolean getStatus(){
        return isOut;
    }
    public void setStatus(boolean x){
        isOut = x;
    }
}

public class Student{
    private String name;
    private int grade;

    public Student(String name, int grade){
        this.name = name;
        this.grade = grade;
    }
}

public class LibrarySystem{
    private String district;
    private Library lib;
    
    public LibrarySystem(String district, Library lib){
        this.district = district;
        this.lib = lib;
    }

    public void addBooks(Book bk){
        lib.getBooks().add(bk);
        isOut = false;
    }
    public void issueBook(Book bk, int i, Student stu){
        if(lib.getBooks().get(i).getStatus() == false){
            lib.getBooks().get(i).setStatus(true);
            lib.getBooks().get(i).setCurrentStudent(stu);
        }
        
    }
    public void returnBooks(Book bk, int i){
        lib.getBooks().get(i).setStatus(false);
        lib.getBooks().get(i).setCurrentStudent(null);
    }
}