from ml.data_processing.encoding import encoding
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
df=encoding()

X= df.drop(columns="Salary Estimate")
y=df["Salary Estimate"]

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True)

model=RandomForestRegressor(max_depth=20)

model.fit(X_train,y_train)

y_predict= model.predict(X_test)



