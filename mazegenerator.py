#The program will be divided into two parts ,1 will be maze generating and the next will be maze solving

import random
import turtle

#adding all the element in the list
def list_sum(input):
    ans=0
    for rows in input:                                                                                 #I have assumed the notations of walls of each cell in list form as
        ans=ans+sum(rows)                                                                                       #node[1  ,1,  1,  1]
    return ans                                                                                        #mode_positions[left,top,right,bottom]

#used to generate the walls of maze

def maze_wall_generate(len_x,len_y):
    Walls=[[[1,1,1,1] for a in range(len_x)] for b in range(len_y)]
    x=0
    y=0
    total_visited=0
    currentnode=[x,y]
    visited=[[0 for a in range(len_x)] for b in range(len_y)]
    visited[x][y]=1
    visited_node_n=[[x,y]]
    n=0
    while total_visited!=(len_x*len_y):#check to see if finished
        options=[0,0,0,0]
        if x!=0:
            if visited[y][x-1]==0:
                options[0]=1
                #wall can be removed on the left
        if y!=len_y-1:
            if visited[y+1][x]==0:
                options[1]=1
                #wall can be removed above
        if x!=len_x-1:
            if visited[y][x+1]==0:
                options[2]=1
                #wall can be removed on the right
        if y!=0:
            if visited[y-1][x]==0:
                options[3]=1
                #wall can be removed below
        
        if options==[0,0,0,0]:
            currentnode=visited_node_n[n-1]
            x=currentnode[0]
            y=currentnode[1]
            n=n-1
            #moves back to previous square/node

        
        else:
         nodefound=False
         while nodefound==False:
                randomint=random.randint(0,3)
                if options[randomint]==1:
                    if randomint==0:
                        oppisitenode=[currentnode[0]-1,currentnode[1]]#moves into cell on the left
                        Walls[currentnode[1]][currentnode[0]][0]=0#removing wall left
                        Walls[oppisitenode[1]][oppisitenode[0]][2]=0
                    elif randomint==1:
                        oppisitenode=[currentnode[0],currentnode[1]+1]#moves into cell above
                        Walls[currentnode[1]][currentnode[0]][1]=0#removing wall above
                        Walls[oppisitenode[1]][oppisitenode[0]][3]=0
                    elif randomint==2:
                        oppisitenode=[currentnode[0]+1,currentnode[1]]#moves into cell on the right
                        Walls[currentnode[1]][currentnode[0]][2]=0#removing wall right
                        Walls[oppisitenode[1]][oppisitenode[0]][0]=0
                    else:
                        oppisitenode=[currentnode[0],currentnode[1]-1]#moves into cell below
                        Walls[currentnode[1]][currentnode[0]][3]=0#removing wall below
                        Walls[oppisitenode[1]][oppisitenode[0]][1]=0
                    n=n+1
                    visited_node_n.insert(n,oppisitenode)					
                    currentnode=oppisitenode					
                    visited[currentnode[1]][currentnode[0]]=1			
                    x=currentnode[0]							
                    y=currentnode[1]							
                    nodefound=True
        total_visited=list_sum(visited)
    return(Walls)

         
                    
def printmaze(sizex,sizey,Walls):
    startx=-380
    starty=-startx
    gridsize=(2*(-startx))/sizex
    turtle.clear()
    turtle.speed(0.005)
    turtle.penup()
    turtle.goto(startx,starty)
    turtle.pendown()
    turtle.goto(-startx,starty)
    turtle.goto(-startx,-starty)
    turtle.setheading(0)
    for y in range(sizex):
        turtle.penup()
        turtle.goto(startx,-starty+gridsize*(y))
        for x in range(sizey):
            if Walls[y][x][3]==1:
                turtle.pendown()
            else:
                turtle.penup()
            turtle.forward(gridsize)
    turtle.left(90)
    for x in range(sizex):
        turtle.penup()
        turtle.goto(startx+gridsize*(x),-starty)
        for y in range(sizey):
            if Walls[y][x][0]==1:
                turtle.pendown()
            else:
                turtle.penup()
            turtle.forward(gridsize)


#Main Program
sizex=10
sizey=10
Walls=maze_wall_generate(sizex,sizey)
print(Walls)
printmaze(sizex,sizey,Walls)

                   
                    
                   
                        
                       
