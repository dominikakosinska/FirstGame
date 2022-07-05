import random
# the beginning of the game
print("""Welcome to the game!

Give your name:
""")

name = input()

print(" ")
print(name + """, select: stone, paper or scissors and type below:
""")

# user choice

User = input()

# removing the occurrence of problems related with size of the letter

User_new = User.lower()

# user choice function, elimination of wrong written

def User_fun(User_new):
    x = 0
    if User_new == "paper":
        x += 0
    elif User_new == "stone":
        x += 1
    elif User_new == "scissors":
        x += 2
    else:
        print("\nSpelling mistake! Select again:")
        print(" ")
        User = input()
        User_new = User.lower()
        x = User_fun(User_new)
    return x

x = User_fun(User_new)
print(" ")


# computer choice

choice = ["paper", "stone", "scissors"]

computer = random.sample(choice, 1)

y = computer[0]

print(y)

# convert text to number

if y == "paper":
    y = 0
if y == "stone":
    y = 1
if y == "scissors":
    y = 2


print(" ")

if x == y:
    print("Draw")
elif (x == 0 and y == 1) or (x == 1 and y == 2) or (x == 2 and y == 0):
    print("You win!!!")
else:
    print("The computers win!!!")

