
import pandas as pd

data = {
    'Name': ['Amit', 'Sneha', 'Rahul', 'Priya', 'Neha',
             'Rohan', 'Pooja', 'Karan', 'Anjali', 'Vijay'],
    'Marks': [80, 90, 75, 85, 95, 70, 88, 65, 92, 78]
}

df = pd.DataFrame(data)

print(df.tail())
