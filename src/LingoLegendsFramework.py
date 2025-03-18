"""
TODO:
-Implement API [Done]
-Develop Difficulty System []
    - Create variable for user global progress and grab word from API. Implementation Depends on API or Library Used.
- Catch Errors for users submitting words that are smaller. [Done]
-Implement PyWebUi [Done]
"""

import random
import word_generator
#Only importing needed functions from PyWebIO in the future we can import all depedning on efficency of program.
from WebPackage.pywebio.input import input
from WebPackage.pywebio.output import put_html, put_text, clear
from WebPackage.pywebio import start_server

Styling = """
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-family: Arial, sans-serif;
            height: 100vh;
            text-align: center;
        }
        .letter {
            display: inline-block;
            padding: 30px;
            font-size: 24px;
            font-weight: bold;
            color: white;
            border-radius: 4px;
        }
        .correct {
            background-color: green;
            padding: 30px;
        }
        .present {
            background-color: yellow;
        }
        .final {
            background-color: green;
            padding: 5px;
        }
        .absent {
            background-color: gray;
        }
        .progress {
            display: flex;
            justify-content: center;
            padding-bottom: 60px;
        }
    </style>
    """
#Function to greet the user, instead of copying code over and over
def greeting():
    put_html(Styling)
    put_html("<h1 style='color: green;'>Lingo Legends</h1>")
    put_html("<h3>You will be given 5 attempts to guess words. If you do not guess a word within the given, the game will end.</h3>")

# This is the WebApp Function anything in here can/will be used on the front end of the website.
def WebApp():
    rounds = 5
    current_round = 1
    game_over = False 
    Round_Words = []
    greeting()
    #New Loop to allow 5 words, can implement difficulty system soon. Rounds can be changed.
    while current_round <= rounds and not game_over: 
        
        put_html(f"<h3>Round {current_round} of {rounds}</h3>")
        
        Level_word = word_generator.generate_word_medium()
        Round_Words.append(Level_word)
        #For time being word is displayed for testing.
        put_html(f"Word: {Level_word}") 

        winner = False  
        User_attempts = 0
        while User_attempts < 5:
            Current_attempt = input(f"Guess {str(User_attempts + 1)} >>").lower()

            Progress = ""
            try:
                for x in range(len(Level_word)):
                    if Current_attempt[x] == Level_word[x]:
                        Progress += f"<span class='letter correct'>{Current_attempt[x]}</span>"
                    elif Current_attempt[x] in Level_word:
                        Progress += f"<span class='letter present'>{Current_attempt[x]}</span>"
                    else:
                        Progress += f"<span class='letter absent'>{Current_attempt[x]}</span>"
                
                put_html("<br><br>")
                put_html(f"<div class='progress'>{Progress.strip()}</div>")
            except IndexError:
                put_text("Please enter a word that is 5 letters long")
                User_attempts -= 1  

            User_attempts += 1

            # Check if the user has guessed the word correctly
            if Current_attempt == Level_word:
                put_html(f"Yes! The word was: <span class='letter final'>{Level_word}</span>")
                #Clear is used in the following two functions so that the user only sees the current round they are on.
                clear()
                greeting()
                winner = True
                break

        if not winner:
            put_html(f"You have used all of your attempts for this round! The correct word was: <span class='letter final'>{Level_word}</span>")
            clear()
            put_html(Styling)
            game_over = True  
        else:
            current_round += 1

    if current_round > rounds:  
        put_html("<h2>Congratulations! You've completed the game!</h2>")
        put_html("<h1>Words used this round:</h1>")
        for x in range(len(Round_Words)):
            put_html(f"<h3>Round {str(x + 1)}: {Round_Words[x]}</h3>")
    else: 
        put_html("<h2>Game Over! Try again next time!</h2>")

        put_html("<h1>Words used this round:</h1>")
        for x in range(len(Round_Words)):
            put_html(f"<h3>Round {str(x + 1)}: {Round_Words[x]}</h3>")
        

# This is the init __main__ function. We are currently hosting this website on port 8000.
if __name__ == '__main__':
    start_server(WebApp, port=8000)

