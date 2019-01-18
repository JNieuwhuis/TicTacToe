#Gemaakt door Jackolien Nieuwhuis

def print_header():
    print("Welcome to this game of Tic Tac Toe!")

def draw_board(choices):
    toprint = ""
    for position in range(len(choices)):
        if position != 2 and position != 5 and position != 8:
            toprint += " " + str(choices[position]) + " |"  
        elif position == 2 or position == 5:
            toprint += " " + str(choices[position]) + "\n-----------\n"
        else:
            toprint += " " + str(choices[position])
    print("\n"+toprint+"\n")

           
def player_turn(choices, player):
    validChoice = False
    while not validChoice:
        choice = input("\n Where do you want to place your " + player + "? >> ")
        if not choice.isdigit():
            print("\n Please only insert numbers.")
        else:
            choice = int(choice) -1
            if choice<0 or choice>8:
                print("\n Please enter a value between 1 and 9.")
            else:
                if not str(choices[choice]).isdigit():
                    print ("\n Position already taken!")
                else:
                    choices[choice] = player
                    validChoice = True
                    return choices 


def check_choices(choices, player):
    count = 0
    win_combinations = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for combi in win_combinations:
        if choices[combi[0]] == choices[combi[1]] == choices[combi[2]] == player:
            print("\n Player " +player+ " Wins! Congratulations!\n")
            return True
    if 9 == sum((n=="X" or n=="O") for n in choices):
        print("It's a tie!\n")
        return True
               

def change_player(player):
    if player == "X":
        return "O"
    else:
        return "X"


def tictactoe():   
    play_again = True
    while play_again:
        print_header()
        print("\nLet's start!")
        choices = [1,2,3,4,5,6,7,8,9]
        isGamePlaying = True
        player = "X"
        draw_board(choices)
        play_again = False
        while isGamePlaying:
            choices = player_turn(choices, player)
            draw_board(choices)
            if check_choices(choices, player):
                isGamePlaying = False
            player = change_player(player)
        if input("Do you want to play again? (y/n) \n>> ").lower() == ("y"):
            play_again = True
          
            
tictactoe()
