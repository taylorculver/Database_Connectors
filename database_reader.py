from sqlalchemy import create_engine
import pandas as pd


engine = create_engine('sqlite:///Chinook.sqlite')
table_names = engine.table_names()
print(table_names)
connection = engine.connect()
artists_query = connection.execute('select * from Artist;')
data_frame = pd.DataFrame(artists_query.fetchall())
data_frame.columns = artists_query.keys()  # set column headers to values in table
connection.close()
# print(data_frame.head())

'''OR less complicated'''

with engine.connect() as connection:
    artists_query = connection.execute('select * from Artist;')
    data_frame = pd.DataFrame(artists_query.fetchmany(size=5))  # select only top 5 records
    data_frame.columns = artists_query.keys()

'''OR even less complicated'''

engine = create_engine('sqlite:///Chinook.sqlite')
data_frame = pd.read_sql_query("SELECT * FROM Artist", engine)
print(data_frame.get_values())