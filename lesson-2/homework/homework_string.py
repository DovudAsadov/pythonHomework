#Question 1
name, year = input("Enter name: "), int(input("Enter year: "))
print(f"{name} {2024 - year} years old.")

#Question 2
txt = 'LMaasleitbtui'
print(f"{txt[1:3]}{txt[5]}{txt[7]}{txt[9]}{txt[11]}")

#Question 3
a1 = input("Enter string: ")
print(f"Length: {len(a1)}, Upper: {a1.upper()}, Lower: {a1.lower()}")

#Question 4
a2 = input("Enter a string: ")
print("Palindrome" if a2 == a2[::-1] else "Not a palindrome")

#Questrion 5
s = input("Enter a string: ").lower()
vowels = "aeiou"
a3, a4 = sum(1 for ch in s if ch in vowels), sum(1 for ch in s if ch.isalpha() and ch not in vowels)
print(f"Vowels: {a3}, Consonants: {a4}")

#Question 6
a5, a6 = input("Enter string 1: "), input("Enter string 2: ")
print("Contains" if a6 in a5 else "Does not contain")

#Question 7
a7, a8, a9 = input("Input sentence: "), input("Replace: "), input("With: ")
print(f"Output {a7.replace(a8, a9)}")

#Question 8
a10 = input("Enter a string: ")
print(f"First: {a10[0]}, Last: {a10[-1]}")

#Question 9
print(input("Enter string: ")[::-1])

#Question 10
print(len(input("Enter sentence: ").split()))

#Question 11
print(any(ch.isdigit() for ch in input("Enter string: ")))

#Question 12
list_of_words = []
while True:
    input_from_user = input("Enter input: ")
    if not input_from_user: 
        break
    else:
        list_of_words.append(input_from_user)

separator = input("Enter separator: ")  
print(separator.join(list_of_words)) 


#Qestion 13
print(input("Enter string: ").replace(" ", ""))

#Qestion 14
print("Equal" if input("Enter 1 string: ") == input("Enter 2 string: ") else "Not Equal")

#Qestion 15
print(''.join(a11[0].upper() for a11 in input("Enter sentence: ").split()))

#Qestion 16
print(input("Enter string: ").replace(input("Character to remove: "), ""))

#Qestion 17
a12, a13 = input("Enter string: "), input("Enter symbol: ")
print(''.join(a13 if ch in "aeiouAEIOU" else ch for ch in a12))

#Qestion 18
s, start, end = input("Enter string: "), input("Starts with: "), input("Ends with: ")
print("Matches" if s.startswith(start) and s.endswith(end) else "Does not match")