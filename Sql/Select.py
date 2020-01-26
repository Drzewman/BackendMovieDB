from Sql.Connect import create_connection
from Sql.DbPath import path
from Sql.Exec import execSql


def select(where='id>', val='0', sort='id', sortway='asc', column='*'):

    if sort == 'cast':
        sort = '`cast`'
    if where == 'cast':
        where = '`cast`'
    if where == 'id>':
        sql_select = """select """ + column + """ from MOVIES where """ + where + """=""" + val + """ order by """ + sort + """ """ + sortway + """;"""
    else:
        sql_select = """select """ + column + """ from MOVIES where """ + where + """ order by """ + sort + """ """ + sortway + """;"""

    #print(sql_select)
    conn = create_connection(path())

    if conn is not None:

        selected = execSql(conn, sql_select)
        return selected

    else:
        print("Error! cannot create the database connection.")


