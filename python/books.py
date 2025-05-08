books = ['1984', 'The Catcher in the Rye', 'To kill a Mockingbird', 'The Great Gatsby']
print("first:", books[0], "last:", books[-1])

books.append("Moby Dick")
print(books)

books.insert(3, "Pride and Perjudice")
print(books)

books.remove("The Catcher in the Rye")
print(books)

books[0] = "Brave New World"
print(books)

for i in books:
    print(f"I have read {i}")

more_books = ['The Hobbit', 'Farenheit 451']
books = books + more_books
print(books)