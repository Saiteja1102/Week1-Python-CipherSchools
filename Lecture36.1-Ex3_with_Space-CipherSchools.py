name,char = input("Enter comma separated name and character : ").split(",")
print(f"length of your name is {len(name)}")
print(f"Character count: {name.strip().lower().count(char.strip().lower())}")

# Removing spaces
# name.strip().lower().count(char.strip().lower())
# char.strip().lower()
