from random import choice

options = ["R", "P", "S"]
optionsDict = {"R": "Rock", "P": "Paper", "S": "Scissors"}
while True:
  playerChoice = input(f'Pick an option between {" ".join(options)}: ').upper();
  if not playerChoice in options:
    print("The option provided is not a valid option")
    continue
  computerChoice = choice(options)
  print(f'Player ({optionsDict[playerChoice]}) : CPU ({optionsDict[computerChoice]})')
  if playerChoice == computerChoice:
    print("It's a tie")
    continue
  elif (playerChoice == "R" and computerChoice == "S") or (playerChoice == "P" and computerChoice == "R") or (playerChoice == "S" and computerChoice == "P"):
    print("You won !!!")
    break
  else:
    print("CPU Won !!!")
    break
