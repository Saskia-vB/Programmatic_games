user_input = int(input("Enter a number to check if prime or not: "))

def prime_number(user_input):
    for num in range(2, user_input):
        if num >1:
            for i in range (2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

print(prime_number(user_input))