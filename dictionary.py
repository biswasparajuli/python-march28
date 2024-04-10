a={
    'name': 'Sudan',
    'address': 'Kathmandu',
    'phone_Number': 98550000000
}
b={
    'colour_liked': 'red', 'fruit_liked': 'banana'
}
a['name']='Biswas'
a['country']='Nepal'
print(a)
print(a['name'])
print(a.keys())
print(a.values())
print(len(a))
print(b)
a['c']=b
print ("Test..............", a)
print(a['c']['fruit_liked'])
print(a['c']['fruit_liked'])

data = {
    'name': 'Biswas',
    'phone': [{
        'type': 'NTC',
        'number': 9855013113
    },
    {
        'type': 'NCELL',
        'number': 9808595491
    }],
    'address': ['dang', 'kathmandu']
}
print ('Testing .........', data)
