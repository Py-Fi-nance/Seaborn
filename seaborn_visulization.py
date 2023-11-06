# -*- coding: utf-8 -*-
"""Seaborn Visulization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sZ9ErKp36c8YqBwgLmmbo_N3mzo1l0r0
"""

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 11, 12, 12]

# Setting a style and color palette
sns.set_style("whitegrid")  # Sets background to white with gray grid lines
palette = sns.color_palette("viridis", n_colors=len(x))  # Uses the 'viridis' color palette

# Create scatter plot using Seaborn
sns.scatterplot(x=x, y=y, palette=palette, size=y, sizes=(50,200), hue=y, legend="full")

# Adding title and labels
plt.title('Colorful Scatter Plot with Seaborn')
plt.xlabel('X Values')
plt.ylabel('Y Values')

# Display the plot
plt.show()

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 11, 12, 12]
y2 = [3, 5, 4, 6, 7, 7, 10, 10, 13, 14]  # New data set

# Setting a style
sns.set_style("whitegrid")  # Sets background to white with gray grid lines

# Create line plot using Seaborn for both y and y2
sns.lineplot(x=x, y=y, label='y', linewidth=2.5)
sns.lineplot(x=x, y=y2, label='y2', linewidth=2.5)

# Adding title, labels, and legend
plt.title('Multiple Lines Plot with Seaborn')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend()

# Display the plot
plt.show()

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd  # Added this for DataFrame conversion

# Sample data
data_dict = {
    'Category': ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B'],
    'Price': [15, 25, 14, 35, 45, 35, 25, 55, 50, 60]
}

# Convert dictionary to DataFrame
data = pd.DataFrame(data_dict)

# Create catplot using Seaborn
sns.catplot(x='Category', y='Price', data=data, kind='bar')

# Adding title
plt.title('Bar Catplot with Seaborn')

# Display the plot
plt.show()

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd  # For DataFrame conversion

# Sample data
data_dict = {
    'Category': ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B'],
    'Price': [15, 25, 14, 35, 45, 35, 25, 55, 50, 60]
}

# Convert dictionary to DataFrame
data = pd.DataFrame(data_dict)

# Create catplot using Seaborn with kind='box'
sns.catplot(x='Category', y='Price', data=data, kind='box')

# Adding title
plt.title('Boxplot with Seaborn')

# Display the plot
plt.show()

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd  # For DataFrame conversion

# Sample data
data_dict = {
    'Category': ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B'],
    'Price': [15, 25, 14, 35, 45, 35, 25, 55, 50, 60]
}

# Convert dictionary to DataFrame
data = pd.DataFrame(data_dict)

# Create violin plot using Seaborn
sns.violinplot(x='Category', y='Price', data=data, inner='quartile')

# Adding title
plt.title('Violin Plot with Seaborn')

# Display the plot
plt.show()

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd  # For DataFrame conversion

# Sample data with more categories and values
data_dict = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C'],
    'Price': [15, 20, 18, 25, 30, 22, 14, 32, 28, 35, 34, 26, 27, 24, 29, 37, 33, 36]
}

# Convert dictionary to DataFrame
data = pd.DataFrame(data_dict)

# Create strip plot using Seaborn
palette = sns.color_palette("viridis", n_colors=len(data['Category'].unique()))  # Defining a color palette
sns.stripplot(x='Category', y='Price', data=data, jitter=True, marker='o', alpha=0.7, palette=palette)

# Adding title
plt.title('Colorful Strip Plot with Seaborn')

# Display the plot
plt.show()

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  # For random data generation

# Generating larger dataset
np.random.seed(0)  # Setting seed for reproducibility
categories = ['A', 'B', 'C', 'D', 'E']
n_points = 1000

data_dict = {
    'Category': np.random.choice(categories, n_points),
    'Price': np.random.rand(n_points) * 100  # Prices between 0 and 100
}

# Convert dictionary to DataFrame
data = pd.DataFrame(data_dict)

# Create swarm plot using Seaborn
palette = sns.color_palette("viridis", n_colors=len(categories))
sns.swarmplot(x='Category', y='Price', data=data, palette=palette, size=5)

# Adding title and labels
plt.title('Swarm Plot with Seaborn for Large Dataset')
plt.xlabel('Product Category')
plt.ylabel('Price ($)')

# Display the plot
plt.tight_layout()  # Adjusts the plot dimensions for better display
plt.show()

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  # For random data generation

# Generating larger dataset
np.random.seed(42)  # Setting seed for reproducibility
categories = ['A', 'B', 'C', 'D', 'E']
n_points = 1000

data_dict = {
    'Category': np.random.choice(categories, n_points),
    'Value': np.random.rand(n_points) * 100  # Random values between 0 and 100
}

# Convert dictionary to DataFrame
data = pd.DataFrame(data_dict)

# Create bar plot using Seaborn
palette = sns.color_palette("viridis", n_colors=len(categories))
sns.barplot(x='Category', y='Value', data=data, palette=palette, ci='sd')  # Plotting with standard deviation as the error bar

# Adding title and labels
plt.title('Bar Plot with Seaborn')
plt.xlabel('Category')
plt.ylabel('Average Value')

# Display the plot
plt.tight_layout()  # Adjusts the plot dimensions for better display
plt.show()

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  # For random data generation

# Generating larger dataset
np.random.seed(10)  # Setting seed for reproducibility
categories = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
n_points = 2000

data_dict = {
    'Category': np.random.choice(categories, n_points, p=[0.1, 0.15, 0.2, 0.15, 0.1, 0.1, 0.1, 0.1])
}

# Convert dictionary to DataFrame
data = pd.DataFrame(data_dict)

# Using Seaborn's countplot function to visualize the counts of each category
palette = sns.color_palette("viridis", n_colors=len(categories))
sns.countplot(x='Category', data=data, palette=palette, order=sorted(data['Category'].unique()))

# Adding title and labels
plt.title('Count Plot with Seaborn for Large Dataset')
plt.xlabel('Category')
plt.ylabel('Count')

# Display the plot
plt.tight_layout()  # Adjusts the plot dimensions for better display
plt.show()

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np  # For random data generation

# Generating larger dataset
np.random.seed(15)  # Setting seed for reproducibility

# Generating 5000 data points from a normal distribution
values = np.random.randn(5000)

# Using Seaborn's histplot function to visualize the data distribution
palette = sns.color_palette("viridis", n_colors=2)
sns.histplot(values, bins=50, kde=True, color=palette[0], line_kws={"color": palette[1], "linewidth": 2})

# Adding title and labels
plt.title('Histogram with Seaborn')
plt.xlabel('Value')
plt.ylabel('Count')

# Display the plot
plt.tight_layout()  # Adjusts the plot dimensions for better display
plt.show()

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generating dataset
np.random.seed(42)
data = np.random.randn(1000)

# Using Seaborn's kdeplot function to visualize the data distribution
palette = sns.color_palette("viridis", n_colors=2)
sns.kdeplot(data, color=palette[0], shade=True, linewidth=2)

# Adding title and labels
plt.title('Kernel Density Estimation with Seaborn')
plt.xlabel('Value')
plt.ylabel('Density')

# Display the plot
plt.tight_layout()
plt.show()

# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generating dataset
np.random.seed(42)
data = np.random.randn(1000)

# Using Seaborn's ecdfplot function to visualize the empirical cumulative distribution
palette = sns.color_palette("viridis", n_colors=2)
sns.ecdfplot(data, color=palette[0], linewidth=2)

# Adding title and labels
plt.title('ECDF Plot with Seaborn')
plt.xlabel('Value')
plt.ylabel('Proportion of Data')

# Display the plot
plt.tight_layout()
plt.show()

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generating synthetic data
np.random.seed(42)
x = np.random.randn(150)
y = 2 * x + np.random.randn(150)

# Creating the jointplot
sns.jointplot(x=x, y=y, kind='scatter', color='m')

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset("iris")

# Create a pairplot of the iris dataset
sns.pairplot(iris, hue='species', palette='bright')

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1.1, 2.5, 2.9, 3.8, 5.1, 6.3, 6.9, 8.2, 9.1]

# Using Seaborn's regplot to plot data and regression model fit
sns.regplot(x=x, y=y, color='blue', line_kws={"color": "red"})

plt.title("Seaborn regplot")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Loading the tips dataset
tips = sns.load_dataset("tips")

# Using Seaborn's lmplot
sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex", col="time", markers=["o", "s"], palette="Set1")

plt.show()

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
data = np.random.rand(10, 10)  # A 10x10 matrix of random values between 0 and 1

# Define labels for rows and columns
rows = ['Metric ' + str(i) for i in range(1, 11)]
columns = ['Category ' + str(j) for j in range(1, 11)]

# Convert data into a DataFrame for better labeling
import pandas as pd
df = pd.DataFrame(data, index=rows, columns=columns)

# Plotting the heatmap
sns.heatmap(df, cmap='YlGnBu', annot=True)

plt.title('Metrics Across Categories')
plt.show()

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
data = np.random.rand(10, 10)  # A 10x10 matrix of random values between 0 and 1

# Define labels for rows and columns
rows = ['Metric ' + str(i) for i in range(1, 11)]
columns = ['Category ' + str(j) for j in range(1, 11)]

# Convert data into a DataFrame for better labeling
import pandas as pd
df = pd.DataFrame(data, index=rows, columns=columns)

# Plotting the clustermap
sns.clustermap(df, cmap='YlGnBu', annot=True, figsize=(10, 10))

plt.suptitle('Hierarchical Clustering of Metrics Across Categories', y=1.02)
plt.show()

