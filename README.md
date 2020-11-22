Noughts and Crosses game
The user is pitted against the computer in an intense round of Noughts and Crosses (Tic Tac Toe). Some assumptions made: User is always crosses (x). The user goes first. As long as the game is not full, the user is prompted to choose where to place an x by entering a number between 1-9. Explicitly shown:
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
User is reprompted for bad input (!int) or if the space already has a x or o in it.
After the user, the computer gets to move. Instead of random, the computer move is written in a way to attempt to stop a user victory, or to defeat the user.
First the computer will check if the user is about to win, then place an o into that square. 
If not, the computer will look for available squares in the corners and take a random corner.
If not, the computer will check if the square in the middle is available.
Then the computer will look for available squares in the edges and choose a random one.
