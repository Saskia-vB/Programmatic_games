# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

def fib_upto(num):
    new_num, num_1 = 0,0
    num_2 = 1
    while new_num < num:
        new_num = num_1 + num_2
        print(num_1)
        num_1 = num_2
        num_2 = new_num

fib_upto(7)