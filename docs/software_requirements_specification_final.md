# Overview
This document is serving as our final checklist and validation tool, it helps us confirm that we actually built what all 4 of us orignally agreed to, with some minor changes. This allows us to go back through and make sure each of our features stated are working as described. Allowing all who are interested in our game to understand the intentions behind our software used.

# Software Requirements
<Describe the structure of this section>

## Functional Requirements
### <Home screen>
| ID | Navigation and Interface |
| :-------------: | :----------: |
| FR1 | Home screen shall be displayed when going to locally hosted website. |
| FR2 | Game level shall be displayed when the play button is selected on the home screen. |
| FR3 | Leaderboard page shall be displayed when leaderboard button is selected on Home Screen |
| FR4 | Lingo Legends shall have background music that can be toggled on and off |
| FR5 | Game will stop running when close button is pressed. |
### <Gameplay>
| ID | Game Mehanics |
| :-------------: | :----------: |
| FR6 | Each level's difficulty shall be set based upon a user's progress |
| FR7 | A game word shall be picked from the WonderWords API before each round according to user's difficulty level |
| FR8 | Previously attempted words shall be stored in an array to prevent repeats. |
| FR9 | Users will be told correct letters for incorrect words. |
| FR10 | … |
### <User Incentives>
| ID | Scoring and Leaderboard |
| :-------------: | :----------: |
| FR11 | When a user does not guess  word within given attempts for round, score shall be displayed while asking for intitials for leaderboard |
| FR12 | Scores shal be kept based upon a users progression through the game. |
| FR13 | Upon completetion of a round, the user shall be passed to the next round with x-1 attempts. |
| FR14 | … |
| FR15 | … |

## Non-Functional Requirements
### <Screen Displays>
| ID | Accessibility |
| :-------------: | :----------: |
| NFR1 | The game interface shall provide clear visual feedback after each guess. |
| NFR2 |  All the game instruction and labels shall use simple, beginner-freindly language. |
| NFR3 |  The toggle for background music shall be visible and easily accessible from any game screen. |
| NFR4 | … |
| NFR5 | … |
### <Processing time>
| ID | Performance and Reliability |
| :-------------: | :----------: |
| NFR6  | Game word retrieval from the wonderwords API shall take no longer than 2 seconds. |
| NFR7  |  The game shall respond to a user's guess input in under a second. |
| NFR8  |  If the API fails, the system shall fall back to a local word list to continue gameplay. |
| NFR9  | Attempts and game state shall persist in memory without loss until the session ends. |
| NFR10 | … |
### <Scalability>
| ID | Maintainability |
| :-------------: | :----------: |
| NFR11 | The Python codebase shall follow PEP8 coding standards for readability |
| NFR12 |  The application shall log errors such as API failures to a debug file for us to review. |
| NFR13 |  Game configuration shall be stored in a seperate cofiguration file for easy access and editing. |
| NFR14 | … |
| NFR15 | … |

# Software Artifacts
<Describe the purpose of this section>

* [Use Case Diagram](https://github.com/tym360/gvsu-cis350-CodeCrusaders/blob/main/artifacts/use_case_diagram/UseCaseDiagram.png)
* [Class Diagram](https://github.com/tym360/gvsu-cis350-CodeCrusaders/blob/main/artifacts/LingoLegendsUML.pdf)
* [Sequence Diagram](https://github.com/tym360/gvsu-cis350-CodeCrusaders/blob/main/artifacts/LingoLegendsSequenceDiagram.pdf)