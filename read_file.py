
import matplotlib.pyplot as m
from pandas import read_csv

data=read_csv("raw_data.csv")
print(data)
x=data["name"]
y=data["percent"]
m.plot(x,y)
m.show()
