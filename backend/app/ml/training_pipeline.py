import sys
from pathlib import Path
import joblib

sys.path.append(str(Path(__file__).resolve().parents[3]))

from backend.app.ml.data_processing.encoding import encoding
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
df=encoding()

X= df.drop(columns=["Salary Estimate", "Job Description", "Job Title","job_role"])
y=df["Salary Estimate"]

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True)

model=RandomForestRegressor(max_depth=20, verbose=2)

model.fit(X_train,y_train)

y_predict= model.predict(X_test)

mae= mean_absolute_error(y_test, y_predict)
r2= r2_score(y_test, y_predict)
print(mae)
print(r2)

joblib.dump(model, 'backend/app/saved_model/rf_model.pkl')

