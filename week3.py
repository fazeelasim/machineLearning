# a = 3
# b = 5
# while b > a: 
#     print (a)
#     a=a+1

# class class2:
#     def __init__(self) -> None:
#         self.a=5

# class class3(class2):
#     def abc(self) -> None:
#             self.b=8
#             self.b = self.a  


# ob1= class3()
# ob1.abc()
# print(ob1.a, ob1.b)

import numpy as np
# import scipy as sy
# from scipy import stats as st
# list1=[345,234,45,23,23,3124]
# #m=np.mean(list1)
# #m=np.median(list1)
# m=st.mode(list1)
# print(m)


list1=[345,234,45,23,23,3124]
#m = np.std(list1)
#m = np.var(list1)
m = np.percentile(list1,23)
print(m)





