import pandas as pd
data = pd.read_csv("C:/Users/Shridhar Ingale/yob1880.csv")
data.head()
print(data)

from sdv.tabular import GaussianCopula
model = GaussianCopula()
model.fit(data)

sample = model.sample(200)
sample.head()
print(sample)