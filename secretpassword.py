#This program open the secret sauce and validates the password
passwordFile = open('secretpasswordfile.txt')
secretpassword = passwordFile.read()
print('Enter your password:')
typedPassword = input()
if typedPassword == secretpassword:
    print('Access granted')
elif typedPassword == '12345':
        print('That password is one that an idot puts on their luggage.')
else:
    print('Access Denied')