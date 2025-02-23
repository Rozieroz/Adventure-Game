name = input("What is our name? ").strip().capitalize()
if not name or name.isspace():
    name = "Guest"
print(f"{name}, welcome to this short adventure.")

answer = input("""You wake up in a room with 2 doors to exit the room. 
               One on your right and the other on your left. Which door do you use to exit?
               Type right or left: """).lower().strip()

if answer == "left":
    left_ans = input("""The door leads to a forest and you can't go back. As you walk, you see a 
capuchin monkey that is hurt and nearby there is a hyena. Do you go to save it or run away?
Type 'save' to save it or 'run' to run away: """).lower().strip()
    
    while left_ans not in ["save", "run"]:
        print("Please choose either 'save' or 'run'")
        left_ans = input("Type 'save' or 'run': ").lower().strip()
    
    if left_ans == "save":
        print("It's great to see you have such a good heart, :)")
    elif left_ans == "run":
        print("Ha ha... Survival for the fittest it is.")
    else:
        print("Not a valid answer")
    
elif answer == "right":
    right_ans = input("""The door opens up to a city street. You come across a treasure box and a hurt child and you can 
                      either pick the treasure box or help the child get to a hospital, ONLY ONE. Type (box) to pick the 
                      treasure box and (child) to help the child: """).lower()
    
    if right_ans == "box":
        print("Out of words but okay")
    if right_ans == "child":
        print("The world really needs more people like you, I'm moved :)")
    else:
        print("Not a valid answer")
    
else:
    print("Not a valid answer. You loose :(")

print(f"Thank you {name} for trying and for your time")

help(list)