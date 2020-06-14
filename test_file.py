def div_num_3_5(num):
    return num % 5 == 0 and num % 3 ==0

def div_num_5(num):
    return num % 5 == 0

def div_num_3(num):
    return num % 3 == 0

def game(num):
    if div_num_3_5(num):
        print('bizzuu')
    elif div_num_5(num):
        print('bizz')
    elif div_num_3(num):
        print('buzz')
    else:
        print(num)

while True:
    num = input("Please enter your number:")
    if 'exit' in num:
        print('pineapple')
        break
    if num.isnumeric():
        num = int(num)
    for number in range(0, num+1):
        game(number)