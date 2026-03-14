# Simple Library Management System (Buggy Version)

books = []

def add_book(title, author, pages):
    book = {"title": title, "author": author, "pages": pages, "issued": False}
    books.append(book)
    print("Book added successfully")


def show_books():
    if len(books) == 0:
        print("No books available")
    for b in books:
        print("Title:", b["title"], "| Author:", b["author"], "| Pages:", b["pages"], "| Issued:", b["issued"])


def calculate_average_pages():
    total = 0
    for i in range(len(books)+1):      # BUG 1: Index error (range too large)
        total += books[i]["pages"]
    avg = total / len(books)           # BUG 2: Division by zero if list empty
    return avg


def find_longest_book():
    longest = books[0]                 # BUG 3: Crash if no books exist
    for b in books:
        if b["pages"] < longest["pages"]:   # BUG 4: Logical error (should be >)
            longest = b
    return longest


def search_book(title):
    for b in books:
        if b["title"] = title:         # BUG 5: Syntax error (= instead of ==)
            return b
    return None


def issue_book(index):
    books[index]["issued"] = True      # BUG 6: Index error possible
    print("Book issued")


def return_book(index):
    if books[index]["issued"] == False:
        print("Book was not issued")
    else:
        books[index]["issued"] = False
        print("Book returned")


def remove_book(index):
    books.pop(index)                   # BUG 7: Index error if invalid index
    print("Book removed")


def show_statistics():
    avg = calculate_average_pages()
    longest = find_longest_book()

    print("Average pages:", avg)
    print("Longest book:", longest["title"])


def main():
    while True:
        print("\n---- Library Menu ----")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Average Pages")
        print("4. Longest Book")
        print("5. Search Book")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. Remove Book")
        print("9. Statistics")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            pages = int(input("Enter pages: "))
            add_book(title, author, pages)

        elif choice == "2":
            show_books()

        elif choice == "3":
            print("Average pages:", calculate_average_pages())

        elif choice == "4":
            book = find_longest_book()
            print("Longest book:", book["title"])

        elif choice == "5":
            title = input("Enter title to search: ")
            b = search_book(title)
            print(b["title"])          # BUG 8: Crash if book not found

        elif choice == "6":
            index = int(input("Enter index to issue: "))
            issue_book(index)

        elif choice == "7":
            index = int(input("Enter index to return: "))
            return_book(index)

        elif choice == "8":
            index = int(input("Enter index to remove: "))
            remove_book(index)

        elif choice == "9":
            show_statistics()

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


main()