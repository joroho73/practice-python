# Rock Paper Scissors
# R > S
# S > P
# P > S

valid_input = ["R", "P", "S"]

p1 = input("P1: Choose: R, P or S: ").upper()
p2 = input("P2: Choose: R, P or S: ").upper()

if p1 not in valid_input or p2 not in valid_input:
    print(f"Either {p1} or {p2} is not a valid input.")
else:

    winner = ""

    if p1 == "R":
        if p2 == "R":
            winner = "Draw"
        elif p2 == "S":
            winner = "Player 1"
        elif p2 == "P":
            winner = "Player 2"
    elif p1 == "P":
        if p2 == "P":
            winner = "Draw"
        elif p2 == "R":
            winner = "Player 1"
        elif p2 == "S":
            winner = "Player 2"
    elif p1 == "S":
        if p2 == "S":
            winner = "Draw"
        elif p2 == "P":
            winner = "Player 1"
        elif p2 == "R":
            winner = "Player 2"
            
    print(f"Congratulations! The winner is {winner}!")
    