# Answer:

name,single_char = input("Enter the name and single character using comma: ").split(",")
name.strip().lower()
print(len(name))
print(name.count(single_char))
