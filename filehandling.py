f = open('classes.py','r')
print (f.read())

f = open ("data.txt",'w')
f.write('Hi Broadway!!!')
f.close()

f = open ("data.txt",'a')
f.write(" \n \t Hi This is testing 2")
f.close