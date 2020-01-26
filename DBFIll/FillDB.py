from Request.FromApi import Request
from Sql.GetColumn import getcolumn
from Sql.Select import select
from Sql.Update import trim, update


def fillDb():

    trim()
    for row in select(column="TITLE"):

        for key, val in Request(row[0]).items():

            for column in getcolumn():

                if key.lower() == column.lower():
                    if key.lower() == 'title':
                        title = val
                        continue
                    update(key, val, title)
