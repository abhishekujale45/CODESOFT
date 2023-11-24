import random as rd
game_array=["rock","paper","scissor"]

user=0
com=0
print(game_array)
_input=1
while(_input==1):
    computer_int = game_array[rd.randint(0, 2)]
    user_int = (input("\nEnter The Input For User "))
    print(f"\nThe Computer choice is {computer_int}")
    print("The user Input is " ,user_int)
    if (user_int==computer_int):
        continue
    elif(user_int=="rock" and computer_int=="paper"):
        com+=1
    elif (user_int == "paper" and computer_int =="scissor" ):
        com += 1
    elif (user_int == "rock" and computer_int == "scissor"):
        user += 1
    elif (user_int == "paper" and computer_int == "rock"):
        user += 1
    elif (user_int == "scissor" and computer_int == "rock"):
        com += 1
    elif (user_int == "scissor" and computer_int == "paper"):
        user += 1
    _input=int(input("Enter 1 for Again "))
print("\nThe output for ")
print("------------------------")
print(f" computer is {com}|\n \t user is {user}|")
if (com==user):
    print("Tied")
elif(com>user):
    print("\nComputer  Wins")
else:
    print("\nUser Wins")