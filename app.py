from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for books (just for demonstration)
books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "price": 9.99},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 7.99},
    {"id": 3, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 8.99},
]

# Home route to display list of books
@app.route('/')
def home():
    return render_template('index.html', books=books)

# Route to display a specific book's details
@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return f"Book with id {book_id} not found!", 404
    return render_template('book_detail.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)
