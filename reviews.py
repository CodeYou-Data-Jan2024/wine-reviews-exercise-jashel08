# add your code here
import pandas as pd

#Create a Python program that reads in the `data/winemag-data-130k-v2.csv.zip` 
#file. Create a summary of the data that contains the name, number of reviews, 
#and the average points for each unique country in the dataset. Write the summary
#data to a new file in the `data` folder named `reviews-per-country.csv`.

#The csv file created by your program should be saved in the `data` folder.
#The csv file created by your program should be added, committed and pushed 
#to GitHub.
#The column names should match the example above.
# The values in the points column should be rounded to 1 decimal point.

filepath = 'data\\winemag-data-130k-v2.csv.zip'
reviews = pd.read_csv(filepath, index_col=0, compression='zip')

country_ser = pd.Series(reviews.country.unique())
country_ser_df = pd.DataFrame({'country': country_ser})

country_count = pd.Series(reviews.groupby('country').country.count())
country_count_df = pd.DataFrame({'count': country_count})

combo_df = pd.merge(country_ser_df, country_count_df, on ='country', how ='inner') 

points_ser = pd.Series(reviews.groupby('country').points.mean().round(1))
points_df = pd.DataFrame({'points': points_ser})

reviews_per_country = pd.merge(combo_df, points_ser, on= 'country', how='inner')
reviews_per_country

reviews_per_country.to_csv('data\\reviews-per-country.csv', sep='|', index=False)


