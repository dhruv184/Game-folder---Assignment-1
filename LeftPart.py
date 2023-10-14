def left():

    import Level2

    print("\nYou have taken Left path...")
    print("As you move on Left path... You encounter a big round opening, filled with darkness .")

    while True:

        print("\nWhat will you do???\n")
        print("1> Try to Go in the cave and find a way out..")
        print("2> Try to find other way.\n")

        a=int(input("Enter the choice (1 or 2)=="))

        if a==1:

            print("""
                You entered the cave with a Long stick and torch...
                But at the end of the cave there a Tiger who blocked the way to go out.
                """ )
            
            print("\nWhat will u do now?\n")
            print("A> Face the tiger to go out of the cave.")
            print("B> Run away.\n")

            b=str(input("Enter the choice (A or B)=="))
            
            if b=="A":

                print("""
                    Congratulations! By using the stick and torch 
                    You face the Tiger and made a way out of the cave and forest. 
                    """)
                
                print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")

                print("\nWelcome to Level --> 2\n")
                Level2.level2()

                break

            elif b=="B":

                print("""
                    You tried to run away from Tiger,
                    but Tiger caught you and you were killed . Game over.
                    """)

                break
            else:
                print("wrong input  Try again")
                
            break

        elif a==2:

            print("""
                    You tried to find other way to get out,  
                    but got by Tiger and you were killed. Game over.
                """)
            
            break
    
        else:
            print("Invalid input. Please Enter again...\n")
          
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")