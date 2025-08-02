import keyword


print('=='*20)

print(keyword.__package__)
print('=='*20)
print(keyword.__all__)
print('=='*20)

print(keyword.__name__)
print('=='*20)

print(keyword.__loader__)
print('=='*20)

mylist = ['python','django', 'admin', 'forms', 'Barri']

print(dir(keyword)) 


def formation():
    return 'commnet fonctionne '