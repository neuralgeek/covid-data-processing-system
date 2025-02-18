from mage_ai.data_preparation.decorators import data_loader, transformer, data_exporter

@data_loader
def ingest_data():
    df = pd.read_sql("SELECT * FROM covid_raw", engine)
    return df

@transformer
def process_data(df):
    df_cleaned = df.drop(columns=['Lat', 'Long'])
    df_cleaned.rename(columns={'Country/Region': 'country', 'Province/State': 'state'}, inplace=True)
    return df_cleaned

@data_exporter
def store_data(df_cleaned):
    df_cleaned.to_sql('covid_cleaned', engine, if_exists='replace', index=False)