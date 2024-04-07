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
print(data[4][0])
# List Method
# mutable
# add data using append
teachers = ['Nasir', 'Irfan' , 'Haris', 'Sheraz', 'Farah']
teachers.append("Sudan")
teachers.append(1)
teachers.append(['1',3])
print (teachers)
# insert i.e. add to the given position
teachers.insert(2, "Sudan")
teachers.insert(-2, "Sudan")
print (teachers)
# extend means to extend list i.e. sum any 2 list
data.extend(teachers)
print (data)
# delete list
del teachers[0]
print(teachers)
# remove i.e. delete the data
teachers.remove('Sudan')
teachers.remove('Sudan')
teachers.remove('Sudan')
print (teachers)
# pop i.e. it delete data that is at last
colour=['Red','black', 'green']
colour.pop()
print( colour)
# Clear
colour.clear()
print (colour)


