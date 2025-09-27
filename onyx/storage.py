import sqlite3
from contextlib import contextmanager
from datetime import datetime

DB_PATH = "onyx.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            source TEXT,
            title TEXT,
            snippet TEXT,
            url TEXT,
            timestamp TEXT,
            metadata TEXT
        )
    ''')
    conn.commit()
    conn.close()

@contextmanager
def get_db_session():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()

def save_results(session, query, results):
    c = session.cursor()
    for res in results:
        c.execute(
            'INSERT INTO results (query, source, title, snippet, url, timestamp, metadata) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (query, res['metadata']['source'], res['title'], res['snippet'], res['url'], res['timestamp'], str(res['metadata']))
        )
    session.commit()
