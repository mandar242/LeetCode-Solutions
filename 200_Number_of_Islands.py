"""
BASIS idea here is to count total number of areas of all connected 1's
we can do this by either DFS or BFS 
here we will do following steps to solve this problem - >
1.iterate over each matrix element eg. grid[0][0]
2.check if it is 1, if yes then change it to 0, 
  then using DFS go to its left, right, up, down  and convert all the 1's to 0's
3. once all the connected 1's are turned to 0's return number of islands as 1
NOTE: Changing connected 1's to 0's can be imagined similar to sinking a part of an islnad. 
      So once all parts of an island are sunk we can return that 1 islnad has been sunked.
4. add this island to total_number of islands and keep iterating until no 1's remain.

# we can further reduce the space by using BFS instead.

TIME - O ( M * N ) SPACE - O( M * N ) 
"""


def numIslands(grid):
    
    total_num = 0
    
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
                total_num = total_num + dfs(grid,i,j)
                
    return total_num

def dfs(grid, i, j):
    
    #boundary checking to make pointers dont go out of matrix
    
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j] == '0':
        return 0
    else:
        
        grid[i][j] = '0'     #sink the island
        dfs(grid,i+1,j) #go down
        dfs(grid,i,j+1) #go right
        dfs(grid,i,j-1) #go left
        dfs(grid,i-1,j) #go up
        
        return 1 
    

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(numIslands(grid))

grid1 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(numIslands(grid1))