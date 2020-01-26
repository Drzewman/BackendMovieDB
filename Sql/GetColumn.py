from sqlite3 import Error
from Sql.Connect import create_connection
from Sql.DbPath import path


def getcolumn():
    sql_insert = """SELECT name FROM PRAGMA_TABLE_INFO('MOVIES');"""
    conn = create_connection(path())
    if conn is not None:

        try:

            c = conn.cursor()
            c.execute(sql_insert)
            conn.commit()
            rows = c.fetchall()
            columnname = []
            for row in rows:
                if row[0] == 'ID':
                    continue

                columnname.append(row[0])

        except Error as e:
            print(e)


    else:
        print("Error! cannot create the database connection.")

    return columnname



