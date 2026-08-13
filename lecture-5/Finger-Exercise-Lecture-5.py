str = input("Enter a string: ")

print("Characters at even indices:")

even_characters = ""
for i in range(0, len(str), 2):
    even_characters += str[i]
print(even_characters)