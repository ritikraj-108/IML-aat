import pandas as pd
from sklearn import linear_model

# Read training data into a Pandas DataFrame
data = pd.read_csv('trainingdata.txt', names=['charging_time', 'battery_life'])
df = pd.DataFrame(data)

# Remove 'noise' from the data
df_cleaned = df[df['battery_life'] < 8.00]

# Read charging time (independent variable) and battery life (dependent variable)
X = df_cleaned[['charging_time']]
y = df_cleaned['battery_life']

# Read charging time for prediction
timeCharged = float(input().strip())

# Check if the charging time is more than 4 hours
if timeCharged > 3.99:
    print("8.00")
else:
    # Initialize and fit the linear regression model
    reg = linear_model.LinearRegression()
    reg.fit(X, y)
    
    # Predict the battery life for the input charging time
    prediction = reg.predict([[timeCharged]])
    
    # Print the prediction rounded to 2 decimal places
    print(f"{prediction[0]:.2f}")
