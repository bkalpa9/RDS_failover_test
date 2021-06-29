import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()


def get_pg_write_conn():
    try:
        conn = psycopg2.connect(os.getenv("WRITE_DATABASE_URL"))
        conn.set_session(autocommit=True)
        cur = conn.cursor()
        print('PG Database connected...',cur)
        return cur
    except Exception as e:
        print(e)
        return None


def get_read_conn():
    try:
        conn = psycopg2.connect(os.getenv("READ_DATABASE_URL"))
        conn.set_session(autocommit=True)
        cur = conn.cursor()
        print('PG Database connected...',cur)
        return cur
    except Exception as e:
        print(e)
        return None

if __name__ == '__main__':
    get_pg_write_conn()