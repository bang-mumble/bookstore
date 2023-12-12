# order.py

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_info(self):
        print(f"Order ID: {self.order_id}")
        self.customer.display_info()

        print("Books in the order:")
        for book in self.books:
            book.display_info()
