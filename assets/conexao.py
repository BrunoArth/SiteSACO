import psycopg2
import  psycopg2.extras

def conectar():
    conn = psycopg2.connect(
        host = 'localhost',
        database = '',
        user = '',
        password = '',
    )
    return conn

def receberCur(conn):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return cur
