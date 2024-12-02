import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

df = pd.read_csv('processed_data.csv')

df.sort_values(['l_ipn', 'date'], inplace=True)

df['f_lag1'] = df.groupby('l_ipn')['f'].shift(1)
df['f_lag7'] = df.groupby('l_ipn')['f'].shift(7)

df_reg = df.dropna()

features_reg = ['l_ipn', 'r_asn', 'f_lag1', 'f_lag7', 'weekday', 'is_weekend', 'month']
X_reg = df_reg[features_reg]
y_reg = df_reg['f']

train_end_date = '2006-08-31'
X_train_reg = X_reg[df_reg['date'] <= train_end_date]
y_train_reg = y_reg[df_reg['date'] <= train_end_date]
X_test_reg = X_reg[df_reg['date'] > train_end_date]
y_test_reg = y_reg[df_reg['date'] > train_end_date]

rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
rf_reg.fit(X_train_reg, y_train_reg)

y_pred_reg = rf_reg.predict(X_test_reg)

mse = mean_squared_error(y_test_reg, y_pred_reg)
print("Erro Quadrático Médio (EQM): {:.2f}".format(mse))

mae = mean_absolute_error(y_test_reg, y_pred_reg)
print("Erro Absoluto Médio (EAM): {:.2f}".format(mae))

plt.figure(figsize=(10, 6))
plt.plot(y_test_reg.values, label='Valor Real', alpha=0.7)
plt.plot(y_pred_reg, label='Valor Previsto', alpha=0.7)
plt.legend()
plt.title('Comparação entre Valores Reais e Previstos')
plt.xlabel('Amostras')
plt.ylabel('Número de Fluxos')
plt.savefig('prediction_comparison.png')
plt.close()
