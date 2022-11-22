# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
t_left = 90 - age
days = t_left * 365
weeks = t_left * 52
months = t_left * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")