"""
Python Extract Transform Load (ETL) example
"""

# %%
import os
import pandas as pd
import requests
from sqlalchemy import create_engine
from dotenv import load_dotenv
from functions import glimpse

api_url = os.getenv("api_url")
# %%
# Extract
def extract() -> dict:
    """
    Extract data from a URL
    """
    data = requests.get(api_url).json()
    return data
# %%
    """
    data = extract()
    data = pd.DataFrame(data)
    data.pipe(glimpse)
    """

#%%
# Transform
def transform(data: dict) -> pd.DataFrame:
    """
    Transform data into a DataFrame
    """
    df = pd.DataFrame(data)
    df = df[df["name"].str.contains("cali", case=False)]
    
    df["domains"] = [','.join(map(str, l)) for l in df["domains"]]
    df["web_pages"] = [','.join(map(str, l)) for l in df["web_pages"]]
    df = df.reset_index(drop=True)
    return df[['domains','country','name','web_pages']]
# %%
#load
def load(df: pd.DataFrame) -> None:
    """
    Load data into a SQLite database
    """
    disk_engine = create_engine("sqlite:///data.db")
    df.to_sql("cal_uni",disk_engine,if_exists='replace',index=False)
# %%
data = extract()
df = transform(data)
load(df)

# %%
#verify
"""
Probando la carga de datos
"""
disk_engine = create_engine("sqlite:///data.db")
df = pd.read_sql_query("SELECT * FROM cal_uni", disk_engine)
df.head()
# %%
