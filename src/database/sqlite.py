import sqlite3

# SQLite Database
def sql_database():
    conn = sqlite3.connect("data.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS Data
                (XCOORD            BLOB NOT NULL,
                YCOORD             BLOB NOT NULL
                );''')
    conn.close()
def save_progress(xcoord, ycoord):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Data")
    parameters  = (xcoord, ycoord)
    cursor.execute("INSERT INTO Data VALUES (?,?)", parameters)
    conn.commit()
    conn.close()
def progress_retrieve():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Data")
    retrieve_data = cursor.fetchall()
    conn.close()
    return retrieve_data

sql_database()
