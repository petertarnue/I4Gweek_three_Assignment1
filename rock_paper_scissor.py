# import the random module
import random 

def rock_paper_scissor_game():
    print(' ')
    while True:
        player = input("Please enter your choice (rock, paper, scissors): ")
        player = player.upper()

        possible_game_action = ["R", "P", "S"] 

        computer = random.choice(possible_game_action)

        print(f"Player ({player}) : computer ({computer}).\n")

        if player == "S":
            if computer == "P":
                print("Scissor cuts paper! You win")
            else:
                print("Rock smashes scissor! You lose.")
       
        elif player == "P":
            if computer == "R":
                print("Paper cover rock! You win!") 
            else:
                print("Scissor cuts paper! You lose.") 

        elif player == computer:
            print(f"Both players selected ({player}). It is a tie")
            print("Let us Play Again since we had tie in the previous game ")
            rock_paper_scissor_game()

        elif player == "R":
            if computer == "S":
                print("Rock smashes Scissors! You Win.")
            else:
                print("Paper cover rock! You lose.") 
        
        elif player != "R":
            print("You have enter an invalid word. That's violation of the game rule")
            print("Please try again with either of the these letters, 'R', 'S', or 'P' ")
            rock_paper_scissor_game()
        
        elif player != "S":
            print("You have enter an invalid response. That's violation of the game rule")
            print("Please try again with either of the these letters, 'R', 'S', or 'P' ")
            rock_paper_scissor_game()

        elif player != "P":
            print("You have enter an invalid response. That's violation of the game rule")
            print("Please try again with either of the these letters, 'R', 'S', or 'P' ")
            rock_paper_scissor_game()
        
        play_again = input("Do you want to play another game? yes (Y), no (N): \n")
        play_again = play_again.lower()

        if play_again == "y":
            rock_paper_scissor_game()

        else:
            print("Thank for playing this beautiful game. Hope you enjoyed playing it!")
        break


rock_paper_scissor_game()
