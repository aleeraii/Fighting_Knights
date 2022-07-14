#  Battling Knights

### Introduction:
This is a 8x8 board game where four knights fight with each other for survival. The knights can pick the items on the ground and 
those items will be set free if the knight gets killed or drown. 

<b> Input: </b>
<li> A file named <i>moves.txt</i> is read by the program. The file contains the movements of the knights in the board.
The file should start with first line as <b>GAME-START</b> Below is the sample format for the file:

```
GAME-START
R:S
R:S
B:E
G:N
Y:N
GAME-END
````

<b> Output:</b>
<br> The output is a file named as `final_state.json`. The file contains information in below-mentioned format:

```
 "red": [<R position>,<R status>,<R item (null if no item)>,R Attack,<R Defence>],
 "blue": [<B position>,<B status>,<B item (null if no item)>,B Attack,<B Defence>],
 "green": [<G position>,<G status>,<G item (null if no item)>,G Attack,<G Defence>],
 "yellow": [<Y position>,<Y status>,<Y item (null if no item)>,Y Attack,<Y Defence>],
 "magic_staff": [<M position>,<M equipped>],
 "helmet": [<H position>,<H equipped>],
 "dagger": [<D position>,<D equipped>],
 "axe": [<A position>,<A equipped>],
}
```

Here is a sample output file:

```
{
    "red": [[2, 0], "LIVE", 1, 1], 
    "blue": [[7, 1], "LIVE", 1, 1], 
    "green": [[6, 7], "LIVE", 1, 1], 
    "yellow": [[0, 0], "DROWNED", 0, 0], 
    "magic_staff": [[5, 2], false], 
    "helmet": [[5, 5], false], 
    "dagger": [[2, 5], false], 
    "axe": [[2, 2], false]
}
```

### Instructions to execute code:
Follow below-mentioned steps to execute the code:
<li> Create a .txt file named moves.txt in the sample format given above
<li> Make sure the moves.txt file is at the same directory level as the game.py
<li> Execute the python program by using this command 

```
python game.py
```

<li> You can see the results in the output file named as final_state.json
<li> To run the test cases execute below command:

```
python -m unittest -v tests
```

<br><br><br><br>

