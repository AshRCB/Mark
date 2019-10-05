import time

name=input("enter your name: ")

print("Hello, " + name, "Time to play hangman!")
time.sleep(1)

print ("Start guessing...")
time.sleep(1)

guesses=''
turns=10
word="python"

while turns>0:
    failed=0
    
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_ ",end="")
            failed+=1
    
    if failed==0:
        print("You Won")
        break
    guess=input("\nGuess the word:")
    guesses+=guess
    
    if guess not in word:
        turns-=1
        time.sleep(0.5)
        print("Wrong")
        time.sleep(0.5)
        print("you have {} more guesses".format(turns))
    
    if turns==0:
        time.sleep(0.5)
        print("You Loose")
