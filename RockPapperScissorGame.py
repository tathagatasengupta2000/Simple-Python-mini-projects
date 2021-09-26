rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
signs=[rock,paper,scissors]
print("Welcome to Rock Papper Scissors Game")
yc=int(input("Enter your choice, 0 for Rock, 1 for Papper, 2 for Scissors\n"))
if yc>=3:
  print("You have entered invalid numbe, You LOSE....")
else:  
  import random
  cc=random.randint(0,2)
  print(signs[cc])
  print("Computer Choose")
  print(signs[yc])
  print("Your Choose")
  if yc==cc:
    print("Its a Draw")
  elif yc==0 and cc==1:
    print("You Lose...")
  elif yc==0 and cc==2:
    print("You Win....")
  elif yc==1 and cc==0:
    print("You Win...")
  elif yc==1 and cc==2:
    print("You Lose....")
  elif yc==2 and cc==0:
    print("You Lose...")
  elif yc==2 and cc==1:
    print("You Win....")