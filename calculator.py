import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("24_08_25to24_09_24.csv")



Amount_col=df["Amount"]
Category_col=df["Category"]
Currency_col=df["Currency"]

exchange_rate_cny_to_hkd = 1.11
df['Amount_in_HKD'] = df.apply(
    lambda row: row['Amount'] * exchange_rate_cny_to_hkd if row['Currency'] == 'CNY' else row['Amount'], axis=1
)

#pie plot
category_sums = df.groupby('Category')['Amount_in_HKD'].sum()
plt.figure(figsize=(6,6))
plt.pie(category_sums, labels=category_sums.index, autopct='%1.1f%%')

# Add a title
plt.title('Expense Distribution by Category')

# Show the plot
plt.savefig("pie_category.pdf")
plt.close()


# bar plot
# Create a bar chart based on the aggregated data
colors = plt.cm.get_cmap('tab10', len(category_sums))  # Using a colormap (e.g., 'tab10') for distinct colors
plt.figure(figsize=(15,15))
plt.bar(category_sums.index, category_sums.values, color=[colors(i) for i in range(len(category_sums))])# Add labels and title
plt.xlabel('Category')
plt.ylabel('Total Amount (HKD)')
plt.title('Total Amount by Category')

# Rotate the category labels on the x-axis for better readability if there are many categories
plt.xticks(rotation=45)
plt.savefig("bar_category.pdf")
plt.close()
