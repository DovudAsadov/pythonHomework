#Question 1
print("Valid" if input("Username: ") and input("Password: ") else "Invalid")

#Question 2
print("Equal" if int(input("1 number: ")) == int(input("2 number: ")) else "Not equal")

#Question 3
a1 = int(input("Enter input: "))
print("Positive and Even" if a1 > 0 and a1 % 2 == 0 else "Not Positive and Even")

#Question 4
a2 = {int(input(f"Enter number {i+1}: ")) for i in range(3)}
print("All different" if len(a2) == 3 else "Not all different")

#Question 5
print("Same length" if len(input("Enter first string: ")) == len(input("Enter second string: ")) else "Different length")

#Question 6
print("Divisible by 3 and 5" if (n := int(input("Enter a number: "))) % 3 == 0 and n % 5 == 0 else "Not divisible")

#Question 7
print("Greater than 50" if int(input("First number: ")) + int(input("Second number: ")) > 50 else "Not greater than 50")

#Question 8
print("In range" if 10 <= int(input("Enter a number: ")) <= 20 else "Out of range")