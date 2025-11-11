def p1():   # Step 1
    students = {
        "Alice": "A",
        "Bob": "B",
        "Charlie": "F-",
        "David": "D",
        "Eve": "A"
    }
    
    for student in students:
        print(f"{student} has a grade of {students.get(student)}")
    
def p2():   # Step 2 and 3
    student = {"name": "Alice", "age": 16, "grade": "A"}
    print(f"{student['name']} is {student['age']}")
    
    student['grade'] = "A+"
    print(student)
    
def p3():   # Step 4
    movies = {
        "The Terminator": 1984,
        "The Matrix": 1999,
        "Roundhay Garden": 1888
    }
    movie_name = input("Enter a movie\n>")
    try:
        movie_date = int(input("Enter release date\n>"))
        movies.update({movie_name: movie_date})
    except:
        print("Invalid release date. Entry not added.")
        
def p4():   # Step 5
    fruits = {
        "Apple": 0.79,
        "Banana": 0.29,
        "Grape": 2.49,
        "Dragonfruit": 4.99,
        "Lemon": 0.99
    }
    
    for fruit in fruits:
        print(f"{fruit} is {fruits.get(fruit)}")
        
    remove = input("\nWhich would you like to remove?\n>")
    try:
        fruits.pop(remove.capitalize())
    except:
        "Fruit not found."
        
    print(fruits)

def p5():   # Step 6
    inventory = {"apples": 10, "bananas": 5, "oranges": 8}
    for item in inventory:
        print(f"There are {inventory.get(item)} {item}")

def p6():   # Step 7
    words = input("Type a sentence\n>").lower().split()
    word_dict = {}
    
    for word in words:
        word_dict.update({word: word_dict.get(word, 0)+1})
    print(word_dict)

def p7():   # Step 8
    books = {
        1:{
            "Title": "Book",
            "Author": "Guy",
            "Year": 1992
        },
        2:{
            "Title": "BuK",
            "Author": "Dude",
            "Year": 1993
        },
        3:{
            "Title": "Book 2: Revenge of the Guy",
            "Author": "Guy",
            "Year": 1994
        }
    }
    
    for book in books:
        book_dict = books.get(book)
        print(f"\nBook {book}\n  Title: {book_dict.get("Title")}\n  Author: {book_dict.get("Author")}\n  Year: {book_dict.get("Year")}")
        
def p8():   # Step 9
    squares = {}
    for i in range(1, 11):
        squares.update({i: i**2})
        
def p9():   # Step 10
    employee_salaries ={
        "Jeremy": 36000,
        "John": 150000,
        "Charlie": 10000,
        "Gregory": 100000
    }
    
    highest_payed = "Charlie"
    for e in employee_salaries:
        if employee_salaries.get(e) > employee_salaries.get(highest_payed):
            highest_payed = e
    print(highest_payed)

p9()