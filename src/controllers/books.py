from flask_restx import Resource, Namespace, fields

# Criando o namespace
books_ns = Namespace('Books', description='Operations related to books')

# Modelo para validação
book_model = books_ns.model('Book', {
    'id': fields.Integer(required=True, description='Book ID'),
    'title': fields.String(required=True, description='Book title')
})

# Simulando um banco de dados
books_db = [
    {'id': 0, 'title': 'War and Peace'},
    {'id': 1, 'title': 'Clean Code'}
]

@books_ns.route('/')
class BookList(Resource):
    def get(self):
        """Retorna a lista de todos os livros."""
        return books_db, 200

    @books_ns.expect(book_model)
    def post(self):
        """Adiciona um novo livro."""
        new_book = books_ns.payload
        books_db.append(new_book)
        return {'message': 'Book added successfully!', 'book': new_book}, 201

@books_ns.route('/<int:id>')
class Book(Resource):
    def get(self, id):
        """Retorna um livro pelo ID."""
        book = next((book for book in books_db if book['id'] == id), None)
        if book:
            return book, 200
        return {'message': 'Book not found'}, 404

    @books_ns.expect(book_model)
    def put(self, id):
        """Atualiza um livro pelo ID."""
        book = next((book for book in books_db if book['id'] == id), None)
        if book:
            data = books_ns.payload
            book.update(data)
            return {'message': 'Book updated successfully!', 'book': book}, 200
        return {'message': 'Book not found'}, 404

    def delete(self, id):
        """Deleta um livro pelo ID."""
        global books_db
        books_db = [book for book in books_db if book['id'] != id]
        return {'message': 'Book deleted successfully!'}, 200
