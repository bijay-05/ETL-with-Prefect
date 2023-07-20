import polars as pl
from configparser import ConfigParser

parser = ConfigParser()
    # read config file
parser.read("database.ini")

    # get section, default to postgresql
keys = {}
if "postgres" in parser.sections():
    params = parser.items("postgres")
    for param in params:
        keys[param[0]] = param[1]



conn_string = f"postgres://{keys[user]}:{keys[password]}@{keys[host]}:{keys[port]}/{keys[database]}"

query = f"SELECT * FROM public.{table_name} WHERE date LIKE '2023-07-18*'"
    
    # read the data from database into dataframe
dataframe = pl.read_database(connection_uri=conn_string, query=query)

print(dataframe.dtypes)
