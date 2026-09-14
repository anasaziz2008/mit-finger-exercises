# Finger exercise: Write a lambda expression that has two numeric
# parameters. If the second argument equals zero, it should return
# None. Otherwise it should return the value of dividing the first
# argument by the second argument. Hint: use a conditional
# expression.

lambda_divide = lambda x, y: None if y == 0 else x / y
print(lambda_divide(10, 2))  # Returns 5.0