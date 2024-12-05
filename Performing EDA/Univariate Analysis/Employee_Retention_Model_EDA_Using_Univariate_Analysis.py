# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


df=pd.read_csv('HR.csv')
df.sample(10)
# -

# Applying Univariate Analysis and Trying to identify their correlation 

# ..........................................................................

df.shape

# +
# plotting countplot on the left column

sns.countplot(x=df['left'],data=df)
plt.xlabel('Left')
plt.ylabel('Number of Employees')
plt.show()

# +
#countPLot  on the department column 

sns.countplot(x=df['Department'])
plt.xticks(rotation=90)
plt.show()

value=df['Department'].value_counts()
value
# value.sum(numeric_only=True)

# +
#countplot for salary dataset 

sns.countplot(x=df['salary'])
plt.show()

df['salary'].value_counts()


# +
# hisghest count of those employess who left the company 

left=df[df['left']==1]
sns.countplot(x=left['Department'])
plt.ylabel('Emplooyes who left the company')
plt.xticks(rotation=90)
plt.show()
left['Department'].value_counts()

# +
# maximum number of exmplooyes from department who still works in the company 


no_left=df[df['left']==0]
sns.countplot(x=no_left['Department'])
plt.ylabel('Employees who still works in the company')
plt.xticks(rotation=90)
plt.show()
no_left['Department'].value_counts()
# -

df['left'].value_counts()

df.corr(numeric_only=True)

sns.countplot(x=df['number_project'])
plt.xticks(rotation=0)
plt.show()
df['number_project'].value_counts()


# +
# Porject number of people who left the company

sns.countplot(x=left['number_project'])
plt.xticks(rotation=0)
plt.show()
left['number_project'].value_counts()


# +


# Porject number of people who still works in  the company

sns.countplot(x=no_left['number_project'])
plt.ylabel('People who still works in  company')
plt.xticks(rotation=0)
plt.show()
no_left['number_project'].value_counts()
# -

df[df['number_project']==7]

# +

sns.countplot(x=df['promotion_last_5years'])

plt.show()

df['promotion_last_5years'].value_counts()


# +
# Promoted people who still works in  the company

sns.countplot(x=no_left['promotion_last_5years'])

plt.ylabel('People who still works in  company')
plt.xticks(rotation=0)
plt.show()
no_left['promotion_last_5years'].value_counts()

# +
# Promoted people who left the company

sns.countplot(x=left['promotion_last_5years'])
plt.xticks(rotation=0)
plt.show()
left['promotion_last_5years'].value_counts()

# +

sns.countplot(x=df['time_spend_company'])
plt.xticks(rotation=0)
plt.show()
df['time_spend_company'].value_counts()


# +
# Time spent people who left the company

sns.countplot(x=left['time_spend_company'])
plt.xticks(rotation=0)
plt.ylabel('People who left company')
plt.show()
left['time_spend_company'].value_counts()

# +
# Time spent people who still the company

sns.countplot(x=no_left['time_spend_company'])
plt.xticks(rotation=0)
plt.ylabel('People who still works in  company')
plt.show()
no_left['time_spend_company'].value_counts()
# -

# Total People who had work acciedent
sns.countplot(x=df['Work_accident'])
plt.xticks(rotation=0)
plt.show()
df['Work_accident'].value_counts()

# +
# Work accident of people who left the company

sns.countplot(x=left['Work_accident'])
plt.xticks(rotation=0)
plt.ylabel('People who left company')
plt.show()
left['Work_accident'].value_counts()

# +
# Work accident of people who still works in the company

sns.countplot(x=no_left['Work_accident'])
plt.xticks(rotation=0)
plt.ylabel('People who left company')
plt.show()
no_left['Work_accident'].value_counts()

# +
#Plotting pie chart of left Column

lv=df['left'].value_counts()
dg=lv.plot(kind='pie',autopct='%0.3f',explode=[0.0,0.1])
plt.title('Left company')
plt.legend()
plt.show()

# +
import matplotlib.pyplot as plt

# Work Accident for Employees Who Left the Company
work_accident_left = left['Work_accident'].value_counts()
work_accident_left.plot(kind='pie', autopct='%0.1f%%', explode=[0.1, 0.0], colors=['lightcoral', 'lightskyblue'], labels=['No Accident', 'Accident'])
plt.title('Work Accidents (Left the Company)')
plt.ylabel('')
plt.savefig('work_accidents_left.png')  # Save the figure
plt.show()

# Work Accident for Employees Who Still Work
work_accident_no_left = no_left['Work_accident'].value_counts()
work_accident_no_left.plot(kind='pie', autopct='%0.1f%%', explode=[0.1, 0.0], colors=['lightgreen', 'gold'], labels=['No Accident', 'Accident'])
plt.title('Work Accidents (Still Working)')
plt.ylabel('')
plt.savefig('work_accidents_still_working.png')  # Save the figure
plt.show()

# Time Spent in Company for All Employees
time_spent_all = df['time_spend_company'].value_counts()
time_spent_all.plot(kind='pie', autopct='%0.1f%%', startangle=140, colormap='viridis')
plt.title('Time Spent at Company (All Employees)')
plt.ylabel('')
plt.savefig('time_spent_all.png')  # Save the figure
plt.show()

# Time Spent in Company for Employees Who Left
time_spent_left = left['time_spend_company'].value_counts()
time_spent_left.plot(kind='pie', autopct='%0.1f%%', startangle=140, colors=['coral', 'cyan', 'magenta'])
plt.title('Time Spent (Left Company)')
plt.ylabel('')
plt.savefig('time_spent_left.png')  # Save the figure
plt.show()

# Time Spent in Company for Employees Still Working
time_spent_no_left = no_left['time_spend_company'].value_counts()
time_spent_no_left.plot(kind='pie', autopct='%0.1f%%', startangle=140, colors=['lime', 'gold', 'blue'])
plt.title('Time Spent (Still Working)')
plt.ylabel('')
plt.savefig('time_spent_still_working.png')  # Save the figure
plt.show()

# Promotions in the Last 5 Years for Employees Who Left
promotion_left = left['promotion_last_5years'].value_counts()
promotion_left.plot(kind='pie', autopct='%0.1f%%', explode=[0.1, 0.0], colors=['pink', 'yellow'], labels=['No Promotion', 'Promotion'])
plt.title('Promotions (Left the Company)')
plt.ylabel('')
plt.savefig('promotions_left.png')  # Save the figure
plt.show()

# Promotions in the Last 5 Years for Employees Still Working
promotion_no_left = no_left['promotion_last_5years'].value_counts()
promotion_no_left.plot(kind='pie', autopct='%0.1f%%', explode=[0.1, 0.0], colors=['purple', 'green'], labels=['No Promotion', 'Promotion'])
plt.title('Promotions (Still Working)')
plt.ylabel('')
plt.savefig('promotions_still_working.png')  # Save the figure
plt.show()

# Departments for All Employees
departments = df['Department'].value_counts()
departments.plot(kind='pie', autopct='%0.1f%%', startangle=90, colormap='Pastel1')
plt.title('Departments (All Employees)')
plt.ylabel('')
plt.savefig('departments_all.png')  # Save the figure
plt.show()

# Departments for Employees Who Left
departments_left = left['Department'].value_counts()
departments_left.plot(kind='pie', autopct='%0.1f%%', startangle=90, colormap='tab10')
plt.title('Departments (Left the Company)')
plt.ylabel('')
plt.savefig('departments_left.png')  # Save the figure
plt.show()

# Departments for Employees Still Working
departments_no_left = no_left['Department'].value_counts()
departments_no_left.plot(kind='pie', autopct='%0.1f%%', startangle=90, colormap='Accent')
plt.title('Departments (Still Working)')
plt.ylabel('')
plt.savefig('departments_still_working.png')  # Save the figure
plt.show()

# Salary Levels for All Employees
salary_all = df['salary'].value_counts()
salary_all.plot(kind='pie', autopct='%0.1f%%', startangle=140)
plt.title('Salary Levels (All Employees)')
plt.ylabel('')
plt.savefig('salary_levels_all.png')  # Save the figure
plt.show()

# -

# Plotting For Numerical Values
#

df.sample(10)


# +
#Plotting Histogram on the satisfaction level column

plt.hist(df['satisfaction_level'],bins=35)
plt.savefig('satisfaction_level_histogram.png')
plt.show()


# +
#sATISFACTION LEVEL OF THOSE WHO LEFT COMPANY

plt.hist(left['satisfaction_level'],bins=35)
plt.savefig('satisfaction_level_left_histogram.png')
plt.show()


# +
#sATISFACTION LEVEL OF THOSE WHO still works  COMPANY

plt.hist(no_left['satisfaction_level'],bins=35)
plt.savefig('satisfaction_level_still_work_histogram.png')
plt.show()


# +
import matplotlib.pyplot as plt

# Histogram of Work Accident for Employees Who Left the Company
plt.hist(left['Work_accident'], bins=5, color='skyblue', edgecolor='black')
plt.title('Work Accident (Left the Company)')
plt.xlabel('Work Accident')
plt.ylabel('Frequency')
plt.savefig('work_accident_left_histogram.png')
plt.show()

# Histogram of Work Accident for Employees Who Still Work
plt.hist(no_left['Work_accident'], bins=5, color='green', edgecolor='black')
plt.title('Work Accident (Still Working)')
plt.xlabel('Work Accident')
plt.ylabel('Frequency')
plt.savefig('work_accident_no_left_histogram.png')
plt.show()

# Histogram of Time Spent in the Company for All Employees
plt.hist(df['time_spend_company'], bins=10, color='purple', edgecolor='black')
plt.title('Time Spent at Company (All Employees)')
plt.xlabel('Time Spent (Years)')
plt.ylabel('Frequency')
plt.savefig('time_spent_all_histogram.png')
plt.show()

# Histogram of Time Spent in the Company for Employees Who Left
plt.hist(left['time_spend_company'], bins=10, color='red', edgecolor='black')
plt.title('Time Spent at Company (Left the Company)')
plt.xlabel('Time Spent (Years)')
plt.ylabel('Frequency')
plt.savefig('time_spent_left_histogram.png')
plt.show()

# Histogram of Time Spent in the Company for Employees Still Working
plt.hist(no_left['time_spend_company'], bins=10, color='blue', edgecolor='black')
plt.title('Time Spent at Company (Still Working)')
plt.xlabel('Time Spent (Years)')
plt.ylabel('Frequency')
plt.savefig('time_spent_no_left_histogram.png')
plt.show()

# Histogram of Promotions in the Last 5 Years for Employees Who Left
plt.hist(left['promotion_last_5years'], bins=5, color='orange', edgecolor='black')
plt.title('Promotions in Last 5 Years (Left the Company)')
plt.xlabel('Promotion Status')
plt.ylabel('Frequency')
plt.savefig('promotion_left_histogram.png')
plt.show()

# Histogram of Promotions in the Last 5 Years for Employees Still Working
plt.hist(no_left['promotion_last_5years'], bins=5, color='magenta', edgecolor='black')
plt.title('Promotions in Last 5 Years (Still Working)')
plt.xlabel('Promotion Status')
plt.ylabel('Frequency')
plt.savefig('promotion_no_left_histogram.png')
plt.show()

# Histogram of Departments for All Employees
plt.hist(df['Department'], bins=len(df['Department'].unique()), color='cyan', edgecolor='black')
plt.title('Departments (All Employees)')
plt.xlabel('Departments')
plt.ylabel('Frequency')
plt.savefig('departments_all_histogram.png')
plt.show()

# Histogram of Salary Levels for All Employees
plt.hist(df['salary'], bins=len(df['salary'].unique()), color='brown', edgecolor='black')
plt.title('Salary Levels (All Employees)')
plt.xlabel('Salary Levels')
plt.ylabel('Frequency')
plt.savefig('salary_all_histogram.png')
plt.show()


# +
#Plotting Displot

sns.distplot(df['satisfaction_level'])
plt.savefig('satisfaction_level_distplot_.png')
plt.show()



