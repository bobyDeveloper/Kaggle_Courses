import pandas as pd

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")

print(wine_reviews)

print(wine_reviews.shape)

print(wine_reviews.shape[0])

print(wine_reviews.shape[1])

print(wine_reviews.head)

wine_reviews2 = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews2.head())

# select country from wines
wine_country = wine_reviews.country
print (wine_country)

# select top 1 country from wines
wine_country_0 = wine_reviews['country'][0]
print (wine_country_0)

# select top 1 * from wines
wine_all_0 = wine_reviews.iloc[0]
print (wine_all_0)

# select country from wines
wine_country_all = wine_reviews.iloc[:, 1]
print (wine_country_all)

# select top 3 country from wines
wine_country_3 = wine_reviews.iloc[:3, 1]
print (wine_country_3)

# select country country from wines
wine_country_2 = wine.reviews.iloc[1:3, 1]
print (wine_country_2)

# select top 6 country from wines
print('\n top 6');
wines_range = wine_reviews.iloc[ [0, 1, 2, 3, 4, 5], [1, 2, 3]]
print(wines_range)

# select bottom 

