a = [] # Empty List
a = [1,2,3,4,5,6] # List with integers number
a = ['broadway', 1 , 2,3]
print (len(a)) # length of data
print (a[-1], a[0]) # number always start with 0 and ends at -1
# slicing
a = ['broadway', 1 , 2,3]
print(a[0:2])
print(a[:])
print(a[::])
# list in List
data = [1,2,3,4,['Sudan', 'Test']]
print(data[-2][0])