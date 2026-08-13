denary = int(input("Enter a denary number: "))

result = ""
while denary > 0:
    result = str(denary % 2) + result
    denary = denary // 2
print("The binary representation is:", result)