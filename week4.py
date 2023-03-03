import matplotlib.pyplot as pl
import numpy as np
# 
# x1 = np.array([5,7,8,5])
# y1 = np.array([7,9,5,3])
# #pl.plot (x ,y)
# #pl.plot (x ,y,'*')
# #pl.plot (x, linestyle ='dotted' )
# pl.subplot(1,2,1)
# pl.plot (x,y, linestyle ='dashed' , color ='r', linewidth = '4' )
# pl.xlabel('X axis')
# pl.ylabel('Y axis')
# pl.title('graph')
# pl.grid(axis ='x')
# pl.subplot(1,2,2)
# pl.plot (x1,y1, linestyle ='dashed' , color ='b', linewidth = '2' )
# pl.xlabel('X axis')
# pl.ylabel('Y axis')
# pl.title('graph')
# pl.grid(axis ='x')
# pl.suptitle('graphs')
# size=np.array([2,6,25,38])
# pl.scatter(x,y)
# pl.scatter(x1,y1, color = 'r', s= size, alpha=0.5)
# pl.show()
# x = np.array(["X" ,"Y", "Z"])
# y = np.array([2,8,4])
# # pl.bar(x,y)
# pl.barh(x,y)
# pl.show()
# x=np.random.normal(170,10,250)
# print(x)
# pl.hist(x)
# pl.show()
# x=np.array([30,30,40])
# labs = ["a","b","c"]
# pl.pie(x,labels=labs)
# pl.show()
# x=np.random.uniform(0.0 , 5.0 ,200)
# pl.hist(x)
# pl.show()

# from scipy import stats
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# slope,intercept,r,p,std = stats.linregress(x,y)

# def func(x):
#     return slope*x+intercept

# model= list(map(func,x))
# pl.scatter(x,y)
# pl.plot(x,model)
# pl.show()

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# model = np.poly1d(np.polyfit(x,y,3))
# line = np.linspace(1,22,100)
# pl.scatter (x,y)
# pl.plot(line,model(line))
# pl.show()



import pandas
from sklearn import linear_model
data = pandas.read_csv ("data.csv")
x=data[["Weight","Volume"]]
y=data["CO2"]

model = linear_model.LinearRegression()
model.fit(x,y)
output1=model.predict([[55,178]])
print(output1)




