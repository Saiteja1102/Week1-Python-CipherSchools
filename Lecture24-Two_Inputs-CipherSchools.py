# name = input("Enter your name: ")
# age = input("Enter your age: ")
#can even write in one line

name,age = input("Enter your name and age sperated by space ").split(" ")
# give space between name and age
name,age = input("Enter your name and age sperated by comma ").split(",")
# give comma between name and age
print(name)
print(age)