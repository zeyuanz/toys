from sklearn.preprocessing import  KBinsDiscretizer, OrdinalEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd

data = {
    'a': ['a', 1, 2,3, 4],
    'b': ['c', 2, 2,3, 4],
    'c': [1, -1, 5,2, 1],
    'd': [0.5, 2, 2,6, 2],
}

df = pd.DataFrame(data)
df[['a', 'b']] = df[['a', 'b']].astype(str)
ct = ColumnTransformer([
    ("label", OrdinalEncoder(), [0,1]),
    ("Kbins", KBinsDiscretizer(n_bins=2, encode="ordinal"), [2,3]),
    ("Kbins2", KBinsDiscretizer(n_bins=3, encode="ordinal"), [2,3]),
], remainder='passthrough')

transform_df = ct.fit_transform(df)
print(transform_df)