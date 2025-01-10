#lJudah Franklin
#Judah Franklin
#10/17/2024
def namegenerator():
    print("Welcome to What Nba Player you are")
    print("Answer the following questions to find out which NBA player you are most alike")
    Region = input("Would you rather be in the East or West?: " )
    if Region == "West":
        CurrentPast = input("Would you rather be a Current or Past player?: ")
        if CurrentPast == "Current":
            ShooterRounded = input("Would you rather be an elite shooter(E) or an extremely well rounded player(R): ")
            if ShooterRounded == "E":
                print("You are Steph Curry!")
            else:
                print("You are Lebron James!")
        else:
            ScorerBully = input("Would you rather be an elite scorer(S) or an elite bully dunker(D): ")
            if ScorerBully == "S":
                print("You are Kobe Bryant!")
            else:
                print("You are Shaquille O'neal!")
    else:
        PastCurrent = input("Would you rather be a Current or Past player?: ")
        if PastCurrent == "Current":
            RimShooter = input("Would you rather be an Elite Rim Rusher(R) or an elite shooter(S)?: ")
            if RimShooter == "R":
                print("Giannis Antetokounmpo!")
            else:
                print("You are Jalen Brunson!")
        else:
            WinnerHandler = input("Would you rather be the best winner and scorer OAT(W) or the best Ball Handler OAT(H): ")
            if WinnerHandler == "f":
                print("You are Allen Iverson!")
            else:
                print("You are Michael Jordan")

namegenerator()
