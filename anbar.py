from sqlalchemy import create_engine as ce
from sqlalchemy import Table, MetaData
from sqlalchemy import inspect


reserveds = ['alembic_version']
url = 'sqlite:///app.db'
engine = ce(url)
connection = engine.connect()
met = MetaData(engine)
inspector = inspect(engine)


tables = []
for tname in inspector.get_table_names():
    tables.append(tname)
for r in reserveds:
    try:
        tables.remove(r)
    except:
        pass
print(tables)
