# strings are immutable
#               replace method can't change the original string

string = "string"
string.replace("t","T")
print(string) # does not change
new_string = string.replace("t","T")
print(new_string) 
