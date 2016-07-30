from flask import Flask
from .settings import DATABASE_NAME

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db/{}'.format(DATABASE_NAME)


@app.route('/')
def index():
    return 'Hello World 2'
