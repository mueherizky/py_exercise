########## 1 ###########

# make function
def max_func(*numbers):
    print(f"This numbers what you input {numbers}")
    max_num = max(numbers)  
    print(max_num)

# call function
max_func(1,2,4,7,100)


########## 2 ###########
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


########## 3 ###########



########## 4 ###########
def showNumbers(limit):
    for number in range(1,limit+1):
        if number % 2 == 0:
            print(f"{number} is even number")
        else:
            print(f"{number} is odd number")

showNumbers(20)


########## 5 ###########



########## 6 ###########
def show_stars(rows):
    for stars in range(1,rows+1):
        many_stars = "*" * stars
        print(many_stars)

show_stars(10)


