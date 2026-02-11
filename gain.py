import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv("homeprice.csv")
df

%matplotlib inline
plt.xlabel('year')
plt.ylabel('price(US$)')
plt.scatter(df.area,df.price,color='red',marker='+')

reg=linear_model.LinearRegression()
reg.fit(df[['year']],df.price)

reg.predict(3300)

reg.coeff

reg.intercept

y=m*x+b
print(y)
