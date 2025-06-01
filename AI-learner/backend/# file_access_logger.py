# file_access_logger.py
import sqlite3
from datetime import datetime
import os

DB_NAME = 'llm_data.db'

# --- STEP 1: Initialize the database and table (only once) ---
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS file_access (
            file_path TEXT PRIMARY KEY,
            start_date TEXT,
            end_date TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print(f"\u2705 Database '{DB_NAME}' initialized.")

# --- STEP 2: Update or insert file access entry ---
def update_access_log(file_path):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM file_access WHERE file_path = ?', (file_path,))
    record = cursor.fetchone()

    if record is None:
        # First time access
        cursor.execute('''
            INSERT INTO file_access (file_path, start_date, end_date)
            VALUES (?, ?, ?)
        ''', (file_path, now, now))
    else:
        # Update only the end_date
        cursor.execute('''
            UPDATE file_access SET end_date = ? WHERE file_path = ?
        ''', (now, file_path))

    conn.commit()
    conn.close()

    print(f"\u2705 Access log updated: {file_path} | Start: {record[1] if record else now} | End: {now}")




# --- STEP 3: View all access logs ---
def view_access_log():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM file_access')
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("\nNo access logs found.")
    else:
        print("\nAccess Log:")
        for row in rows:
            print(f"\U0001F4C1 {row[0]} | Start: {row[1]} | End: {row[2]}")





# --- CLI Interface ---
def main():
    init_db()
    while True:
        print("\nChoose an option:")
        print("1. Update file access")
        print("2. View access log")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == '1':
            path = input("Enter file name or path: ").strip()
            if os.path.exists(path):
                update_access_log(path)
            else:
                print("\u274C File does not exist.")

        elif choice == '2':
            view_access_log()

        elif choice == '3':
            print("\nExiting. Goodbye!")
            break

        else:
            print("\u26A0\uFE0F Invalid choice. Try again.")

if __name__ == "__main__":
    main()
