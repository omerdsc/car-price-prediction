import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Veri setini yükle
car_price = pd.read_csv("C:\\Users\\omer_\\OneDrive\\Desktop\\zulıip web\\car_prices.csv")


# Ön işleme (gönderdiğin gibi)
car_price['make'] = car_price['make'].fillna('Other')
car_price['model'] = car_price['model'].fillna('Other')
car_price['trim'] = car_price['trim'].fillna('Other')
car_price['color'] = car_price['color'].fillna('Other')
car_price['body'] = car_price['body'].fillna(car_price['body'].mode()[0])
car_price['transmission'] = car_price['transmission'].fillna(car_price['transmission'].mode()[0])
car_price['interior'] = car_price['interior'].fillna(car_price['interior'].mode()[0])
car_price["condition"] = car_price["condition"].fillna(car_price["condition"].mean())
car_price["odometer"] = car_price["odometer"].fillna(car_price["odometer"].mean())
car_price["mmr"] = car_price["mmr"].fillna(car_price["mmr"].mean())
car_price.dropna(subset=['vin', 'saledate'], inplace=True)

# Bağımlı ve bağımsız değişkenler
df_new = car_price[["year", "make", "model", "body", "transmission", "odometer", "color", "interior", "sellingprice"]]
Y = df_new["sellingprice"]
X = df_new.drop("sellingprice", axis=1)

categorical_cols = ["make", "model", "body", "transmission", "color", "interior"]
numeric_cols = ["year", "odometer"]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
], remainder='passthrough')

model = Pipeline([
    ("preprocess", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=10, max_depth=10, random_state=42))
])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)
print("R2 Skoru:", r2_score(Y_test, Y_pred))
print("RMSE:", mean_squared_error(Y_test, Y_pred, squared=False))

joblib.dump(model, "arac_fiyat_modeli.pkl")
