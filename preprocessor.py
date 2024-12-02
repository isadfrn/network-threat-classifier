import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('data.csv')

df['date'] = pd.to_datetime(df['date'])

compromised_ips = {
    1: ('2006-08-14', '2006-09-30'),
    5: ('2006-08-25', '2006-09-30'),
    4: ('2006-09-08', '2006-09-30'),
    3: ('2006-09-16', '2006-09-30'),
    6: ('2006-09-16', '2006-09-30')
}
def is_compromised(row):
    ip = row['l_ipn']
    date = row['date']
    if ip in compromised_ips:
        start_date, end_date = compromised_ips[ip]
        if pd.to_datetime(start_date) <= date <= pd.to_datetime(end_date):
            return 1
    return 0

df['compromised'] = df.apply(is_compromised, axis=1)

df['weekday'] = df['date'].dt.weekday
df['month'] = df['date'].dt.month
df['is_weekend'] = df['weekday'].apply(lambda x: 1 if x >= 5 else 0)

scaler = StandardScaler()
df[['f', 'r_asn']] = scaler.fit_transform(df[['f', 'r_asn']])

df.to_csv('processed_data.csv', index=False)
