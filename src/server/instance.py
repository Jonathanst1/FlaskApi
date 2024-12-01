from flask_restx import Api
from flask import Flask

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='Sample BOOK API',
            description='A simple book API',
            doc='/docs'
        )

    def run(self):
        self.app.run(debug=True)

server = Server()
