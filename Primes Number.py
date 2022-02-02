# print all prime numbers between 2 and 50

this_number = int(input("enter a number: "))

while (this_number < 51):
    is_prime_number = True
    counter = 'this_number'
    while (counter < this_number -1):
        if ((this_number % counter) == 0):
            is_prime_number = False
        counter = counter + 1
        
    if (is_prime_number == True):
         print(this_number)
         
    this_number = this_number + 1
