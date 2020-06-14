
# fizzbuzz
# if divisible by 5 and 3 = fizzbuzz
# if divisible by 5 = fizz
# if divisible by 3 = buss

def div_by_5_and_3(num):
    return num % 5 == 0 and num % 3 == 0

def div_by_5(num):
    return num % 5 == 0

def div_by_3(num):
    return num % 3 == 0

def fizzbuzz(num):
    if div_by_5_and_3(num):
        print("fizzbuzz")
    elif div_by_5(num):
        print("fizz")
    elif div_by_3(num):
        print("buzz")
    else:
        print(num)

while True:
    num = input("please enter a number: ")
    if 'exit' in num:
        print("ciao bella")
        break
    if num.isnumeric():
        num = int(num)
    for number in range (1, num+1):
        fizzbuzz(number)
