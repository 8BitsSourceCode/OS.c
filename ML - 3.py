import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('books.csv')

# 🔹 Bar Graph (Bike Type)
dataset['Type'].value_counts().plot(kind='bar')
plt.title('Number of Bikes by Type')
plt.show()

# 🔹 Scatter Plot (Engine_CC vs Price)
plt.scatter(dataset['Engine_CC'], dataset['Price'])
plt.xlabel('Engine CC')
plt.ylabel('Price')
plt.title('Engine CC vs Price')
plt.show()

# 🔹 Box Plot (Price)
sns.boxplot(x=dataset['Price'])
plt.title('Price Distribution')
plt.show()

# 🔹 Histogram (Mileage)
plt.hist(dataset['Mileage'], bins=8)
plt.title('Mileage Distribution')
plt.show()

# 🔹 Line Graph (Bikes per Year)
year_count = dataset['Year'].value_counts().sort_index()
plt.plot(year_count.index, year_count.values)
plt.title('Bikes by Year')
plt.show()
