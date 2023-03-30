import sys
num = 0

def collatz(number):
    if number % 2 == 0:
        num = number // 2
        print(num)
    else:
        num = 3 * number + 1
        print(num)


while num != '':
    try:
        num = int(input("Enter number:"))
        collatz(num)
    except:
        print('Numbers only')