import pygame
import mazeclass

# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size=[1000,500]
screen=pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("Maze Project")

# Get a new maze
mazegrid =  [[2,2,2,2,2,2,2,2,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
             [2,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,2],
             [2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,2],
             [2,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,2],
             [2,0,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,2],
             [2,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,2],
             [2,0,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,2],
             [2,0,1,0,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,2],
             [2,0,1,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,2],
             [2,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,2],
             [2,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,2],
             [2,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,2],
             [2,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,2],
             [2,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,0,2],
             [2,0,1,0,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,2],
             [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

testgrid = [[2,2,2,2,2,2,2,2],
            [2,0,0,0,0,0,5,2],
            [2,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,2],
            [2,0,0,0,0,0,0,2],
            [2,2,2,2,2,2,2,2],]

the_maze = mazeclass.Maze(mazegrid)
# the_maze = mazeclass.Maze(testgrid)

##########################################################
def forwardbackward(curpos):
    # Warm up at the current position
    moveto(curpos, 3)
    moveto(curpos, 3)
    # Look for positions that can be visited
    neighbourlist = unvisitedneighbours(curpos)    
    if neighbourlist != []:        
        # Select the first position that can be visited
        newpos = neighbourlist[0]      
        # Go to that position
        moveto(newpos, 3)
        # Warm up at the new position
        moveto(newpos, 4)
        # Move back
        moveto(curpos, 4)

def unvisitedneighbours(curpos, acceptableValues=[0]):
    # Return list of positions that meet criteria in acceptableValues and are neighbour to current position
    x = curpos[0]
    y = curpos[1]
    free = []
    for newpos in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0 <= newpos[0] < the_maze.rows and 0 <= newpos[1] < the_maze.columns:
                if the_maze.grid[newpos[0]][newpos[1]].status in acceptableValues: 
                    free.append(newpos)     
    return free

def moveto(newpos, status, movebot=True):
    # Mark the new position as being visited
    the_maze.grid[newpos[0]][newpos[1]].status = status
    # If required, move to the new position
    if movebot:
        the_maze.bot_xcoord = newpos[0]
        the_maze.bot_ycoord = newpos[1]
    # Wait a bit and then display the current state of the maze
    # pygame.time.delay(300)
    the_maze.display_maze(screen)
    pygame.display.flip()
    pygame.event.pump()
    
# Code to be implemented
def dft(newpos):
    moveto(newpos, 3)

    neighbours = unvisitedneighbours(newpos)
    for neighbour in neighbours:
        dft(neighbour)
        moveto(newpos, 4)

def dfs(newpos):
    if the_maze.grid[newpos[0]][newpos[1]].status == 5:
        moveto(newpos, 3)
        return True

    moveto(newpos, 3)
    neighbours = unvisitedneighbours(newpos, [0,5])
    for neighbour in neighbours:
        if not dfs(neighbour): # didn't find exit
            moveto(newpos, 4)
        else:
            return True

def depthfirsttraversal(curpos):
    # Do a depth-first traversal of all unvisited neighbours
    dft(curpos)

    # return to the starting position
    moveto(curpos, 4)

def depthfirstsearch(curpos):
    # Perform a depth-first search to find the exit
    dfs(curpos)

def breadthfirstsearch(curpos):
    # Perform a breadth-first search to find the exit
    pos = curpos 
    q = [] 
    parent = {}
    
    # put init values on queue
    for neighbour in unvisitedneighbours(pos):
        parent[neighbour] = pos 
        q.append(neighbour)
        
    while q:
        pos = q.pop(0)
        moveto(pos, 3, False)
        
        for neighbour in unvisitedneighbours(pos, [0,5]):
            if the_maze.grid[neighbour[0]][neighbour[1]].status == 5:
                parent[neighbour] = pos 
    #            print("Found Exit at", neighbour, "from", pos)
                pos = neighbour
                q = 0 # break out of both loops
                break
            else:
                q.append(neighbour)
                parent[neighbour] = pos 

    # build path
    path = []
    while pos != curpos:
        path.append(pos)
        pos = parent[pos]

    for val in reversed(path):
        moveto(val, 4)

# Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while done==False:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN: # If user wants to perform an action
                if event.key == pygame.K_q:
                    quit()
                if event.key == pygame.K_f:
                    the_maze.reset(mazegrid)
                    forwardbackward((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_t:
                    the_maze.reset(mazegrid)
                    depthfirsttraversal((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_d:
                    the_maze.reset(mazegrid)
                    depthfirstsearch((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_b:
                    the_maze.reset(mazegrid)
                    breadthfirstsearch((the_maze.bot_xcoord, the_maze.bot_ycoord))
                         
        the_maze.display_maze(screen)
        # Limit to 50 frames per second
        clock.tick(50)
 
        # update the screen with what we've drawn.
        pygame.display.flip()
     
pygame.quit()
