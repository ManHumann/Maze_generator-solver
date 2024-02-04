#The program will be divided into two parts ,1 will be maze generating and the next will be maze solving

import random

#adding all the element in the list
def list_sum(input):
    ans=0
    for rows in input:
        ans=ans+sum(rows)
    return ans

#used to generate the walls of maze

def maze_wall_generate(len_x,len_y):
    walls=[]
    for a in range(len_x):
        row=[]
        for b in range(len_y):
            cell=[1,1,1,1]
            row.append[cell]
    walls.append(row)
x=0
y=0
current_node=[x,y]

            