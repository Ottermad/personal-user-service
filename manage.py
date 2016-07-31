from flask_script import Manager
from flask_migrate import MigrateCommand
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError

from app import app
from app.settings import DATABASE_NAME

import logging

# Get an instance of a logger
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] - %(message)s')

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def hello():
    print("hello")

@manager.command
def create_database():
    logging.info("Creating database")
    engine = create_engine("postgresql://postgres:postgres@db/postgres")
    conn = engine.connect()
    conn.execute("commit")

    try:
        conn.execute("create database {}".format(DATABASE_NAME))
        logging.info("Created database")
    except ProgrammingError:
        logging.info("Database already existed, continuing")
    finally:
        conn.close()

@manager.command
def run():
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    manager.run()
