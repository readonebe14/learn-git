import pandas as pd
from sqlalchemy import create_engine

df_users_w_postal_code = pd.read_csv ("/002_Documents/001_Private/LEARNING/DATA ENGINEER/Digital Skola/Sesi 17/Project 3/source/users_w_postal_code.csv", sep = ",")
df_region = pd.read_csv("/002_Documents/001_Private/LEARNING/DATA ENGINEER/Digital Skola/Sesi 17/Project 3/source/region.csv", sep=",")

engine = create_engine("postgresql://postgres:welcome123@localhost:5432/postgres")

df_users_w_postal_code.to_sql("users_w_postal_code", engine, if_exists="replace", index=False)
df_region.to_sql("region", engine, if_exists="replace", index=False)

engine.dispose()