from app import app
from app.setup import create_database, create_tables

if __name__ == '__main__':
    create_database()
    create_tables()
    app.run(host='0.0.0.0')
