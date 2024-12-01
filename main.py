from src.server.instance import server
from src.controllers.books import books_ns

if __name__ == "__main__":
    server.api.add_namespace(books_ns, path='/books')
    server.run()