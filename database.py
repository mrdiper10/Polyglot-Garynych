import sqlite3
from typing import List, Tuple

DB_PATH = 'polyglot.db'  # Путь к вашей базе данных

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            language TEXT NOT NULL,
            word TEXT NOT NULL,
            translation TEXT,
            known INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_word_to_db(user_id: int, language: str, word: str, translation: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO words (user_id, language, word, translation, known) VALUES (?, ?, ?, ?, 0)",
        (user_id, language, word, translation)
    )
    conn.commit()
    conn.close()

def get_words(user_id: int) -> List[Tuple[str, str, str, int]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT word, translation, language, known FROM words WHERE user_id = ?",
        (user_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return [(row['word'], row['translation'], row['language'], row['known']) for row in rows]

def clear_user_dictionary(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM words WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

def get_words_count_by_language(user_id: int, language: str) -> Tuple[int, int]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*), SUM(known) FROM words WHERE user_id = ? AND language = ?",
        (user_id, language)
    )
    total, known = cursor.fetchone()
    conn.close()
    if known is None:
        known = 0
    return total, known
