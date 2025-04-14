import pandas as pd
from sqlalchemy import create_engine 


#STEP 5
engine = create_engine('postgresql+psycopg2://username:password@localhost:5432/is303')
df.to_sql('sale',engine, if_exists = 'replace', index = false)


#STEP 6

print("You've imported the excel file into your postgres database.")
