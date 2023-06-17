import random

cont='Y'
while(cont=='Y'):
    inp = input("Enter 'R' for rock or 'P' for paper or 'S' for scissor: ")
    print("your selection: ",inp)

    N = inp.upper()
    list = ['R', 'P', 'S']

    comp = random.choice(list)
    print("computers selection: ",comp)

    if(( (N == 'R') and (comp == 'S')) or
       ((N == 'P') and (comp == 'R')) or
       ((N == 'S') and (comp == 'P'))):
        print("You win")
    elif(((N == 'R') and (comp == 'R')) or
         ((N == 'P') and (comp == 'P')) or
         ((N == 'S') and (comp == 'S'))):
        print("tie")
    else:
        print("You lose")
    # if (N == 'R') and (comp == 'R'):
    #     print("tie")
    # elif (N == 'R') and (comp == 'P'):
    #     print("You lose")
    # elif (N == 'R') and (comp == 'S'):
    #     print("You win")

    # elif (N == 'P') and (comp == 'R'):
    #     print("You win")
    # elif (N == 'P') and (comp == 'P'):
    #     print("tie")
    # elif (N == 'P') and (comp == 'S'):
    #     print("you lose")

    # elif (N == 'S') and (comp == 'R'):
    #     print("You lose")
    # elif (N == 'S') and (comp == 'P'):
    #     print("You win")
    # elif (N == 'S') and (comp == 'S'):
    #     print("tie")
    cont=input("do you want to continue? Y/N :")


