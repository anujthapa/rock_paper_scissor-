from random import randint

possiable_outcomes =["PAPER", "ROCK", "SCISSOR"]

def generate_outcome():
    return possiable_outcomes[randint(0,len(possiable_outcomes)-1)]


def main():
    while True:
        print(f"Welcome to RPS game.")
        print(f"1. Press 1 for PAPER")
        print(f"2. Press 2 for ROCK")
        print(f"3. Press 3 for SCISSOR")

        user_input = input(f"Enter your choice")
        if user_input not in ["1","2","3"]:
            print(f"Invalid choice, Please choose again")
            continue

        computer_choice = generate_outcome()            
        print(f"Your choice is {user_input}. \n Computer choice is {computer_choice}.")


        if user_input == "PAPER" and  computer_choice == "2":
            print(f"Sorry You loose")
        elif user_input == "ROCK" and computer_choice == "0":
            print(f"Sorry You loose")
        elif user_input == "SCISSOR" and computer_choice == "1":
            print("Sorry You loose")
        elif user_input == computer_choice:
            continue
        else :
            print(f"Congratulations You Won!!!!!")
         

        choice = input(f"Enter 1 to reply and 0 to exit")
        print(f"Choice to reply {choice}")
        match choice:
            case "1":
                print("Welcomeback")
                continue
            case "0":
                print(f"Thanks for playing")
                break
            case _:
                print("Invalid choice, Thanks for playing")
                break




        

if __name__ == "__main__":
    main()