# Design a library catalog system with a base class LibraryItem and subclasses for different types of items like Book,
# DVD, and Magazine. Include methods to check out, return, and display information about each item.

class LibraryItem:
    def __init__(self, title, author, item_type):
        self.title = title
        self.author = author
        self.item_type = item_type
        self.is_checked_out = False

    def checkout(self):
        if self.is_checked_out:
            return f"{self.title} is already checked out."
        else:
            self.is_checked_out = True
            return f"You have checked out {self.title}."

    def return_item(self):
        if not self.is_checked_out:
            return f"{self.title} was not checked out."
        else:
            self.is_checked_out = False
            return f"You have returned {self.title}."

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Type: {self.item_type}, Checked Out: {self.is_checked_out}"

class Book(LibraryItem):
    def __init__(self, title, author, genre):
        super().__init__(title, author, "Book")
        self.genre = genre

    def display_info(self):
        return f"{super().display_info()}, Genre: {self.genre}"

class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        super().__init__(title, director, "DVD")
        self.duration = duration

    def display_info(self):
        return f"{super().display_info()}, Duration: {self.duration} minutes"

class Magazine(LibraryItem):
    def __init__(self, title, editor, issue_number):
        super().__init__(title, editor, "Magazine")
        self.issue_number = issue_number

    def display_info(self):
        return f"{super().display_info()}, Issue Number: {self.issue_number}"


if __name__ == '__main__':
    book = Book("1984", "George Orwell", "Dystopian")
    dvd = DVD("Inception", "Christopher Nolan", 148)
    magazine = Magazine("National Geographic", "Susan Goldberg", 1024)

    print(book.display_info())
    print(dvd.display_info())
    print(magazine.display_info())

    print(book.checkout())
    print(book.checkout())
    print(book.return_item())
    print(book.return_item())
