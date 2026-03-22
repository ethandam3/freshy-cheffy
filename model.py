import numpy as np
import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
import pickle

data = {
    'item':   ['apple','banana','spinach','carrot','zucchini','tomato',
                'apple','banana','spinach','carrot','zucchini','tomato',
                'apple','banana','spinach','carrot','zucchini','tomato',
                'apple','banana','spinach','carrot','zucchini','tomato'],
    'season': [1,1,1,1,1,1, 2,2,2,2,2,2, 3,3,3,3,3,3, 1,1,1,1,1,1],
    'is_ugly':[0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 1,1,1,1,1,1],
    'price':  [1.50,0.35,2.00,0.80,1.20,1.80,
               1.80,0.40,2.50,1.00,1.50,2.20,
               1.60,0.38,2.20,0.90,1.35,2.00,
               0.90,0.25,1.20,0.50,0.75,1.10]
}

df = pd.DataFrame(data)
df = pd.get_dummies(df, columns=['item'])

X = df.drop('price', axis=1).values
y = df['price'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = SGDRegressor(loss='squared_error', learning_rate='constant',
                     eta0=0.01, max_iter=2000, random_state=42)
model.fit(X_scaled, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open('columns.pkl', 'wb') as f:
    pickle.dump(df.drop('price', axis=1).columns.tolist(), f)

print("Model trained!")
print(f"R²: {model.score(X_scaled, y):.3f}")