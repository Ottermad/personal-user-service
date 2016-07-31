from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from app.settings import DATABASE_NAME
from app.models import db


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

def create_tables():
    logging.info("Creating tables")
    try:
        db.create_all()
        logging.info("Created tables")
    except:
        logging.error("Failed to create tables")
