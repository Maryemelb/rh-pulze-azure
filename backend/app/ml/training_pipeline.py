import sys
from pathlib import Path
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
sys.path.append(str(Path(__file__).resolve().parents[3]))
from sklearn.preprocessing import FunctionTransformer
from backend.app.ml.data_processing.processing import processing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from backend.app.ml.data_processing.embedding import generate_embeddings

df=processing()

X= df.drop(columns=["Salary Estimate", "Job Description", "Job Title","job_role"], errors='ignore')
df.drop(columns=["Job Title", "index", "Rating"], inplace=True, errors='ignore')

y=df["Salary Estimate"]

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True)

def frequency_encoding(X):
    X = X.copy()
    for col in X.columns:
        freq = X[col].value_counts()
        X[col] = X[col].map(freq)
    return X

frequency_transformer = FunctionTransformer(frequency_encoding)
text_transformer= FunctionTransformer(generate_embeddings)

# model=RandomForestRegressor(max_depth=20, verbose=2)

# model.fit(X_train,y_train)

# y_predict= model.predict(X_test)

# mae= mean_absolute_error(y_test, y_predict)
# r2= r2_score(y_test, y_predict)
# print(mae)
# print(r2)

# joblib.dump(model, 'backend/app/saved_model/rf_model.pkl')

# model= joblib.load('backend/app/saved_model/rf_model.pkl')

# df.head()
categorial_columns= ['Company Name','Location','Competitors', 'Headquarters', 'Size', 'Type of ownership', 'Industry', 'Sector']

hot_encode_columns= ["Type of ownership"]
ordinal_encode_columns=["Size"]
frequency_encode_columns= ["Sector","Company Name","Headquarters","Location","Competitors","Industry"]
embedding_columns=["description"]
preprocessor = ColumnTransformer(
    transformers=[
        ('hot', OneHotEncoder(handle_unknown='ignore'), hot_encode_columns),
        ('ordinal', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1), ordinal_encode_columns),
        ('frequency', frequency_transformer, frequency_encode_columns), # fix here
        ('frequency', text_transformer, embedding_columns)  # fix here

    ],
    remainder='passthrough'
)

# Full pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor(max_depth=20, random_state=42))
])

# Train once
pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MAE: {mae}")
print(f"R2: {r2}")

# Save pipeline for future use
joblib.dump(pipeline, "backend/app/saved_model/rf_model.pkl")