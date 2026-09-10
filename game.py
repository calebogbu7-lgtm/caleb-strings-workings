import random
secret_number = random.randint(1, 50)
while True:
    try:
        guess = int(input("guess_a_number "))
    except:
        print("entry is invalid")
        continue
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("you are correct")
        break