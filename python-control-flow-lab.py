# # Exercise 1
vowels = ['a', 'e', 'i', 'o', 'u']

def check_letter():
    letter = input('Enter a letter (A-Z):').lower()
    if letter in vowels:
        print(f'The letter {letter} is a vowel.')
    else:
        print(f'The letter {letter} is a consonant.')

check_letter()

# Exercise 2
def check_voting_eligibility():
    age = input('Please enter your age:')

    if int(age) > 0 and int(age) >= 21:
        print('Eligible')
    else:
        print('Not eligible')
    
check_voting_eligibility()

# Exercise 3
def calculate_dog_years():
    dogs_human_age = input("Input a dog's age:")

    if int(dogs_human_age) <= 0:
        print('Age must be a positive number')
        return
    
    if int(dogs_human_age) == 1:
        age_in_dog_years = 10

    elif int(dogs_human_age) == 2:
        age_in_dog_years = 20
    
    else:
        age_in_dog_years = 20 + (int(dogs_human_age)-2)*7

    print(f"Your dog's age in dog years is {age_in_dog_years}")

calculate_dog_years()

# Exercise 4
def weather_advice():
    isCold = input('Is it cold outside? (yes/no):').lower()
    isRaining = input('Is it raining? (yes/no):').lower()

    if (isCold=='yes' and isRaining=='yes'):
        print("Wear a waterproof coat.")
    elif (isRaining=='no' and isCold=='yes'):
        print("Wear a warm coat.")
    elif(isCold=='no' and isRaining=='yes'):
        print("Carry an umbrella.")
    elif(isCold=='no' and isRaining=='no'):
        print("Wear light clothing.")
weather_advice()

# Exercise 5
def fizz_buzz():
    for i in range(1, 50):
        if(i%3==0 and i%5==0):
            print('FizzBuzz')
        elif(i%3==0):
            print('Fizz')
        elif(i%5==0):
            print('Buzz')
fizz_buzz()