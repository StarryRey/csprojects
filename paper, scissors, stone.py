import random
options = ("rock", "scissors","paper")
player =  None
computer = random.choice(options)
running  = True

while running:

   while player not in options:
      player = input( "Enter a choice(rock, scissors,paper):")



   print (f"Player: {player}")
   print (f"Computer:{computer}")

   if player == computer:
      print ( "It's a tie!")
   elif player =='rock' and computer == 'scissors':
      print ("You win!")
   elif player == "paper" and computer == "rock":
      print ("You win!" )
   elif player == "scissors" and computer == "papar":
      print ( "You win!")
   else:
      print ( "You lose!")
   if not input("Play again?(y/n):").lower() =="y":
      running= False
print ( "Thanks for playing!")
