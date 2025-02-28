# Overview
This markdown document serves as our Software Requirment Specification System. Using an SRS will allow us to manage our different features/requirements for Lingo Legends.
As shown below are our functional requirements (Features / User Interaction) and Non-Functional Requirements(Performance / Standards).

# Functional Requirements
1. R1: Home Screen Shall be displayed when going to locally hosted website
    1. R1.1: Game level shall be displayed when the Play button is selected on the home screen
    2. R1.2: Leaderboard page shall be displayed when Leaderbord button is selected on home screen
2. R2: A game word shall be picked from the WonderWords api before each round according to user's difficulty level
    1. R2.1: Each level's difficulty shall be set based upon a users progress.
        1. R2.1.1: Each round (3 words) shall be given x (start with 6) number of attempts with word length increasing for each level of round
        2. R2.1.2: Upon completion of a round, the user shall be passed to the next. However; user will have x-1 attempts
        3. R2.1.3: Upon completion of  round 3 (7 letter, 4 attempts) user shall be marked a winner of LingoLegends
    2. R2.2: Length of game word shall be picked based upon difficulty level
    3. R2.3: User shall only be given a set amount of attempts according to their difficulty level
    4. R2.4: Previously attempted words shall be stored in array to ensure repeaded words are not chosen.
3. R3: When a User does not guess word within given attempts for round, score shall be displayed while asking for intials for leaderboard.
4. R4: Scores shall be kept based upon a users progression through game.
    1. R4.1: Depending on n attempts to guess each level will be scored upon the formula: 1000 / 2^n. n being the number of attempts.
    2. R4.2: Initials shall be kept for displaying leaderboard

# Non-Functional Requirements
1. <Name of Feature 1>
    1. <Non-Functional Requirement 1>
    2. <Non-Functional Requirement 2>
2. <And so on>