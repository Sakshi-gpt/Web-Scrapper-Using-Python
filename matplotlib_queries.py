import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv("books.csv")
df['Price'] = df['Price'].str.replace('Â', '').str.replace('£', '')
df['Price'] = df['Price'].astype(float)
df['Rating'] = df['Rating'].str.strip()

# 1. Average Price per Category
avg_prices = df.groupby('Category')['Price'].mean()
avg_prices.plot.bar()
plt.title('Average Price per Category')
plt.xlabel('Category')
plt.ylabel('Average Price (£)')
plt.tight_layout()
plt.show()

# 2. Number of Books by Rating
rating_counts = df['Rating'].value_counts()
rating_counts.plot.bar()
plt.title('Books by Rating')
plt.xlabel('Rating')
plt.ylabel('Number of Books')
plt.tight_layout()
plt.show()

# 3. In Stock vs Out of Stock
in_stock = df['Availability'].str.contains('In stock')
stock_status = pd.Series([in_stock.sum(), (~in_stock).sum()], index=['In Stock', 'Out of Stock'])
stock_status.plot.bar()
plt.title('Stock Status')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# 4. Top 10 Most Expensive Books
top10 = df.sort_values('Price', ascending=False).head(10)
plt.barh(top10['Title'], top10['Price'])
plt.title('Top 10 Most Expensive Books')
plt.xlabel('Price (£)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# 5. Top 10 Categories by Book Count
category_counts = df['Category'].value_counts().head(10)
category_counts.plot.bar()
plt.title('Top 10 Categories by Book Count')
plt.xlabel('Category')
plt.ylabel('Number of Books')
plt.tight_layout()
plt.show()

# 6. Book Price Distribution
plt.hist(df['Price'], bins=20)
plt.title('Book Price Distribution')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.tight_layout()
plt.show()

# 7. Title Length Distribution
df['TitleLength'] = df['Title'].str.len()
plt.hist(df['TitleLength'], bins=20)
plt.title('Title Length Distribution')
plt.xlabel('Title Length (characters)')
plt.ylabel('Number of Books')
plt.tight_layout()
plt.show()

# 8. Boxplot of Prices by Rating
df.boxplot(column='Price', by='Rating')
plt.title('Boxplot of Price by Rating')
plt.suptitle('')
plt.xlabel('Rating')
plt.ylabel('Price (£)')
plt.tight_layout()
plt.show()

# 9. Number of Books Over Price Thresholds
thresholds = [10, 20, 30, 40, 50]
counts = []
for threshold in thresholds:
    count = len(df[df['Price'] > threshold])
    counts.append(count)
plt.plot(thresholds, counts, marker='o')
plt.title('Books Over Price Thresholds')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.tight_layout()
plt.show()

# 10. Top Categories with Most 5-Star Books
five_star = df[df['Rating'] == 'Five']
top_5star_categories = five_star['Category'].value_counts().head(10)
top_5star_categories.plot.bar()
plt.title('Top Categories with 5-Star Books')
plt.xlabel('Category')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# 12. Top 10 Longest Book Descriptions
df['DescLength'] = df['Description'].str.len()
longest_desc = df.sort_values('DescLength', ascending=False).head(10)
plt.barh(longest_desc['Title'], longest_desc['DescLength'])
plt.title('Top 10 Longest Book Descriptions')
plt.xlabel('Description Length')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# 13. Pie Chart of Category Distribution (Top 6)
top_categories = df['Category'].value_counts().head(6)
top_categories.plot.pie(autopct='%1.1f%%')
plt.title('Top 6 Categories')
plt.ylabel('')
plt.tight_layout()
plt.show()

# 14. Line Chart of Books per Rating
rating_line = df['Rating'].value_counts().sort_index()
plt.plot(rating_line.index, rating_line.values, marker='o')
plt.title('Books per Rating')
plt.xlabel('Rating')
plt.ylabel('Number of Books')
plt.tight_layout()
plt.show()

# 15. Price Comparison by Rating bar
avg_price_by_rating = df.groupby('Rating')['Price'].mean()
avg_price_by_rating.plot.bar()
plt.title('Average Price by Rating')
plt.xlabel('Rating')
plt.ylabel('Average Price (£)')
plt.tight_layout()
plt.show()