a = 10
# print (a+b)

try:
    print(a+'333')
except NameError as e:
    print(e)
except TypeError as e:
    print(e)
except SyntaxError as e:
    print(e)
except:
    print('Error Occoured')