import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create announcements table
cursor.execute("""
CREATE TABLE IF NOT EXISTS announcements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database created successfully.")
