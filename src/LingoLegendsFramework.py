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
from WebPackage.pywebio.input import input
from WebPackage.pywebio.output import put_html, put_text
from WebPackage.pywebio import start_server


#This is the WebApp Function anything in here can/will be used on the front end of the website. For the time being most game functinos will be held here.
def WebApp():
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

    put_html(Styling)
    put_html("<h1 style='color: green;'>Lingo Legends</h1>")
    put_html("<h3>You will be given 5 attempts to guess the word (5 Letters) </h3>")
    
    Level_word = word_generator.generate_word_medium()


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
                    Progress += f"<span class='letter correct'>{Current_attempt[x]}</span>"
                elif Current_attempt[x] in Level_word:
                    Progress += f"<span class='letter present'>{Current_attempt[x]}</span>"
                else:
                    Progress += f"<span class='letter absent'>{Current_attempt[x]}</span>"
            put_html("<br><br>")
            put_html(f"<div class='progress'>{Progress.strip()}</div>")
        # If an IndexError occurs, we will let the user retry the attempt
        except IndexError:
            put_text("Please enter a word that is 5 letters long")
            User_attempts = User_attempts - 1
        User_attempts = User_attempts + 1


        if Current_attempt == Level_word:
            put_html(f"Yes! the word was: <span class='letter final'>{Level_word}</span>")
            winner = True
            break

    if(winner != True):
        put_html(f"You have used all of your attempts! The correct word was: <span class='letter final'>{Level_word}</span>")


#This is the init __main__ funcion. We are currently hosting this website on port 8000.
if __name__ == '__main__':
    start_server(WebApp, port=8000)
