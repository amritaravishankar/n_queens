# 👑 N-Queens
A visualisation tool written in Python (using Pygame) to solve the famous N-Queens problem.

## Problem
The N Queen is the problem of placing N non-attacking chess queens on an N×N chessboard so that no two queens attack each other. 
Solutions exist for all natural numbers other than n=2 and n=3.

<img src="https://github.com/amritaravishankar/n_queens/blob/master/queen.jpg?raw=true" width="250">

## Psuedocode
```
while there are untried configurations
{
   generate the next configuration
   if queens don't attack in this configuration then
   {
      print this configuration;
   }
}
```
## Visualisation Tool
### A screenshot of the tool in progress
The red boxes represent the spaces that cannot have a queen.
<br>
<img src="https://github.com/amritaravishankar/n_queens/blob/master/screenshots/progress.png" width="250">
                                                                                                     
### The tool's final outcome
<img src="https://github.com/amritaravishankar/n_queens/blob/master/screenshots/final.png" width="250">

## Run the tool
To run the visualisation tool, type the following command in the terminal:
```
python backtracking.py
```

## Reference 
https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
