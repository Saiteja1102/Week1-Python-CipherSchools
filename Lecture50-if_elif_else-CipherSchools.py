# if elif else statement

# show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = int(input("Please input your age: "))
if age>0 and age<=3:
    print("Ticket price: Free")
elif age>3 and age<=10:
    print("Ticket price: 150")
elif age>10 and age<=60:
    print("Ticket price: 250")
else:
    print("Ticket price: 200")