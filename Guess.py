def Play():
    import random
    import Level1
    
    def Guess():

        print("\nWelcome")
        print("\nBefore you play the game you need to perform a task...\n")
        print("\nYou need to guess correct number in 5 Tries and Correct number is between 1 to 10 only.\n")

        Random_number = random.randint(1,10)
        tries=0
        while True:

            guess = int(input("Enter your guess (1 B/W 10): "))
            tries = tries + 1

            if tries == 6:
                print("\nYou lost! Thanks For Playing\n")  

                c=str(input("Do you what to play again (yes/no)==>"))

                if c=="yes":
                    print("Try again")
                    continue
                else:
                    print("Thanks for playing")

                break    
                
            elif guess < Random_number:
                print("Too low! Try again.")

            elif guess > Random_number:
                print("Too high! Try again.")

            else:
                print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
                Level1.startgame()
                
                break

    Guess()           