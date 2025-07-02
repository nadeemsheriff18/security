import sqlite3
import json

def init_db():
    conn = sqlite3.connect("cves.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cves(
            id TEXT PRIMARY KEY,
            title TEXT,
            description TEXT,
            severity TEXT,
            published TEXT
        )
    ''')

    conn.commit()
    conn.close()

def load_data_from_json():
    with open("data.json") as f:
        data = json.load(f)

    conn = sqlite3.connect("cves.db")
    cursor = conn.cursor()

    for item in data:
        cursor.execute('''
            INSERT OR REPLACE INTO cves (id, title, description, severity, published)
            VALUES (?, ?, ?, ?, ?)
        ''', (item['id'], item['title'], item['description'], item['severity'], item['published']))

    conn.commit()
    conn.close()   
