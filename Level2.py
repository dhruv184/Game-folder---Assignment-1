def level2():

    import random
    
    health1=100
    health2=120
    
    print("""
        You have got out of the dark forest...
        But still you have not escaped the game,
        as a Monster is on your the way!!!
        You must defeated to escape...
          """)
    
    b=str(input("Give a name to your charactor =>"))

    print("\nRules:-\n")
    print("1.",b,"can hit damage between 20 and 25 only")
    print("2. The Monster's health will be denoted by '*' sign. The more the '*' the more is the health.\n")
    
    while True :

        if health2>=0 and health1>0:
            
            x=int(input("Give Damage: "))

            if x>=20 and x<=25:

                health2=health2-x
                health1=health1-random.randint(20,25)

                if health2>0:

                    print("\nHealth of oppenent==>") 

                    for i in range(health2,-1,-20):
                        print("*",end=" ")

                    print("\n") 

                else:
                    print("\nMonster Health ==> 0")  

            else:
                print("\nwrong input\n")
                
        elif health2<=0:

            print("\nyou win\n")
   
            break
        
        elif health1<=0:

            print("Monster win\n")
            
            break
        
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    print("\nDo you want to Play Again\n")