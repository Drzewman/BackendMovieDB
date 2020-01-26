from Sql.Connect import create_connection
from Sql.DbPath import path
from Sql.Exec import execSql

def update(column, val,title):
    conn = create_connection(path())
    val = val.replace('\'', '\'\'')
    sql_insert = """UPDATE MOVIES SET """+column+"""='"""+val+"""' WHERE TITLE='"""+title+ """';"""

    print(sql_insert)



    if conn is not None:

        execSql(conn, sql_insert)
    else:
        print("Error! cannot create the database connection.")


def trim():
    conn = create_connection(path())
    sql_insert = """UPDATE MOVIES SET TITLE = trim(TITLE);"""

    if conn is not None:

        execSql(conn, sql_insert)
    else:
        print("Error! cannot create the database connection.")



