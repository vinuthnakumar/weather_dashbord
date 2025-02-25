import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
data = pd.read_csv('data.csv')

# Basic data analysis
average_column = data['selected_column'].mean()
print(f'Average of selected column: {average_column}')

# Bar chart
plt.figure(figsize=(10, 6))
data['category_column'].value_counts().plot(kind='bar')
plt.title('Bar Chart of Categories')
plt.xlabel('Categories')
plt.ylabel('Counts')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['x_column'], data['y_column'])
plt.title('Scatter Plot of X vs Y')
plt.xlabel('X Column')
plt.ylabel('Y Column')
plt.show()

# Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()