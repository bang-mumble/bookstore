# bookstore_system.py

from book import Book
from customer import Customer
from order import Order

# Create books
book1 = Book(1, "The Great Gatsby", "F. Scott Fitzgerald", 9.99)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 12.99)

# Create customers
customer1 = Customer(101, "Alice", "alice@example.com")
customer2 = Customer(102, "Bob", "bob@example.com")

# Create orders
order1 = Order(1001, customer1)
order1.add_book(book1)
order1.add_book(book2)

order2 = Order(1002, customer2)
order2.add_book(book2)

# Display information
print("Order Information:")
order1.display_info()
print()
order2.display_info()
