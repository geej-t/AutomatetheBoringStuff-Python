catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothin to stop.):')

    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatentation
print('The cat names are:')
for name in catNames:
    print(' ' + name)

# supplies = ['pens','papers','staplers']
# for i in range(len(supplies)):
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])