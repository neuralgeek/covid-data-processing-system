def clean_data():
    df = pd.read_sql("SELECT * FROM covid_raw", engine)
    
    # Drop unnecessary columns
    df.drop(columns=['Lat', 'Long'], inplace=True)
    
    # Rename columns
    df.rename(columns={'Country/Region': 'country', 'Province/State': 'state'}, inplace=True)
    
    # Convert wide format to long format
    df_melted = df.melt(id_vars=['state', 'country'], var_name='date', value_name='cases')
    df_melted['date'] = pd.to_datetime(df_melted['date'])
    
    # Store cleaned data
    df_melted.to_sql('covid_cleaned', engine, if_exists='replace', index=False)
    print("Data cleaned and stored successfully!")

clean_data()