import sqlite3

def get_db():
    return sqlite3.connect("cves.db")

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cves (
            id TEXT PRIMARY KEY,
            description TEXT,
            published TEXT,
            modified TEXT,
            score REAL
        )
    """)
    conn.commit()
    conn.close()
