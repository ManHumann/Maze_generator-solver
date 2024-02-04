#The program will be divided into two parts ,1 will be maze generating and the next will be maze solving

import random
len_y=0
len_x=0
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
total_visited=0
current_node=[x,y]
visited=[]
for a in range(len_x):
    row=[]
    for b in range(len_y):
        row.append(0)
    current_node.append(row)

visited[x][y]=1
visited_node_n=[[x,y]]
n=0
while(total_visited!=(len_x*len_y)):
    
        options=[0,0,0,0]
        if (x!=0 and visited[y][x-1]==0):
            options[0]=1                        #wall in the left can be removed
        elif (x!=len_x - 1 and visited[y][x+1]==0):
            options[2]=1                        #wall in the right can be removed
        elif (y!=0 and visited[y-1][x]==0):
            options[1]=1                        #wall in the top can be removed                                 #Can generate error in the future
        elif (y!=len_y-1 and visited[y+1][x]==0):                                                                 #Can generate erroe in the future
            options[3]=1                         #wall in the bottom can be removed                              #Can generate error in the future
        elif options==[0,0,0,0]:
            current_node=visited_node_n[n-1]
            x=current_node[0]
            y=current_node[1]
            n=n-1
        else: