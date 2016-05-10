import sqlite3, os, json

def connect():
    data_dir = "%s/data" % os.path.dirname(os.path.abspath(__file__))
    db = "%s/stats.db" % data_dir
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    conn = sqlite3.connect(db)
    _init_tables(conn)
    return conn


def _init_tables(conn):
    c = conn.cursor()
    for table in ['Mem', 'Cpu', 'Disk']:
        try:
            c.execute('''
                CREATE TABLE %s(
                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                  data TEXT
                )
            ''' % table)
            conn.commit()
        except sqlite3.OperationalError:
            pass

def insert(conn, table, data):
    c = conn.cursor()
    c.execute("INSERT INTO %s ('data') VALUES ('%s')" % (table, json.dumps(data)))
    conn.commit()
