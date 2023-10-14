import RightPart
import LeftPart
def startgame():

    print("\nLEVEL => 1\n")

    print("""
        Welcome to Text-Based Adventure Game.
          
        Before we begin with game there is a back story:-
          
        You started a Trip to forest... 
          
        While trveling in the forest you missed sign on the path and got lost!
        You find yourself in a dark forest. You have to find a way out.
        """)
    print("\nYou see two path ahead ")
    
    while True:

        print("\nWhat will you do?\n")
        print("1> Take the Right Path..")
        print("2> Take the Left Path..")
        print("3> Quit\n")

        x=int(input("Enter the choice (1 or 2 or 3)=="))

        if x==1:
            RightPart.right()
        
        elif x==2:
            LeftPart.left()
            
        elif x==3:
            print("\nThanks For Playing\n")
            print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
            
            break

        else:
            print("Invalid input, Please Enter again...")  