![Dr Mario Box Art](https://imgs.search.brave.com/IcQhtvQqG6IBTBruBMLQ1mkIUKirD7MBNvFL-2QW21A/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/Z2lhbnRib21iLmNv/bS9hL3VwbG9hZHMv/c3F1YXJlX3NtYWxs/LzkvOTM3NzAvMjM2/MTY4MC1uZXNfZHJt/YXJpby5qcGc "Classic NES Box Art")

# DR MARIO
Dr Mario is a falling block puzzle game released by Nintendo back in 1990 for the NES. Like Tetris, the game allows the user to move and rotate falling pieces to land in desired locations, but where these two games differ is their objectives. The goal of Tetris is to survive as long as possible by strategically filling the board to clear rows as the pieces start dropping faster and faster, meaning the player is competing against themselves or friends to reach highscores. Dr Mario approaches the genre with a new goal of eliminating enemies to progress to harder levels. These enemies, fittingly called viruses, randomly fill the board at the start of the game which wont end until they're all taken care of. 

---

## GAMEPLAY
The game gives you control two-colored pills tossed by Dr Mario into a pill bottle which acts as the game goard and your job is to navigate them to connect the corresponding pill color to each colored virus. At first glance Dr Mario might seem like an easier version of tetris because there are only 3 different pill colors, the pills don't vary in shape, you only need to connect 4 pieces to clear instead of a whole row, and you can clear both vertically and horizontally, but these changes do not make the game any easier. Each of these changes add complexity to the game and require the player to think on their feet because each game looks radically different from the last. Because the viruses stay in the same position throughout the game but each piece is still affected by gravity, the player can strategically place overhanging pills to cascade down and clear additional viruses when the supporting virus above is deleted. These gameplay features not only make the gameplay more interesting and complex, but also increases the technical difficulty to recreate.  

![Dr Mario Gameplay](https://imgs.search.brave.com/VdyNNE3ywgpCdZwaVjKRxhpzRPeeGUXz6cV2bkIHhdU/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/cmV0cm9nYW1lcy5j/ei9nYW1lcy8wNjEv/TkVTLWdhbWVwbGF5/LmdpZg.gif "High Level Gameplay")


---

## MOCK-TER DARIO
I've seen countless clones of Tetris online that people have made as coding practice, but I struggled to find any quality copies of Dr Mario. The projects I did find were either extremely simplified, had features removed to make it play more like tetris, or didn't work at all. I assumed this was because Dr Mario isn't as widespread as Tetris, but once I began making it myself I realized it is also a much more complicated game than Tetris. My goal with this project was not just to make another sub-par clone, but to duplicate the game as faithfully as possible including all original sprites, sounds, fonts, menus, random generation, and movement mechanics. Part of the challenge was not having the original source code, so I often found myself asking how to acheive the same result without knowing what was going on under the hood. It was a lot like creating a math formula only knowing the answer, there were many ways to acheive the same thing, but could I do it with the tools I had in a semi-efficient way? I am happy with the results of the project so far, but there is still much optimizing to be done. I wanted to first get a working game before trimming the fat because "premature optimization is the root of all evil" and it doesn't matter how fast a program runs if it doesn't run.

---

## CONTROLS
Player 1
+ W: rotate counter-clockwise
+ A: move left
+ S: move down
+ D: move right

Player 2
+ UP: rotate counter-clockwise
+ LEFT: move left
+ DOWN: move down
+ RIGHT: move right
  
General
+ ENTER: forward through menus
+ ESCAPE: back through menus / close game
+ SPACE: pause game (not implemented yet)
  
---

## TO DO
Gameplay Features
+ Add level win conditions
+ Add top-out lose condition
+ Add virus level, count, and score indicators in 1-player mode
+ Add best of 5 win condition in 2-player mode
+ Show the 'sprite clear' circles where pieces were just removed when the clear sound plays
+ Animate viruses
+ Randomly seed a list of pill pieces for both players to have the same pill order
+ Add a preview of the next pill incoming
+ Randomly seed a list for the viruses so both players have mirrored boards
+ Create conditions so viruses can never spawn 4 in a row
+ Ability to pause the game
+ Clockwise rotation (was in before, but couldn't find intuitive controls)
+ Possible controller compatibility

Bugs
+ In certain conditions the rotation button will kick the piece left without spinning it
+ Invisible blocks stop falling pieces on occasion
+ Pressing down at the right time can push the pill into occupied spaces
+ Possibility that menu screens are still running after proceeding to the next view
+ Falling blocks can clear lines before landing

Optimizations
+ Would like to consolidate actions like collision detection and dropping pieces into functions
+ Possible refactoring needed to eliminate unnessecary checks in the game loop
+ Falling blocks are too slow and staggered, should all fall together
