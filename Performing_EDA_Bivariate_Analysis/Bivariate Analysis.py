# Importing necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical computations
import matplotlib.pyplot as plt  # For data visualization
import seaborn as sns  # Advanced data visualization library

# Load datasets for analysis
tips = sns.load_dataset('tips')  # Load the 'tips' dataset
flights = sns.load_dataset('flights')  # Load the 'flights' dataset
iris = sns.load_dataset('iris')  # Load the 'iris' dataset
hr = pd.read_csv('HR.csv')  # Load HR dataset from local file

# Display loaded datasets (for inspection)
tips.head()  # Display the first few rows of the 'tips' dataset
flights.head()  # Display the first few rows of the 'flights' dataset
iris.head()  # Display the first few rows of the 'iris' dataset
hr.head()  # Display the first few rows of the HR dataset

# --------------------------------------------
# SCATTERPLOTS - Exploring relationships between variables
# --------------------------------------------

# Scatterplot: Relationship between employees leaving (left) and time spent in the company
sns.scatterplot(x='left', y='time_spend_company', data=hr)
plt.title('Relationship Between Attrition and Time Spent in Company')
plt.xlabel('Attrition (Left)')
plt.ylabel('Time Spent in Company')
plt.savefig('attrition_vs_time_spent.png')
plt.show()

# Scatterplot: Relationship between attrition (left) and average monthly hours
sns.scatterplot(x='left', y='average_montly_hours', data=hr)
plt.title('Attrition vs Average Monthly Hours')
plt.xlabel('Attrition (Left)')
plt.ylabel('Average Monthly Hours')
plt.savefig('attrition_vs_avg_hours.png')
plt.show()

# Scatterplot: Gender vs Tips
sns.scatterplot(x='sex', y='tip', data=tips)
plt.title('Tips Given by Gender')
plt.xlabel('Gender')
plt.ylabel('Tip Amount')
plt.savefig('gender_vs_tips.png')
plt.show()

# Scatterplot: Smoker vs Tips
sns.scatterplot(x='smoker', y='tip', data=tips)
plt.title('Tips Based on Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('Tip Amount')
plt.savefig('smoker_vs_tips.png')
plt.show()

# Scatterplot: Total bill vs Tips with Gender distinction
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex')
plt.title('Total Bill vs Tips (Categorized by Gender)')
plt.xlabel('Total Bill')
plt.ylabel('Tip Amount')
plt.legend(title='Gender')
plt.savefig('total_bill_vs_tips_gender.png')
plt.show()

# Scatterplot: Total bill vs Tips categorized by Gender and Smoking status
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex', style='smoker', size='size')
plt.title('Total Bill vs Tips (Categorized by Gender & Smoking Status)')
plt.xlabel('Total Bill')
plt.ylabel('Tip Amount')
plt.legend(title='Gender & Smoking')
plt.savefig('total_bill_vs_tips_full.png')
plt.show()

# --------------------------------------------
# BARPLOTS - Comparing categorical and numerical data
# --------------------------------------------

# Barplot: Gender vs Tips categorized by Smoking status
sns.barplot(x='sex', y='tip', data=tips, hue='smoker')
plt.title('Tips by Gender and Smoking Status')
plt.xlabel('Gender')
plt.ylabel('Tip Amount')
plt.legend(title='Smoking Status')
plt.savefig('gender_smoking_tips.png')
plt.show()

# Barplot: Day vs Total bill categorized by Gender
sns.barplot(x='day', y='total_bill', data=tips, hue='sex')
plt.title('Total Bill by Day (Categorized by Gender)')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.legend(title='Gender')
plt.savefig('day_vs_total_bill_gender.png')
plt.show()

# Barplot: Salary vs Satisfaction Level categorized by promotion in the last 5 years
sns.barplot(x='salary', y='satisfaction_level', data=hr, hue='promotion_last_5years')
plt.title('Satisfaction Level by Salary and Promotions')
plt.xlabel('Salary')
plt.ylabel('Satisfaction Level')
plt.legend(title='Promotions (Last 5 Years)')
plt.savefig('salary_vs_satisfaction_promotions.png')
plt.show()

# --------------------------------------------
# BOXPLOTS - Distribution of data across categories
# --------------------------------------------

# Boxplot: Total bill vs Day categorized by Gender
sns.boxplot(x='day', y='total_bill', data=tips, hue='sex')
plt.title('Distribution of Total Bill by Day and Gender')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.legend(title='Gender')
plt.savefig('total_bill_distribution_by_day.png')
plt.show()

# Boxplot: Satisfaction Level vs Salary categorized by Work Accident
sns.boxplot(x='salary', y='satisfaction_level', data=hr, hue='Work_accident')
plt.title('Satisfaction Level by Salary and Work Accident')
plt.xlabel('Salary')
plt.ylabel('Satisfaction Level')
plt.legend(title='Work Accident')
plt.savefig('satisfaction_salary_work_accident.png')
plt.show()

# --------------------------------------------
# DISTRIBUTION PLOTS - Distribution of numerical data
# --------------------------------------------

# Distribution of total bill by Gender
sns.displot(tips[tips['sex'] == 'Male']['total_bill'], label='Male', kde=True)
sns.displot(tips[tips['sex'] == 'Female']['total_bill'], label='Female', kde=True)
plt.title('Distribution of Total Bills by Gender')
plt.xlabel('Total Bill')
plt.legend(title='Gender')
plt.savefig('gender_total_bill_distribution.png')
plt.show()

# --------------------------------------------
# HEATMAPS - Visualizing categorical relationships
# --------------------------------------------

# Heatmap: Cross-tabulation of Day and Gender
var = pd.crosstab(tips['day'], tips['sex'])
sns.heatmap(var, annot=True, cmap='coolwarm')
plt.title('Frequency of Gender by Day')
plt.savefig('day_gender_heatmap.png')
plt.show()

# --------------------------------------------
# PAIRPLOTS - Pairwise relationships between variables
# --------------------------------------------

# Pairplot of the Iris dataset
sns.pairplot(iris, hue='species', diag_kind='kde')
plt.title('Pairwise Relationships in Iris Dataset')
plt.savefig('iris_pairplot.png')
plt.show()

# --------------------------------------------
# LINE PLOTS - Trends in numerical data
# --------------------------------------------

# Lineplot: Sepal length vs Sepal width categorized by species
sns.lineplot(x='sepal_length', y='sepal_width', hue='species', data=iris)
plt.title('Sepal Length vs Sepal Width (Categorized by Species)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend(title='Species')
plt.savefig('sepal_length_vs_width.png')
plt.show()

