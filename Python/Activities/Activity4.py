player1= input("enter name of player1")
player2= input("enter name of player2")
choiceplayer1=input("enter the choice of player1")
choiceplayer2=input("enter choice of player2")

while True:
    if choiceplayer1==choiceplayer2:
        print("tie")
    elif choiceplayer1 =='Rock':  
            if choiceplayer2=='Scissors':
                print("rock wins")
            else:
                print("paper wins")    
    elif choiceplayer1=='Scissors':
        if choiceplayer2=='paper':

            print(" Scissors wins")
        else:
            print("Rock wins")
    elif choiceplayer1=='Paper':
        if choiceplayer2=='rock':

            print(" paper wins")
    else:
            print("scissors wins")           

else:
    print("invalid entry")

playagain= input("want ot play again:")
if playagain=="yes":
    pass
elif playagain=="No":
    raise SystemExit
else:
    print("invalid entry")