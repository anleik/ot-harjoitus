import sqlite3

# SQLite Database
def sql_database():
    """Luo tallentamista varten taulun jos sitä ei vielä ole.
    """

    conn = sqlite3.connect("data.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS Data
                (XCOORD            BLOB NOT NULL,
                YCOORD             BLOB NOT NULL,
                LEVEL              BLOB NOT NULL
                );''')
    conn.close()
def save_progress(xcoord, ycoord, level):
    """Tallentaa pelaajan sijainnin tauluun.

    Args:
        xcoord (int): Pelaajan x-koordinaatti.
        ycoord (int): Pelaajan y-koordinaatti.
        level  (int): Taso.
    """

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Data")
    parameters  = (xcoord, ycoord, level)
    cursor.execute("INSERT INTO Data VALUES (?,?,?)", parameters)
    conn.commit()
    conn.close()
def progress_retrieve():
    """Hakee pelaajan tallennetun sijainnin taulusta.

    Returns:
        X- ja Y-koordinaatit.
    """

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Data")
    retrieve_data = cursor.fetchall()
    conn.close()
    return retrieve_data

sql_database()
