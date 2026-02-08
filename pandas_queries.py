import pandas as pd

# Loading data
df = pd.read_csv("books.csv")

# 1. convert price from string to float
df['Price'] = df['Price'].str.replace('£', '')
df['Price'] = df['Price'].str.replace('Â', '')
df['Price'] = df['Price'].astype(float)


# 2. Top 5 most expensive books
print("Top 5 most expensive books:")
print(df.sort_values('Price', ascending=False).head(5))


# 3. Average price of all books
print("\nAverage price:")
print(df['Price'].mean())


# 4. Count of books by star rating
print("\nBooks by Rating:")
print(df['Rating'].value_counts())


# 5. Number of books in each category
print("\nBooks per Category:")
print(df['Category'].value_counts())


# 6. Books with 'Python' in title
print("\nBooks with 'Python' in Title:")
print(df[df['Title'].str.contains('Python', case=False)])


# 7. Books currently in stock
print("\nBooks in stock:")
print(df[df['Availability'].str.contains("In stock")])


# 8. Out-of-stock books
print("\nBooks out of stock:")
print(df[~df['Availability'].str.contains("In stock")])


# 9. Books missing a description
print("\nBooks with no description:")
print(df[df['Description'] == "No Description"].count())


# 10. Most common book rating
print("\nMost common rating:")
print(df['Rating'].mode()[0])


# 11. Number of unique categories
print("\nNumber of unique categories:")
print(len(df['Category'].unique()))


# 12. List of all unique categories
print("\nUnique categories:")
print(df['Category'].unique())


# 13. Books sorted alphabetically by title
print("\nBooks sorted by Title:")
print(df.sort_values("Title"))


# 14. Books with long descriptions (>300 chars)
print("\nBooks with long descriptions:")
print(df[df['Description'].str.len() > 300])


# 15. Cheapest book in each category
print("\nCheapest book in each category:")
categories = df['Category'].unique()
for category in categories:
    print(f"\nCheapest book in each category: {category}")
    category_books = df[df['Category'] == category]
    cheapest = category_books.sort_values('Price').head()
    print(cheapest[['Title', 'Price']])


# 16.Top 3 most expensive books per category
print("\nTop 3 most expensive books per category:")
for category in categories:
    print(f"\nTop 3 books in category: {category}")
    category_books = df[df['Category'] == category]
    top_3 = category_books.sort_values('Price', ascending=False).head(3)
    print(top_3[['Title', 'Price']])


# 17. Books with title length > 50 characters
print("\nBooks with title length > 50 characters:")
print(df[df['Title'].str.len() > 50])


# 18. Add a column for "is_expensive" (price > £40)
print("\nAdding new column (is expensive):")
df['is_expensive'] = df['Price'] > 40
print(df[['Title', 'Price', 'is_expensive']].head())


# 19. Count of expensive books by category
print("\nCount of Expensive books:")
expensive_books = df[df['is_expensive']]
categories = expensive_books['Category'].unique()

for category in categories:
    count = len(expensive_books[expensive_books['Category'] == category])
    print(f"{category}: {count} expensive books")


# 20. Save filtered DataFrame of in-stock & expensive books
expensive_in_stock = df[(df['Availability'].str.contains('In stock')) & (df['Price'] > 40)]
print(expensive_in_stock)