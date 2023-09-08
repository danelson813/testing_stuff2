from domain.book import Book
from repository.generic_repository import GenericRepository


def main():
    # Create the repository
    repo = GenericRepository(Book, "book_database.json")

    # Create a book
    book = Book("1", "Clean Code", "Robert C. Martin", 464)

    # Save the book
    repo.save(book)
    print(repo.get("1"))


if __name__ == "__main__":
    main()
