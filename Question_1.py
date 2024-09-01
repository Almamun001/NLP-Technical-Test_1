import pandas as pd
import numpy as np

data = {
    "fruits": ["Apple", np.nan, "Mango", np.nan, "Banana"],
    "vegetables": ["Carrot", "Cucumber", np.nan, np.nan, "Potato"],
    "animals": [np.nan, "Dog", np.nan, "Cat", "Lion"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# it will fill the previous value into the null value
df_ffill = df.ffill()
print("\nDataFrame after forward fill (ffill):")
print(df_ffill)

# it will fill the next value into the null
df_bfill = df.bfill()
print("\nDataFrame after backward fill (bfill):")
print(df_bfill)
