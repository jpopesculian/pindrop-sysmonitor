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

def fetch(conn, table, sort=1, page=0, size=20):
    c = conn.cursor()
    sort = "DESC" if sort is 1 else "ASC"
    offset = page*size
    c.execute('''
        SELECT * FROM %s
        ORDER BY timestamp %s
        LIMIT %s
        OFFSET %s
    ''' % (table, sort, size, offset))
    result = [_parse_row(row) for row in c.fetchall()]
    return {
        'page': page,
        'length': len(result),
        'events': result
    }




def fetch_last(conn, table):
    c = conn.cursor()
    c.execute('''
        SELECT * FROM %s ORDER BY timestamp DESC LIMIT 1
    ''' % table)
    result = c.fetchone()
    return _parse_row(result)

def _parse_row(row):
    return {
        'id': row[0],
        'timestamp': row[1],
        'stats': json.loads(row[2])
    }
