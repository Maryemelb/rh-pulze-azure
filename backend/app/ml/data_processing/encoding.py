import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
def encoding():
    
    # 1. OneHoteEncoding and OrdinalEncoding and FrequencyEncoding

    categorial_columns= ['Company Name','Location','Headquarters', 'Size', 'Type of ownership', 'Industry', 'Sector']
    hot_encode_coumns= ["Type of ownership"]
    ordinal_encode_columns=["Size"]
    frequency_encode_columns= ["Sector","Company Name","Headquarters","Location","Industry"]
    hot_encode= OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    ordinal_encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
    for col in categorial_columns:
            if col in hot_encode_coumns:
                hot_transformed= hot_encode.fit_transform(df[[col]])
                hot_transformed_df= pd.DataFrame(
                    hot_transformed,
                    columns= hot_encode.get_feature_names_out([col]),
                    index= df.index
                )
                df = pd.concat([df.drop(columns=[col]), hot_transformed_df], axis=1)
            elif col in ordinal_encode_columns:
                ordinal_transformed= ordinal_encoder.fit_transform(df[[col]])
                df[col]= ordinal_transformed
            elif col in frequency_encode_columns:
                # FREQUENCY ENCODING
                freq= df[col].value_counts()
                df[col]=df[col].map(freq)
                df[col].head()

