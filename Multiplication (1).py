import random

print("Welcome to the multiplication quiz game")
print("Select a difficulty: ")
print("""1. Easy
2. Medium
3. Hard
4. Quit""")

option = int(input("(1-3) Select option: "))

# Generate random numbers based on the selected difficulty

while True:
    if option == 1:
        for i in range(5):
            Computer = random.randint(1, 5)
            Space = random.randint(1, 5)
            print(f"Multiply {Computer} by {Space}")
            answer = (Computer * Space)
            final = int(input("Please enter your answer: "))
            if final == answer:
                print("You are correct")
            else:
                print("You are incorrect")
    if option == 2:
        for i in range(5):
            Computer = random.randint(5, 10)
            Space = random.randint(5, 10)
            print(f"Multiply {Computer} by {Space}")
            answer = (Computer * Space)
            final = int(input("Please enter your answer: "))
            if final == answer:
                print("You are correct")
            else:
                print("You are incorrect")
    if option == 3:
        for i in range(5):
            Computer = random.randint(10, 15)
            Space = random.randint(10, 15)
            print(f"Multiply {Computer} by {Space}")
            answer = (Computer * Space)
            final = int(input("Please enter your answer: "))
            if final == answer:
                print("You are correct")
            else:
                print("You are incorrect")
    if option == 4:
        break

