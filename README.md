# N-Queens
👑 A visualisation tool written in Python (using Pygame) to solve the famous N-Queens problem.

## Problem
The N Queen is the problem of placing N non-attacking chess queens on an N×N chessboard so that no two queens attack each other. 
Solutions exist for all natural numbers other than n=2 and n=3.

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

## Run the tool
To run the visualisation tool, type the following command in the terminal:
```
python backtracking.py
```

Source: https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
