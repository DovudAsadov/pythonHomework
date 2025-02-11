#Question 1
a1 = float(input("Enter Input: "))
print(round(a1, 2))

#Question 2
a2 = int(input("Enter Input: "))
a3 = int(input("Enter Input: "))
a4 = int(input("Enter Input: "))
print(max(a2, a3, a4))
print(min(a2, a3, a4))

#Question 3
a5 = float(input("Enter KM"))
print(f"Meters: {a5 * 1000}, Centimeters: {a5 * 100000}")

#Question 4
a6, a7 = int(input("Enter first number: ")), int(input("Enter second number: "))
print(f"Division: {a6 // a7}, Remainder: {a6 % a7}")

#Question 5
a8 = float(input("Enter Celsius: "))
print(f"Fahrenheit: {(a8 * 9/5) + 32}")

#Question 6
a9 = input("Enter Input: ")
print(f"Last digit: {a9[-1]}")

#Question 7
a10 = int(input("Enter a number: "))
print("Even" if a10 % 2 == 0 else "Odd")