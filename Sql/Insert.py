from Request.FromApi import Request
from Sql.Connect import create_connection
from Sql.DbPath import path
from Sql.Exec import execSql
from Sql.GetColumn import getcolumn
from Sql.Select import select
from Sql.Update import update, trim


def insert(title):

    title = "'"+Request(title)['Title']+"'"
    sel = select(column='title', where='title= '+ title)

    if sel==[]:

        sql_insert = """insert into MOVIES (TITLE) VALUES ("""+title+""");"""
        conn = create_connection(path())
        if conn is not None:

            execSql(conn, sql_insert)
        else:
            print("Error! cannot create the database connection.")
        trim()
        title = 'title = ' + title
        for row in select(column='title', where=title):

            for key, val in Request(row[0]).items():

                for column in getcolumn():

                    if key.lower() == column.lower():
                        if key.lower() == 'title':
                            title = val
                            continue
                        update(key, val, title)
    else:
        print('There is already film named ' + title)






