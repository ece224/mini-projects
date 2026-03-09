# Taş kağıt makas oyunu
# bilgisayarla oynancağı için önce bilgisayarın seçimlerini simüle etmemiz için random modülünü içe aktarmamız lazım.
import random
#kullanıcıdan girdi almak input() 

user_choice= input("enter a choice(rock,paper,scissors): ")
#şimdi bilgisayarın seçimi
possible_options= ["rock","paper","scissors"]
computer_choice= random.choice(possible_options)
#listeden rasgele bir öğe seçilmesini sağladık

print(f"\you chose {user_choice}, computer chose {computer_choice}.\n")

# kazananı belirleme her iki oyuncuda seçimini yaptı

if user_choice == computer_choice:
    print(f"both players selected {user_choice}. it is tie!")
elif user_choice =="rock":
    if computer_choice =="scissors":
        print("rock smashes scissors! you win!")
    else:
        print("paper covers rock! you lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("papers covers rock! you win!")
    else:
        print("scissors cuts paper! you lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("scissors cuts paper! you win!")
    else:
        print("Rock smashes scissors! you lose.")  
# buradaki kod yalnızca bir oyun oynamanıza izin veriyo       
        
    
    