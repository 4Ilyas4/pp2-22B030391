import random
print("Hello! What is your name?")
s=str(input())
print("Well, "+ s +", I am thinking of a number between 1 and 20.Take a guess.")
bl=False
k=0
while(bl==False):
    b=int(input())
    r = random.randint(1, 20)
    k+=1
    if b==r:
        bl=True
    else:
        print("Your guess is too low.Take a guess.")
print("Good job, "+ s +"! You guessed my number in "+ str(k) +" guesses!")
