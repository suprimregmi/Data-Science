#mthod 1
# import random
#
# def random_walk(n):
#     """:return co-ordinates aftere 'n' block  random walk"""
#
#     x=0
#     y=0
#
#     for i in range(n):
#         step=random.choice(['N','S','E','W'])
#         if step=='N':
#             y=y+1
#         elif step=='S':
#             y=y-1
#         elif step=='E':
#             x=x+1
#         else:
#             x=x-1
#     return(x,y) #the walk is over at this point so we have returned tuple
#
# for i in range(25):
#     walk=random_walk(10)   #if it walks each 10 blocks long
#     print((walk,"Distance from home=",
#            abs(walk[0]+abs(walk[1]))) #displaying coordinates and distance from home for each walk
#
#
#
# print("ended")


#Method 2


import  random
def random_walk_2(n):
    """return coordinates after 'n' block random walk"""

    x,y=0,0  #initialize

    for i in range(n):  #simulationg n blocks
        (dx,dy)=random.choice([(0,1),(0,-1),(1,0),(-1,0)]) #randomly choosing pair of number ,difference in x & y
        # choosing N=x-cord=0,y increases and so on
        #updating values
        x+=dx
        y+=dy
    return (x,y)

for i in range(25):  #taking 25 random walk.Each walk 10 blocks
    walk=random_walk_2(10)   #if it walks each 10 blocks long
    print((walk,"Distance from home=",
           abs(walk[0]+abs(walk[1]))))  #displaying final coordinates and distance from home for each walk

'''puzzle.
What is the longest random walk you can take so that on avg you will end up 4 blocks or fewer from home?

using monty carlo method

here we compute 1000s of trial and compute
'''


total_walks=1200

for walk_length in range(1,31):
    no_transport=0  #creating couter for walk less than 4 block from home
    for i in range(total_walks):
        (x,y)=random_walk_2(walk_length)
        distance=abs(x)+abs(y)
        if distance <=4:
            no_transport+=1  #increment no counter
    no_transport_percentage=float(no_transport/total_walks)
    print('walk size=',walk_length, "% of no of transport= ",100*no_transport_percentage)




