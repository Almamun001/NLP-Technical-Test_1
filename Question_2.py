#Implement a null value handling code by using cumulative  forward and backward mean fill in pandas

import pandas as pd
import numpy as np

# Creating a DataFrame with np.nan values
data = {
    "Serial": [1, np.nan, 3, np.nan, 5],
    "Price": [10, 20, np.nan, np.nan, 50],
    "Stock": [np.nan, 100, np.nan, 200, 300]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Forward fill using cumulative mean
df_forward = df.fillna(df.expanding().mean())
print("\nDataFrame after forward fill using cumulative mean:")
print(df_forward)
# Backward fill using cumulative mean
df_backward = df[::-1].fillna(df[::-1].expanding().mean())[::-1]
print("\nDataFrame after backward fill using cumulative mean:")
print(df_backward)