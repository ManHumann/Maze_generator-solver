The program will be divided into two parts ,1 will be maze generating and the next will be maze solving.
The various approach which i will take will be uploaded as time passes.

Day 2:
I have added the portion where the walls of the two cells delete their respective walls in order to create a set path. There may be some errors in the code which will be looked at during post processing.

Day 3 & 4:
 The indexing of he lists were challenging ,as i had to go through hours of debugging,writing down the working of my loop in my note book.The python turtle module bit was done with the help of chat gpt.I got assisted on where to draw lines and how long to make those lines.Day 5 will now be dedicated on creaking an algorithm to solve the created maze,the concept of recursion will be used. 

Day5:
The back tracking algorithm was done,as it included checking the previous node ,and follwoing the way back,the onlu thing remaining is to print the final path of the maze,this also includes checking it the algorith works properly or not.This concludes the 75% progress of the project .

as the remaining 25% will include printing the path and debudding any error that may come along the way.


The working of the entire program is as follows"
Certainly! Let's break down the code into its main components, explaining the algorithm used and the data structures employed.

Maze Generation:

Algorithm:
1. The maze is generated using a recursive backtracking algorithm.
2. The maze is represented as a 2D grid of cells, each having four walls (left, top, right, bottom).
3. The algorithm starts at a random cell, marking it as visited.
4. It randomly chooses an unvisited neighboring cell, removes the wall between the current cell and the chosen cell, and repeats the process in the chosen cell.
5. If the current cell has no unvisited neighbors, the algorithm backtracks to the previous cell until all cells are visited.

Data Structures:
`Walls`: A 3D list representing the maze. Each cell has a list of four values indicating the presence (1) or absence (0) of walls in the left, top, right, and bottom directions.

`visited`: A 2D list tracking visited cells during maze generation.

`visited_node_n`: A list keeping track of the visited nodes during the generation process.

Maze Solving:

Algorithm:
1. The maze is solved using a breadth-first search algorithm.
2. The algorithm starts from the top-left corner and explores possible paths until it reaches the bottom-right corner.
3. It maintains a stack of nodes to explore, and at each step, it looks at the neighboring cells and adds unvisited, accessible cells to the stack.
4. The process continues until the bottom-right corner is reached.

Data Structures:
- `visited`: A 2D list indicating the distance from the start cell to each cell in the maze during the breadth-first search.

- `node_stack`: A stack of nodes to be explored during the search.

Turtle Graphics:

Drawing Functions:
`printmaze`: Draws the maze using Turtle graphics, considering the walls and paths.
`print_path`: Draws the solved path using Turtle graphics.
Overall Flow:

1. Maze generation using the recursive backtracking algorithm.
2. Drawing the generated maze using Turtle graphics.
3. Maze solving using breadth-first search.
4. Drawing the solved path using Turtle graphics.

The code combines maze generation, solving, and visualization using the Turtle library. It utilizes lists to represent the maze structure and track visited cells during generation and solving. The algorithms focus on exploring paths in the maze, either creating them during generation or finding the optimal path during solving. The Turtle graphics library facilitates visualizing the maze and solution on the screen.
