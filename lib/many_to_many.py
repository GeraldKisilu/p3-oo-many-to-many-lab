class Author:
    all_authors = []

    def __init__(self, name: str) -> None:
        self.name = name
        Author.all_authors.append(self)

    def __str__(self) -> str:
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value:
            raise Exception('Name must be a non-empty string.')
        self._name = value

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all_books = []

    def __init__(self, title: str) -> None:
        self.title = title
        Book.all_books.append(self)

    def __str__(self) -> str:
        return self.title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str) or not value:
            raise Exception("Title must be a non-empty string.")
        self._title = value

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    all_contracts = []

    def __init__(self, author: Author, book: Book, date: str, royalties: int) -> None:
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    def __str__(self) -> str:
        return (
            f'Contract:\n'
            f'Author: {self.author}\n'
            f'Book: {self.book}\n'
            f'Date: {self.date}\n'
            f'Royalties: {self.royalties}%'
        )

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value: Author):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of the Author class.")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value: Book):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of the Book class.")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value: str):
        if not isinstance(value, str) or not value:
            raise Exception("Date must be a non-empty string.")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value: int):
        if not isinstance(value, int) or not (0 <= value <= 100):
            raise Exception("Royalties must be an integer between 0 and 100.")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

# Example usage
if __name__ == "__main__":
    # Create an author
    author = Author("John Doe")

    # Create a book
    book = Book("Python Programming 101")

    # Author signs a contract for the book
    contract = author.sign_contract(book, "2024-06-11", 25)

    # Print the contract details
    print(contract)

    # Get all contracts of the author
    print(author.contracts())

    # Get all books of the author
    print(author.books())

    # Get total royalties earned by the author
    print(author.total_royalties())

    # Get contracts by date
    print(Contract.contracts_by_date("2024-06-11"))
