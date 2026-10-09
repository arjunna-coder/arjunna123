import pandas as pd
import sqlite3
df= pd.read_excel('mark.xlsx')
#database = "mark.sqlite"
conn = sqlite3.connect("mark.sqlite")
df.to_sql(name='Users',con=conn,if_exists='replace',index=False)

conn.close()