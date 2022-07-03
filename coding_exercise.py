########## 1 ###########

# make function
def max_func(*numbers):
    print(f"This numbers what you input {numbers}")
    max_num = max(numbers)
    print(max_num)


# call function
max_func(1, 2, 4, 7, 100)


########## 2 ###########

'''
The code below is just for check 1 number. And print 1 conditional statement.
'''
def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)


fizz_buzz(20)


'''
If you want to use loop, while input 1 number, i mean for limit. You can use the code below.
'''
def fizzbuzz(limit):
    for num in range(1,limit+1):
        if (num % 5 == 0) and (num % 3 == 0):
            print("Fizz Buzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else: 
            print(num)

fizzbuzz(100)


########## 3 ###########




########## 4 ###########
def showNumbers(limit):
    for number in range(1, limit+1):
        if number % 2 == 0:
            print(f"{number} is even number")
        else:
            print(f"{number} is odd number")


showNumbers(20)


########## 5 ###########


########## 6 ###########
def show_stars(rows):
    for stars in range(1, rows+1):
        many_stars = "*" * stars
        print(many_stars)


show_stars(10)


########## 7 ###########
def prime_num(limit):
    for number in range(1, limit+1):
        if number > 1:
            for num in range(2, number):
                if number % num == 0:
                    break
            else:
                print(number)


prime_num(20)
