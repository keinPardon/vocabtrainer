import sqlite3

def connect_to_db():
    conn = sqlite3.connect('vocabtrainer.db')  
    return conn

def create_vocab_table():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vocabulary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT,
            target_language TEXT,
            translation TEXT,
            difficulty_level INTEGER,
            additional_notes TEXT 
        )
    """)

    conn.commit()  
    conn.close()

def add_word(word, target_language, translation, difficulty_level=None, additional_notes=None):
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO vocabulary (word, target_language, translation, difficulty_level, additional_notes)
        VALUES (?, ?, ?, ?, ?)""", 
        (word, target_language, translation, difficulty_level, additional_notes)
    )

    conn.commit()
    conn.close()

def get_random_word(target_language):
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM vocabulary 
        WHERE target_language = ?
        ORDER BY RANDOM()
        LIMIT 1""", 
        (target_language,)
    )

    result = cursor.fetchone()

    conn.close()
    return result

# Ensure the table exists when you start your app
create_vocab_table() 
