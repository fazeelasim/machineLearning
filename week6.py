import matplotlib.pyplot as pt
from sklearn.cluster import KMeans

x =[3,1,8,3,8,4,9,4]
y =[6,4,8,4,2,8,0,5]


km= KMeans(n_clusters=3)
km.fit(list(zip(x,y)))

pt.scatter(x,y, c= km.labels_)
pt.show()
