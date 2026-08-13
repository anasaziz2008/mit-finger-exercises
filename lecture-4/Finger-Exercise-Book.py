# Finger exercise: Write a program that asks the user to enter an
# integer and prints two integers, root and pwr, such that 1 < pwr < 6
# and root**pwr is equal to the integer entered by the user. If no such
# pair of integers exists, it should print a message to that effect


n = int(input("Enter number: ")) 
flag = False 
for pwr in range(2, 6): 
    guess = 0 
    while guess**pwr < n: 
        guess += 1 
    if guess**pwr == n: 
        print(f"{guess}**{pwr} = {n}") 
        flag = True 
if not flag: 
    print("error")


# Finger exercise: The Empire State Building is 102 stories high. A
# man wanted to know the highest floor from which he could drop an
# egg without the egg breaking. He proposed to drop an egg from the
# top floor. If it broke, he would go down a floor, and try it again. He
# would do this until the egg did not break. At worst, this method
# requires 102 eggs. Implement a method that at worst uses seven
# eggs.


