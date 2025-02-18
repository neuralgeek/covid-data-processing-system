import pandas as pd
import sqlite3

# Load the dataset from GitHub
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
df = pd.read_csv(url)

# Data Cleaning: Handling missing values
df.fillna("Unknown", inplace=True)

# Save to SQLite
conn = sqlite3.connect("covid_data.db")
df.to_sql("covid_cases", conn, if_exists="replace", index=False)
conn.close()
