import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, show

# Tying out listing methods
# For loop
x = []
for n in range(1,100):
    x.append(n)

# List comprehension
y = [m for m in range(1,100)]

print(x)
print(y)

# numpy sines
sin = [np.sin(np.radians(n)) for n in range(0,360)]
print(sin)

# pandas dataframes
# from array
data = np.random.randint(-20,20,(10,5))
df = pd.DataFrame(data, index = pd.date_range('2017-01-10', periods = 10), columns = ['A','B','C','D','E'])
print(df)
# from dictionary
dict_data = {'cats': ['fred', 'maurice', 'raven', 'aaron purr'], 'rand nums': np.random.rand(4), 'nums': [1,2,5,7], 'words': ['apple', 'banana', 'chocolate', 'dust']}
df2 = pd.DataFrame(dict_data)
print(df2)
# finding info
# get list of columns
df.index
# view specific column
df['A']
# by row name
df.loc['2017-01-10']
# by row position
df.iloc['2']
# slicing
df[2:5]
# find all rows for which the following is true
df[df['D'] < 0]
