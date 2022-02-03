# print all prime numbers between 2 and every number that you want

first_num = int(input("enter first number: "))
second_num = int(input("enter second number: "))

if (first_num > second_num):
    print("your first number should be smaller than second one.")

while (first_num < second_num):
    is_prime_number = True
    counter = 2
    while (counter < first_num -1):
        if ((first_num % counter) == 0):
            is_prime_number = False
        counter = counter + 1
        
    if (is_prime_number == True):
         print(first_num)
         
    first_num = first_num + 1
