f1 = open("input06.txt", "r")
f2 = open("output06.txt", "w")

r, h = [int(i) for i in f1.readline().strip().split()]
map = [i.strip() for i in f1.readlines()]

adj = []
for i in map:
    l1 = []
    for j in i:
        l1.append(j)
    adj.append(l1)

def diamond_search(grid, row, col, diamond):   # using the DFS method

    if(row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col]=="#"):
        return diamond
    
    if(grid[row][col] == "D"):
        diamond += 1

    grid[row][col] = "#"

    diamond = diamond_search(grid, row+1, col, diamond)
    diamond = diamond_search(grid, row-1, col, diamond)
    diamond = diamond_search(grid, row, col+1, diamond)
    diamond = diamond_search(grid, row, col-1, diamond)

    return diamond

max_diamond = 0
for row in range(r):
    for col in range(h):
        if(adj[row][col] == "." or adj[row][col] == "D"):
            diamond = diamond_search(adj, row, col, 0)
            max_diamond = max(max_diamond, diamond)

f2.write(f"{max_diamond}")

f1.close()
f2.close()