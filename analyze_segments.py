import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('Bank_Churn.csv')

# 1. Age Segmentation
def age_segment(age):
    if age < 30: return 'Young (<30)'
    elif age < 50: return 'Middle-Aged (30-50)'
    else: return 'Senior (50+)'

df['AgeSegment'] = df['Age'].apply(age_segment)

# 2. Balance Segmentation
def balance_segment(balance):
    if balance == 0: return 'Zero Balance'
    elif balance < 100000: return 'Low-to-Mid Balance (<100k)'
    else: return 'High Balance (100k+)'

df['BalanceSegment'] = df['Balance'].apply(balance_segment)

# 3. Product Usage Segmentation
df['ProductUsage'] = df['NumOfProducts'].apply(lambda x: 'Low (1)' if x == 1 else 'High (2+)')

# Grouping and Analysis
segments = {
    'Age Segments': df.groupby('AgeSegment').agg({'Exited': 'mean', 'Balance': 'mean', 'CustomerId': 'count'}),
    'Balance Segments': df.groupby('BalanceSegment').agg({'Exited': 'mean', 'IsActiveMember': 'mean', 'CustomerId': 'count'}),
    'Geography Segments': df.groupby('Geography').agg({'Exited': 'mean', 'Balance': 'mean', 'CustomerId': 'count'}),
    'Product Usage Segments': df.groupby('ProductUsage').agg({'Exited': 'mean', 'IsActiveMember': 'mean', 'CustomerId': 'count'})
}

for name, data in segments.items():
    print(f"\n--- {name} ---")
    data['Share (%)'] = (data['CustomerId'] / len(df)) * 100
    print(data.rename(columns={'Exited': 'Churn Rate', 'CustomerId': 'Count'}))

# Identifying a "High-Risk" Segment
high_risk = df[(df['Age'] >= 50) & (df['Geography'] == 'Germany')]
print(f"\nHigh-Risk Segment (Seniors in Germany):")
print(f"Count: {len(high_risk)}")
print(f"Churn Rate: {high_risk['Exited'].mean():.2%}")
