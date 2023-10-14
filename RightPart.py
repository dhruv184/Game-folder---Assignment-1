def right():
    import Level2
    
    print("\nYou have taken right path...")
    print("As you move on right path... You encounter a river.")
    
    while True:

        print("\nWhat will you do???\n")
        print("1> Try to find a way to cross river.")
        print("2> Try to swim to cross river\n")
        
        y=int(input("Enter the choice (1 or 2)=="))

        if y==1:

            print("\nYou found there many tree on the side of river")
            print("\nWhat will u do with them?\n")
            print("A> Make a boat to cross river.")
            print("B> Cut a tree to make a bridge to cross river.\n")
            
            z=str(input("Enter the choice (A or B)=="))
 
            if z=="A":

                print("\nCongratulations! You built a Boat and crossed the river.\n")

                print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")

                print("\nWelcome to Level --> 2\n")
                Level2.level2()
                
                break
            
            elif z=="B":

                print("""
                    You cut a tree and tried to use it as a bridge,
                    but you sliped and got swept away by the current. Game over.
                    """)

                break 
            
            else:
                print("wrong input  Try again")
                
            break

        elif y==2:
            print("\nYou tried to swim but got swept away by the current. Game over.\n")

            break
           
        else:
            print("\nInvalid input. Please Enter again...\n")
    

    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")