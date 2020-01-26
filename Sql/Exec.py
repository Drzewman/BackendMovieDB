from sqlite3 import Error


def execSql(conn, sqlcode, *args):
    try:

        c = conn.cursor()
        c.execute(sqlcode, *args)
        conn.commit()
        rows = c.fetchall()
        return rows

    except Error as e:
        print(e)


