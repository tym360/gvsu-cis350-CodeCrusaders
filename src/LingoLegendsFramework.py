import time
import word_generator
from WebPackage.pywebio.input import input
from WebPackage.pywebio.output import put_html, put_text, clear
from WebPackage.pywebio import start_server
from WebPackage.pywebio.input import actions
"""
TODO:
"""
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
    div#pywebio-scope-ROOT {
        text-align: center;
    }
    </style>
"""

def greeting(level):
    put_html(Styling)
    put_html("<h1 style='color: green;'>Lingo Legends</h1>")
    put_html("<h3>You will be given 5 attempts to guess each word.</h3>")
    put_html(f"<h2>Level {level} of 5 Levels</h2>")


def play_level(current_level):
    rounds = 5
    current_round = 1
    round_over = False
    Round_Words = []
    RoundPoints = 0

    greeting(current_level)

    while current_round <= rounds and not round_over: 
        put_html(f"<h3>Word {current_round} of {rounds}</h3>")

        Level_word = word_generator.generate_word(current_level)
        Round_Words.append(Level_word)
        put_html(f"<h3>Amount of Letters {len(Level_word)}</h3>")
        put_html(f"Word: {Level_word}") 

        winner = False  
        User_attempts = 0

        while User_attempts < 5:
            Current_attempt = input(f"Guess {str(User_attempts + 1)} >>").lower()

            if len(Current_attempt) != len(Level_word):
                put_text(f"Please enter a {len(Level_word)}-letter word")
                continue

            Progress = ""
            for x in range(len(Level_word)):
                if Current_attempt[x] == Level_word[x]:
                    Progress += f"<span class='letter correct'>{Current_attempt[x]}</span>"
                elif Current_attempt[x] in Level_word:
                    Progress += f"<span class='letter present'>{Current_attempt[x]}</span>"
                else:
                    Progress += f"<span class='letter absent'>{Current_attempt[x]}</span>"

            put_html("<br><br>")
            put_html(f"<div class='progress'>{Progress.strip()}</div>")

            User_attempts += 1

            if Current_attempt == Level_word:
                WordPoints = ((500 // (rounds / 5)) // 2**User_attempts)
                RoundPoints += WordPoints
                put_html(f"Yes! The word was: <span class='letter final'>{Level_word}</span>")
                put_html(f"Current Round Points: {int(RoundPoints)}")
                time.sleep(2)
                clear()
                greeting(current_level)
                winner = True
                break

        current_round, round_over = end_round(Round_Words, RoundPoints, current_round, rounds, winner)

    return RoundPoints, Round_Words, round_over

def end_round(Round_Words, RoundPoints, current_round, rounds, winner):
    round_over = False

    if not winner:
        put_html(f"You've used all your attempts! The word was: <span class='letter final'>{Round_Words[-1]}</span>")
        round_over = True
    else:
        current_round += 1

    return current_round, round_over
def ShowLeaderboard():
    clear()
    put_html(Styling)
    
    with open("scores.txt", "r") as file:
        lines = file.readlines()

    scores = {}
        
    for line in lines:
        if ',' in line:
            name, score = line.strip().split(',')
            score = int(score)
            #Check for Duplicate Usernames and update score if higher.    
            if name in scores:
                if scores[name] < score:
                    scores[name] = score
            else:
                scores[name] = score
    #Sort scores asyncronously.
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for idx, (name, score) in enumerate(sorted_scores[:10], start=1):
        put_html(f"<h4>{idx}. {name} - {score} pts</h4>")

    result = actions('', buttons=[{'label': 'Back to Start', 'value': 'back'}])
    clear()
    if result == 'back':
        MainMenu()

def MainMenu():
    put_html(Styling)


    put_html("<h1 style='color: green;'>Welcome to Lingo Legends!</h1>")
    put_html("<h3>This is a 5-level word guessing game. Try to guess the word in 5 attempts!</h3>")
    put_html("<h4>Click below when you're ready to start.</h4>")

    result = actions('', buttons=[
        {'label': 'Start Game', 'value': 'start'},
        {'label': 'Leaderboard', 'value': 'leaderboard'}
    ])

    clear()
    if result == 'leaderboard':
        ShowLeaderboard()

def PostScore(total_score, total_words):
    name = input("Enter your name to post your score:")
    with open("scores.txt", "a") as file:
        file.write(f"{name},{int(total_score)}\n")
    AfterPostScore = actions('', buttons=[{'label': 'View Words', 'value': 'ViewWords'}, {'label': 'Play Again', 'value': 'PlayAgain'}])
    if AfterPostScore == 'PlayAgain':
        put_html("<script>location.reload()</script>")
        return
    if AfterPostScore == 'ViewWords':
        ViewWords(total_words)

    clear()
def ViewWords(total_words):
    put_html("<h3 class='final'>All Words Used:</h3>")
    #DIsplay all words used in the game
    for i, word in enumerate(total_words):
        put_html(f"<h4>{i+1}. {word}</h4>")
    AfterViewWords = actions('', buttons=[{'label': 'Play Again', 'value': 'PlayAgain'}])
    if AfterViewWords == 'PlayAgain':
        put_html("<script>location.reload()</script>")
        return

        
def WebApp():
    while True:
        MainMenu()
        total_score = 0
        total_words = []
        total_rounds = 5

        for round_number in range(1, total_rounds + 1):
            clear()
            score, words, failed = play_level(round_number) 

            total_score += score
            total_words.extend(words)

            if failed:
                clear()
                put_html("<h2>Game Over!</h2>")
                put_html(f"<h3>Round {round_number} Score: <i>{score}</i></h3>")
                put_html(f"<h3>Total Score: <i>{total_score}</i></h3>")
                put_html("<h3>Words Used This Round:</h3>")

                AfterFail = actions('', buttons=[
                    {'label': 'Post Score to Leaderboard?', 'value': 'PostScore'},
                    {'label': 'Play Again', 'value': 'PlayAgain'},
                    {'label': 'View Words', 'value': 'ViewWords'}
                ])
                if AfterFail == 'PostScore':
                    PostScore(total_score, total_words)
                if AfterFail == 'PlayAgain':
                    put_html("<script>location.reload()</script>")
                    return
                if AfterFail == 'ViewWords':
                    ViewWords(total_words)
                return  

        else:
            clear()
            put_html("<h2 class='final'>Thanks for playing Lingo Legends!</h2>")
            put_html(f"<h3 class='final'>Final Score: <i>{int(total_score)}</i></h3>")
            PostScoreButton = actions('', buttons=[
                {'label': 'Post Score to Leaderboard?', 'value': 'PostScore'},
                {'label': 'View Words', 'value': 'ViewWords'},
                {'label': 'Play Again', 'value': 'PlayAgain'}
            ])
            if PostScoreButton == 'PostScore':
                PostScore(total_score, total_words)
            if PostScoreButton == 'ViewWords':
                ViewWords(total_words)
            if PostScoreButton == 'PlayAgain':
                put_html("<script>location.reload()</script>")
                return
            return



if __name__ == '__main__':
    start_server(WebApp, port=8000)
