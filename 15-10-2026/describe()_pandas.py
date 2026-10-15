
import pandas as pd

data = {
    'Marks': [80, 90, 75, 85, 95, 70, 88, 65, 92, 78]
}

df = pd.DataFrame(data)

print(df.describe())
