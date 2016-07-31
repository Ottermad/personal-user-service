from flask import Blueprint

blog = Blueprint('blog', __name__)

@blog.route('/')
def index():
    return 'Hello World 2'
