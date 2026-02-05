import pandas as pd

df = pd.read_csv('Bank_Churn.csv')

# Group by Geography and calculate mean for relevant behavior columns
behavior_cols = ['Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'Exited']
geo_behavior = df.groupby('Geography')[behavior_cols].mean()

# Add count to see sample size
geo_behavior['CustomerCount'] = df.groupby('Geography').size()

print("Account Behavior by Geography (Mean values):")
print(geo_behavior)

# Median Balance (since it often has many zeros or is skewed)
print("\nMedian Balance by Geography:")
print(df.groupby('Geography')['Balance'].median())

# Percentage of customers with zero balance
zero_balance = df[df['Balance'] == 0].groupby('Geography').size() / df.groupby('Geography').size() * 100
print("\nPercentage of customers with Zero Balance:")
print(zero_balance)
