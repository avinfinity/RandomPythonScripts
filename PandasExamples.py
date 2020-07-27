import pandas as pd

data = [['Alex',10],['Bob',12], ['Clarke', 15]]
df = pd.DataFrame(data, columns=['Name','Age'])

print(df)

data = [{'a':1,'b':2},{'a':1,'b':2,'c':3}]
df = pd.DataFrame(data)
print(df)