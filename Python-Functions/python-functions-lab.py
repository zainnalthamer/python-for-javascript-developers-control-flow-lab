# Exercise 1: Calculate Area of a Triangle
def calculate_area_triangle(base, height):
    area = (base * height / 2)
    print(area)

calculate_area_triangle(10, 5)

# Exercise 2: Calculate Simple Interest
def simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    print(simple_interest)

simple_interest(1000, 5, 2)

# Exercise 3: Apply a Discount
def apply_discount(price, discount):
    new_price = price - (price*(discount/100))
    print(new_price)

apply_discount(100, 25)

# Exercise 4: Convert Temperature
def convert_temperature(temp, unit):
    if unit.lower() == 'c':
        return (temp * 9/5) + 32
    elif unit.lower() == 'f':
        return (temp - 32) * 5/9

print(convert_temperature(0, 'C'))

# Exercise 5: Sum to N
def sum_to(n):
    total = 0

    for i in range(0, n+1):
        total += i
    return total

print(sum_to(6))

# Exercise 6: Find the Largest Number
def largest(num1, num2, num3):
    return max(num1, num2, num3)

print(largest(1, 2, 3))

# Exercise 7: Calculate a Tip
def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount*(tip_percentage/100)
    return tip

print(calculate_tip(50, 20))

# Exercise 8: Calculate Product of Numbers
def product(*args):
    product = 1

    for num in args:
        product = product*num
    return product

print(product(2, 5, 5))

# Exercise 9: Basic Calculator
def basic_calculator(num1, num2, operation):
    if (operation == 'add'):
        return num1 + num2
    elif (operation == 'subtract'):
        return num1 - num2
    elif (operation == 'multiply'):
        return num1 * num2
    elif (operation == 'divide'):
        return num1 / num2

print(basic_calculator(10, 5, 'divide'))