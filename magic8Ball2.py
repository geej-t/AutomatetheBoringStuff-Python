import random

msg = ['It is certain',
       'It is decidedly so',
       'Yes definitely',
       'Reply hazy try again',
       'Ask again later',
       'Concentrate and ask again']

print(len(msg))
print(msg[random.randint(0, len(msg) - 1)])