"""In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead."""
def neighbours(r, c):
    return [[r,c+1],[r,c+1],[r-1,c],[r+1,c]]

def rottingOranges(arr):
    r = len(arr)
    c = len(arr[0])
    print(c)
    visited = False
    rottenlist = []
    adjacent =
    for i in range(r):
        for j in range(c):
            adjacent = neighbours(i,j)
            for adj in adjacent:




arr =[[2,1,1],[1,1,0],[0,1,1]]
rottingOranges(arr)