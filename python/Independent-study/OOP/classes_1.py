books = []

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def read_book(self):
        if self.is_read == False:
            self.is_read = True
            print(f"You've now read {self.title}")
        else:
            print(f"You've already {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}"

new_title = input(f"What is the title of the book? ")
new_author = input(f"What is the name of the author? ").title()

books.append(print(Book(title=new_title, author=new_author)))

print(books)