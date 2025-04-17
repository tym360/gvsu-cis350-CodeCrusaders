# Overview
This document is serving as our final checklist and validation tool, it helps us confirm that we actually built what all 4 of us orignally agreed to, with some minor changes. This allows us to go back through and make sure each of our features stated are working as described. Allowing all who are interested in our game to understand the intentions behind our software used.

# Software Requirements
Below serves as our Software Requirment Specification System. Using an SRS will allow us to manage our different features/requirements for Lingo Legends. As shown below are our functional requirements (Features / User Interaction) and Non-Functional Requirements(Performance / Standards).

## Functional Requirements
### Home screen
| ID | Navigation and Interface |
| :-------------: | :----------: |
| FR1 | Home screen shall be displayed when going to locally hosted website. |
| FR2 | Game level shall be displayed when the play button is selected on the home screen. |
| FR3 | Leaderboard page shall be displayed when leaderboard button is selected on the home or game over screen|
| FR4 | User shall have the ability to access leaderboards and other features continuously without refreshing website|
| FR5 | Game will stop running when close button is pressed. |
### Gameplay
| ID | Game Mechanics |
| :-------------: | :----------: |
| FR6 | Each level's difficulty shall be set based upon a user's progress |
| FR7 | A game word shall be picked from the WonderWords API before each round according to user's difficulty level |
| FR8 | Previously attempted words shall be stored in an array to prevent repeats. |
| FR9 | When a user fails to guess the word within 5 attemps the game over screen shall be shown|
| FR10 | Users shall be told correct word for failing attempt. |
### User Incentives
| ID | Scoring and Leaderboard |
| :-------------: | :----------: |
| FR11 | When a user does not guess  word within given attempts for round, score shall be displayed while asking for name for leaderboard |
| FR12 | Player shall have the choice to play again without posting score to public scoreboard |
| FR13 | For each word a player shall be assigned points following this formula ((500 // (rounds / 5)) // 2**User_attempts)|
| FR14 | Scores shall be kept based upon a users progression through the game. |
| FR15 | Upon completetion of a round, the user shall be passed to the next round with x-1 attempts. |

## Non-Functional Requirements
### Screen Displays
| ID | Accessibility |
| :-------------: | :----------: |
| NFR1 | The game interface shall provide clear visual feedback after each guess. |
| NFR2 | All the game instruction and labels shall use simple, beginner-freindly language. |
| NFR3 | Lingo Legends shall have appropriate difficulty accellaration to tend to multiple audiences. |
| NFR4 | Leaderboard shall be accessible using a screen reader for vision impared individuals. |
| NFR5 | Lingo Legends shall not prematurely timeout |
### Processing time
| ID | Performance and Reliability |
| :-------------: | :----------: |
| NFR6  | Game word retrieval from the wonderwords API shall take no longer than 2 seconds. |
| NFR7  | The game shall respond to a user's guess input in under a second. |
| NFR8  | If the API fails, the system shall fall back to a local word list to continue gameplay. |
| NFR9  | Attempts and game state shall persist in memory without loss until the session ends. |
| NFR10 | Leaderboard shall filter and display results in no longer than 1.5 seconds. |
### Scalability
| ID | Maintainability |
| :-------------: | :----------: |
| NFR11 | The Python codebase shall follow PEP8 coding standards for readability |
| NFR12 | The application shall log errors such as API failures to a debug file for us to review. |
| NFR13 | Game configuration shall be stored in a seperate function for easy access and editing. |
| NFR14 | Word generation shall be configured seperately to allow easy access for debugging. |
| NFR15 | Game over screen shall dynamically display words used screen incase extra rounds/modes are added in future. |

# Software Artifacts
Linked below are three different software artifacts that visually shows how our program works technically and with our user. The Use Case diagram shows the different interactions a user may have with our game. While, the Sequence Diagram shows how our different classes work with eachother and the user. Finally, the Class Diagram is a technical representation that shows our different classes and how they interact with each other. 

* [Use Case Diagram](https://github.com/tym360/gvsu-cis350-CodeCrusaders/blob/main/artifacts/use_case_diagram/UseCaseDiagram.png)
* [Class Diagram](https://github.com/tym360/gvsu-cis350-CodeCrusaders/blob/main/artifacts/LingoLegendsUML.pdf)
* [Sequence Diagram](https://github.com/tym360/gvsu-cis350-CodeCrusaders/blob/main/artifacts/LingoLegendsSequenceDiagram.pdf)