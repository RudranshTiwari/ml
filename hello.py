# import datetime as dt 
# import time as tm

# # print(tm.time())
# # dtnow = dt.datetime.fromtimestamp(tm.time())
# # print(dtnow.year)


# delta = dt.timedelta(days = 100)
# today = dt.date.today()
# print(today-delta)

# store1 = [ 10, 11, 12.34 , 2.34]
# store2 = [9, 11.10, 12.34, 2.01]
# cheapest = map(max, store1,store2)
# print(cheapest)

# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

# def split_title_and_name(person):
#     return person

# print(list(map(split_title_and_name, people)))
 

# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

# def split_title_and_name(person):
#     title = person.split()[0]
#     lastname = person.split()[-1]
#     return '{} {}'.format(title, lastname)

# print(list(map(split_title_and_name, people)))

# lowercase = 'abcdefghijklmnopqrstuvwxyz'
# digits = '0123456789'

# correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

# print(correct_answer[1:] )# Display first 50 ids
# import numpy as np
# mylist = [1,2,3]
# x = np.array(mylist)
# y = np.array([4,5,6])

# m = np.array([[7,8],[3,5]])
# print(m.shape)
# print(m)
# n = np.arange(0,30,2)
# n = n.reshape(5,3)
# print(n)
import pandas as pd
import numpy as np
# pd.Series
# animals = ['tiger' , ' bear' , ' moose']
# print(pd.Series(animals))
# number = [ 1.4 ,34 ,332,342]
# # print(pd.Series(number))
# sports = {"archery" :" bhuthan"
#  ,"football" : "india",
#  "sumo" : "china"} 
# s = pd.Series(sports)
# print(s)
# print(s.index)
# number = [1,2,3,4,None]
# print(pd.Series(number))
# s = pd.Series(np.random.randint(0,1000,10000))
# print(s.head())
# %%timeit -n  100
# summary = 0
# for item in s:
#     summary += item
# purchase_1 = pd.Series({'name' : 'rud', 'item' : 'dog food', 'cost' : 223})
# purchase_2 = pd.Series({'name' : 'nit','item' :'cat food' , 'cost' : 2222})
# df = pd.DataFrame([purchase_1, purchase_2],  index = ['store1', 'store2'])
# print(df.head)
 
# purchase_1 = pd.Series({'Name': 'Chris',
#                         'Item Purchased': 'Dog Food',
#                         'Cost': 22.50})
# purchase_2 = pd.Series({'Name': 'Kevyn',
#                         'Item Purchased': 'Kitty Litter',
#                         'Cost': 2.50})
# purchase_3 = pd.Series({'Name': 'Vinod',
#                         'Item Purchased': 'Bird Seed',
#                         'Cost': 5.00})

# df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'], 'cost' = cost*20/100)