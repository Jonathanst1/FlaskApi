from flask_restx import Resource, fields
from src.server.instance import server

api = server.api

book_model = api.model('Book', {
    'id': fields.Integer(required=True, description='Book ID'),  # Corrigido o typo aqui
    'title': fields.String(required=True, description='Book title')
})

books_db = [
    {'id': 0, 'title': 'War and Peace'},
    {'id': 1, 'title': 'Clean Code'}
]

@api.route('/books')
class BookList(Resource):
    def get(self):
        """Retorna a lista de livros."""
        return books_db

    @api.expect(book_model)
    def post(self):
        """Adiciona um novo livro à lista."""
        new_book = api.payload
        books_db.append(new_book)
        return {'message': 'Book added successfully!', 'book': new_book}, 201
