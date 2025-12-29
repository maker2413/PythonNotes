import random

images = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
ran_choice = random.choice([0, 1, 2])

win = False

if choice == "0" or choice == "1" or choice == "2":
    print(images[int(choice)])
else:
    print("You did not pick an acceptable option. Please try again!")

print("Computer chose:")

print(images[ran_choice])

if choice == str(ran_choice):
    print("It's a draw")
elif choice == "0" and ran_choice == 2:
    print("You win!")
elif choice == "1" and ran_choice == 0:
    print("You win!")
elif choice == "2" and ran_choice == 1:
    print("You win!")
else:
    print("You lose")
