import pandas as pd
import numpy as np

arr = [(3,4,10) , (4,5,20) , (6,7,30) , (7,8,40)]

arr2 = [(30,4,10,100) , (40,5,20,300) , (60,7,30,400) ]


df1=pd.DataFrame(arr, columns=['a' , 'b' , 'c' ]) 
df2=pd.DataFrame(arr2, columns=['a' , 'b' , 'c','d' ]) 

print(df1.shape)
print(df2.shape)


print (df1)

print("----------------------------")

df = df1.iloc[2:4,2:3]
print(df)

mul =  2*df1
print(mul)



mul =  

print("elementwise \n" , mul)


# mul =  np.multiply(df1 , df2)
# print("elementwise multiple \n" , mul)


# mul =  df1 * df2
# print("elementwise multiple \n" , mul)


mul =  np.dot(df1 , df2)
print("dot product multiple \n" , mul)

print("----------------------------")