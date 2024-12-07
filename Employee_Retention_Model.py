# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np   # For numerical operations
import matplotlib.pyplot as plt  # For visualization
import seaborn as sns  # For advanced visualization

# Load the dataset (assuming 'HR.csv' contains employee data)
df = pd.read_csv('HR.csv')  # Read the dataset into a DataFrame
df  # Display the dataset (you can remove this in a script)

# Display the column names of the dataset
df.columns  # This helps identify the available features in the dataset

# Import train_test_split for splitting the data into training and testing sets
from sklearn.model_selection import train_test_split

# Select the feature columns (X) and the target column (y)
# Here, we select all columns except for the 'left' column, which is the target
X = df.iloc[:, [0, 1, 2, 3, 4, 5, 7, 8, 9]]  # Selecting specific columns based on index
y = df['left']  # 'left' column is the target variable (whether the employee left or not)

# Split the data into training and test sets (80% training, 20% testing)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Display training and testing feature sets (can be removed in a script)
x_train
x_test

# Initialize the Logistic Regression model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# One-hot encode categorical variables (such as 'Department' and 'salary')
# Convert categorical variables into dummy/indicator variables (0 or 1 for each category)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# List of categorical columns
categorical_columns = ['Department', 'salary']

# Perform one-hot encoding on categorical columns
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

# After one-hot encoding, separate features and the target variable again
X = df.drop('left', axis=1)  # Features: Drop the target column 'left'
y = df['left']  # Target variable: 'left' column (whether the employee left)

# Split the data into training and testing sets again (since the DataFrame has been modified)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check the data types of the features to ensure they are all numeric after encoding
print(x_train.dtypes)  # Should all be numeric after one-hot encoding

# Initialize and fit the logistic regression model on the training data
model = LogisticRegression()
model.fit(x_train, y_train)

# Use the trained model to make predictions on the test set
predictions = model.predict(x_test)  # Predict on the test data

# Print the predicted labels (0 or 1, corresponding to whether employees left or stayed)
print(predictions)

# Display the test and training data sets (optional)
x_test
x_train

# Evaluate the model performance by calculating the accuracy score on the test data
model.score(x_test, y_test)  # Returns the accuracy of the model on the test set

# Make predictions on the test set and display the predicted values
y_pred = model.predict(x_test)
y_pred  # Predicted values

# Display the true test labels (y_test) for comparison with predictions
y_test
