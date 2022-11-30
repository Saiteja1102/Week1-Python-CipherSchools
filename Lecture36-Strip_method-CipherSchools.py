name = "        Sai Teja      "
dots = "............................"

# lstrip() method - remove left spaces
# rstrip() method - remove right spaces 

print(name + dots)
print(name.lstrip() + dots)
print(name.rstrip() + dots)

# strip method - removes left and right space but does not remove middle spaces
print(name.strip() + dots)

# To remove all spaces 
print(name.replace(" ","") + dots)