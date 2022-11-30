# replace() method

string = "She is beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was",1))
print(string.replace("is","was",2)) 

# find() method - to find position of a string

print(string.find("is"))
print(string.find("is",5))

# to find second is
is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1 + 1) # adding plus 1 to avoid the same output
print(is_pos2)
