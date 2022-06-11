import random, time
moves = ["rock", "paper", "scissors"]
# global playerScore, cpuScore
playerScore=0
cpuScore=0

def play():
    global playerScore, cpuScore
    time.sleep(1)
    print("Round ", str(rounds))
    playerMove = input("Choose Rock Paper or Scissors: ")
    print("CPU shows hand....")
    time.sleep(1)
    cpuMove = random.choice(moves)
    if playerMove=="rock" and cpuMove=="rock":
        print("Its a draw")
        print("Player Score: ", str(playerScore))
        print("CPU Score: ", str(cpuScore))
    elif playerMove=="rock" and cpuMove=="paper":
        print("Paper wraps around rock! CPU Wins!")
        cpuScore+=1
        print("Player Score: ", str(playerScore))
        print("CPU Score: ", str(cpuScore))
    elif playerMove=="rock" and cpuMove=="scissors":
        print("Rock breaks scissors! Player Wins!")
        playerScore+=1
        print("Player Score: ", str(playerScore))
        print("CPU Score: ", str(cpuScore))
    elif playerMove=="scissors" and cpuMove=="rock":
        print("Rock breaks scissors! CPU Wins!")
        cpuScore+=1
        print("Player Score: ", str(playerScore))
        print("CPU Score: ", str(cpuScore))
    elif playerMove=="paper" and cpuMove=="rock":
        print("Paper wraps around rock! Player Wins!")
        playerScore+=1
        print("Player Score: ", str(playerScore))
        print("CPU Score: ", str(cpuScore))
    elif playerMove=="paper" and cpuMove=="paper":
        print("Its a draw")
        print("Player Score: ", str(playerScore))
        print("CPU Score: ", str(cpuScore)) 
    elif playerMove=="scissors" and cpuMove=="scissors":
        print("Its a draw")
        print("Player Score: ", str(playerScore))
        print("CPU Score: ", str(cpuScore))
    elif playerMove=="scissors" and cpuMove=="paper":
        print("Scissors cuts paper! Player Wins!")
        playerScore+=1
        print("Player Score: ", str(playerScore))
        print("CPU Score: ", str(cpuScore))
    elif playerMove=="paper" and cpuMove=="scissors":
        print("Scissors cuts paper! CPU Wins!")
        cpuScore+=1
        print("Player Score: ", str(playerScore))
        print("CPU Score: ", str(cpuScore))

print("Welcome to Rock Paper Scissors")
time.sleep(2)
rounds=1
for i in range(5):
    play()
    rounds+=1

print("GAME OVER")