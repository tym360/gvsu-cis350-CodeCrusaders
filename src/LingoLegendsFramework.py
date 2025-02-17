import random
from colorama import Style, Fore;
#Will change to API when chosen
words = ["tiger", "bacon", "agile", "group", "lingo"]
Level_word = random.choice(words)

print(f"Lingo legends {Fore.GREEN}framework{Style.RESET_ALL}")
print("You will be given 5 attempts to guess the word (5 Letters)")

User_attempts = 0

while User_attempts < 5:
    Current_attempt = input("Guess " +  str((User_attempts + 1)) + " >>").lower()
    #make sure sure gives the right amount of letters
    if len(Current_attempt) != 5:
        print("You guessed a word without 5 letters")
    User_attempts = User_attempts + 1

    Progress = ""
    for x in range(5):
        if Current_attempt[x] == Level_word[x]:
            Progress += Fore.GREEN + Current_attempt[x]+ Style.RESET_ALL
        elif Current_attempt[x] in Level_word:
            Progress += Fore.YELLOW + Current_attempt[x]+ Style.RESET_ALL
        else:
            Progress += "_"

    print("Your progress: " + Progress.strip())

    if Current_attempt == Level_word:
        print("Yes! the word was: " + Fore.GREEN + Level_word + Style.RESET_ALL)
        winner = True
        break
if(winner != True):
    print("You have used all of your attempts! The correct word was: " + Fore.GREEN + Level_word + Style.RESET_ALL)
