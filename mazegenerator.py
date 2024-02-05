#The program will be divided into two parts ,1 will be maze generating and the next will be maze solving

import random
len_y=0
len_x=0
walls=[]
#adding all the element in the list
def list_sum(input):
    ans=0
    for rows in input:                                                                                 #I have assumed the notations of walls of each cell in list form as
        ans=ans+sum(rows)                                                                                       #node[1  ,1,  1,  1]
    return ans                                                                                        #mode_positions[left,top,right,bottom]

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
    visited=[[[0 for a in range(len_x)] for b in range(len_y)]]
    #for a in range(len_x):
   # row=[]                              #first initilize every block of list as unvisited or 0
   # for b in range(len_y):
   #     row.append(0)
   # current_node.append(row)

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
            y=current_node[1]                      #moves back to the previous node
            n=n-1
        
        else:
            nodefound=False
            while nodefound==False:
                random_int=random.randint(0,3)
                
                if options[random_int]==1:
                    
                     if random_int==0:
                       opposite_node=[current_node[0]-1,current_node[1]]            #moves to the cell left of current node
                       walls[current_node[1],current_node[0]][0]=0                  #deletes the left wall of current node
                       walls[opposite_node[1],current_node[0]][2]=0                 #deletes the right wall of the oppossite node

                     elif random_int==1:
                         opposite_node=[current_node[0],current_node[1]-1]          #moves to the node above
                         walls[current_node[1],current_node[0]][1]=0                #removes the top wall of the current node
                         walls[opposite_node[1],opposite_node[0]][3]=0              #removes the bottom part of the current node

                     elif random_int==2:
                         opposite_node=[current_node[0]+1,current_node[1]]
                         walls[current_node[1],current_node[0]][2]=0
                         walls[opposite_node[1],opposite_node[0]][0]=0

                     else :
                            random_int==3
                            opposite_node=[current_node[0],current_node[1]+1]
                            walls[current_node[1],current_node[0]][3]=0
                            walls[opposite_node[1],opposite_node[0]][1]=0
                n=n+1
                visited_node_n.insert(n,opposite_node)
                current_node=opposite_node
                visited[current_node[1]][current_node[0]]=1
                x=current_node[0]
                y=current_node[1]
                nodefound=True
            total_visited=list_sum(visited)
    return(walls)          
                    
                    
                    
                   
                        
                       
