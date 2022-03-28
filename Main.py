digits = input("Two digit number\n")
digit_one = digits[0]
digit_two = digits[1]
results = int(digit_one) + int(digit_two)
print(results)
numbers = input("Three digit numbers\n")
first_number = int(numbers[0])
second_number = int(numbers[1])
third_number = int(numbers[2])
print(first_number + second_number + third_number)
#Exercise:BMI calculator
height = input("what is your height in m: \n")
weight = input("what is your weight in kg: \n")
Body_mass_index = int(weight)/float(height)**2
BMI = round(Body_mass_index,2)
print(f"Your BMI is {BMI}")
#Tip Calculator
print("Hello, welcome to the tip calculator")
bill = float(input("What is the total bill\n"))
percentage = int(input("What percent would you like to tip\n"))
#print(type(percentage))
percentage_tip = percentage/100
print(percentage_tip)
number = int(input("How many are you\n"))
tip_per_person = float(bill*percentage_tip/number)
total_bill = tip_per_person*number+bill
print(f"Each person pays a tip of {tip_per_person}\nYour total bill is {total_bill}")