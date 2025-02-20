"""
TODO:
-Implement API []
-Develop Difficulty System []
    - Create variable for user global progress and grab word from API. Implementation Depends on API or Library Used.
- Catch Errors for users submitting words that are smaller. [Done]
"""

import random
from colorama import Style, Fore
import word_generator


Level_word = word_generator.generate_word_medium()

print(f"Lingo legends {Fore.GREEN}framework{Style.RESET_ALL}")
print(f"You will be given 5 attempts to guess the word ({len(Level_word)} Letters)")

User_attempts = 0
winner = False
while User_attempts < 5:
    Current_attempt = input("Guess " +  str((User_attempts + 1)) + " >>").lower()
    # Make sure user gives the right amount of letters

    Progress = ""
    # Exception handling Below:  Current_Attempt is broken down into an array, something outside of Level_word's length will cause an Index Error.
    # Test parsing
    try:
        for x in range(len(Level_word)):
            if Current_attempt[x] == Level_word[x]:
                Progress += Fore.GREEN + Current_attempt[x] + Style.RESET_ALL
            elif Current_attempt[x] in Level_word:
                Progress += Fore.YELLOW + Current_attempt[x] + Style.RESET_ALL
            else:
                Progress += Fore.RED + Current_attempt[x] + Style.RESET_ALL
        print("Your progress: " + Progress.strip())
    # If an IndexError occurs, we will let the user retry the attempt
    except IndexError:
        print(f"Please enter a word that is {len(Level_word)} letters long")
        User_attempts = User_attempts - 1
    User_attempts = User_attempts + 1


    if Current_attempt == Level_word:
        print("Yes! the word was: " + Fore.GREEN + Level_word + Style.RESET_ALL)
        winner = True
        break

if(winner != True):
    print("You have used all of your attempts! The correct word was: " + Fore.GREEN + Level_word + Style.RESET_ALL)
