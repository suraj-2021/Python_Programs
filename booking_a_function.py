#Passing list of books as an function argument and doing things with that
books=['Atomic Habits','Sri Gita Bhashyam','How to win Friends','Thinking Clearly']

def my_books(books):
    for book in books:
        print(f"{book}")
        
my_books(books)
