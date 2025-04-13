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
import random
list_of_choices = [rock, scissors, paper]

user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 Scissors."))
computer_choice = random.randint(0, 2)

if user_choice >=3 or user_choice <0 :
    print('You typed an invalid number')
else :
    print("You chose : \n", list_of_choices[user_choice])
    print("\n\n Computer chose : \n", list_of_choices[computer_choice])
    if user_choice == computer_choice:
        print ('Draw')
    elif ((user_choice - computer_choice)%3 == 1) :
        print("You win")
    else :
        print('You lose')