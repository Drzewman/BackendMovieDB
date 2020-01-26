import os
from pathlib import Path


def path():
    a = Path('Sql').parent.resolve().parent.resolve()
    path = os.path.join(a, "Sql\movies.sqlite")
    return path


