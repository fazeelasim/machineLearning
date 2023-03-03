import matplotlib.pyplot as pl
import numpy as np
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn import metrics

# data = pandas.read_csv ("data.csv")
# x=data[["Weight","Volume"]]
# sc = StandardScaler()
# sx = sc.fit_transform(x)
# y=data["CO2"]
# # print(x)
# # print(sx)


# model = linear_model.LinearRegression()
# model.fit(sx,y)
# output1=model.predict([[55,178]])
# print(output1)

# np.random.seed(2)
# x = np.random.normal(3,1,100)
# y = np.random.normal(150,40,100)/x

# pl.scatter(x,y)


# trainx= x [:80]
# trainy= y [:80]
# testx = x [80:]
# testy = y [80:]

# # pl.scatter(trainx,trainy)
# # pl.scatter(testx,testy)
# # pl.show()

# model = np.poly1d(np.polyfit(trainx,trainy,3))
# ouptutscore =r2_score(testy,model(testx))
# line = np.linspace(0,6,100)
# pl.scatter (trainx,trainy)
# pl.plot(line,model(line))
# pl.show()

# print(ouptutscore)

model = linear_model.LogisticRegression()
x=np.array([7.3,6.4,3.8,8.8,9.4,6.3,7.4]).reshape(-1,1)
y=np.array([1,1,0,1,0,1,1])

model.fit(x,y)
output = model.predict(np.array([3.4]).reshape(-1,1))
print(output)

y=np.array([1,1,0,1,0,1,1])
y2=np.array([0,1,1,1,1,0,1])

cmat =metrics.confusion_matrix(y,y2)
cmdis =metrics.ConfusionMatrixDisplay(confusion_matrix = cmat, display_labels =[False,True] )
cmdis.plot()
pl.show()
# print(cmat)

# precs =metrics.precision_score(y,y2)
# print(precs)

# precs =metrics.recall_score(y,y2)
# print(precs)

precs =metrics.f1_score(y,y2)
print(precs)