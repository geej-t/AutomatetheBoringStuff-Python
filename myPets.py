#Program will checks if the name is in a LIST

myPets = ['Zophie','Pooka','Fat-tail']

print('Enter a per name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')