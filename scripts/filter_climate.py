# create a function to filter climate hot in colombia and save the result to a new CSV file
import pandas as pd

def filter_climate_data( temp):  
    df = pd.read_csv("./scripts/col_weather.csv") # read the CSV file into a DataFrame

    filtered_df = df[(df['temperature'] > temp)] # filter dataframe por temperature column 
    filtered_df.to_csv("./scripts/hot_weather.csv", index=False) # save the filtered DataFrame to a new CSV file without the index
    
filter_climate_data(25) # call the function with a temperature threshold of 25 degrees  

print("Filtered data saved to hot_weather.csv")