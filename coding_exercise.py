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

