import pandas as pd
import requests as re
from bs4 import BeautifulSoup

product_names = []
prices = []
descriptions = []
ratings = []

for i in range(2, 10):
    url = "https://www.flipkart.com/search?q=phone+undr+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on" + str(i)
    r = re.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    names = soup.find_all("div", class_="_4rR01T")
    for name in names:
        product_names.append(name.text.strip()) ### strip() are use for romve a extra space

    prices_tags = soup.find_all("div", class_="_30jeq3 _1_WHN1")
    for price_tag in prices_tags:
        prices.append(price_tag.text.strip())

    descriptions_tags = soup.find_all("ul", class_="_1xgFaf")
    for description_tag in descriptions_tags:
        descriptions.append(description_tag.text.strip())

    ratings_tags = soup.find_all("div", class_="_3LWZlK")
    for rating_tag in ratings_tags:
        ratings.append(rating_tag.text.strip())

# Check lengths of all lists to ensure they are the same
print(len(product_names), len(prices), len(descriptions), len(ratings))

# Create DataFrame if all lists have the same length
table = pd.DataFrame({
        "Product Name": product_names,
        "Price": prices,
        "Description": descriptions,
        "Rating": ratings
    })

# Save to CSV
table.to_csv("Scrape.csv", index=False)

###Print first few rows of the DataFrame
print(table.head())

