import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'game.db')

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Characters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER, 
            gender TEXT,
            skin_color TEXT,
            shirt_model TEXT,
            shirt_color TEXT,
            hair_model TEXT,
            hair_color TEXT,
            tail_model TEXT,
            tail_color TEXT,
            pants_model TEXT,
            pants_color TEXT,
            sucks_model TEXT,
            sucks_color TEXT,
            shoes_model TEXT,
            shoes_color TEXT,
            wings_model TEXT,
            wings_color TEXT,
            eye_model TEXT,
            eye_color TEXT,
            horn_model TEXT,
            horn_color TEXT,
            gun_model TEXT,
            gun_color TEXT  
        )
    """)

    conn.commit()
    conn.close()
    print("Database and table created successfully.")

if __name__ == "__main__":
    create_database()
