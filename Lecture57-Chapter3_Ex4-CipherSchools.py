# Solution

number = input("Enter more than one digit: ")
# "1245" # length = 4 , last index = 3
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)
