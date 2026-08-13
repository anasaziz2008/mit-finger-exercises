N = int(input("Enter integer 1 - 1000: "))

low = 0
high = 1001
guess = (low + high) // 2
count = 0

while guess != N:
    if guess < N:
        low = guess
    else:
        high = guess
    guess = (low + high) // 2
    count += 1
print("The number is:", guess)
print("The number of guesses is:", count)