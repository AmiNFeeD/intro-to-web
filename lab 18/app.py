from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    books = [
        {"id":1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"id":2, "title": "1984", "author": "George Orwell"},
        {"id":3, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
    ]
    return render_template('index.html', books=books, title = "Book List")

if __name__ == '__main__':
    app.run(debug=True)