# Day 9 of Advent of Code 2021
# Completed by cho on December 21, 2021


class Tile():
    '''
    Models a Tile on the heightmap.
    '''
    
    all_tiles = []
    
    def __init__(self, lvl, t_type, claimed=False):
        
        self.lvl = int(lvl)
        self.t_type = t_type
        self.is_deep = False
        self.claimed = claimed
        Tile.all_tiles.append(self)


    def __le__(self, other):
        '''
        T <= Tile --> bool
        Returns True if this Tile's level is less than or equal to the other 
        Tile's level, or False otherwise.
        '''
        return self.lvl <= other.lvl    
    
    
    def __ge__(self, other):
        '''
        T >= Tile --> bool
        Returns True if this Tile's level is greater than or equal to the other 
        Tile's level, or False otherwise.
        '''        
        return self.lvl >= other.lvl     


    def __str__(self):
        
        if self.t_type == 'border':
            return ' '
        
        elif self.is_deep:
            return 'D'    

        else:
            if self.claimed:
                return 'C'
            else:
                return str(self.lvl)
            
        
    def __repr__(self):
        
        if self.t_type == 'border':
            return ' '
        
        elif self.is_deep:
            return 'D'
        
        else:
            if self.claimed:
                return 'C'
            else:
                return str(self.lvl)


def __grid_str(grid):
    
    g_str = ""
    
    for row in grid:
        
        for col in row:
            g_str += ' ' + str(col)
            
        g_str += '\n'
        
    return g_str

def __is_sublist(l1, l2):
    
    if all(a in l2 for a in l1):
        return l2
    
    else:
        return None


def __dictionary_index(basins, tl):
    
    vals = list(basins.values())    
    
    for v in vals:
        
        result = __is_sublist(tl, v)
        
        if result != None:
            return list(basins.keys())[list(basins.values()).index(result)]
    
    return None


def __claim_surroundings(x, y, tile, grid, basins):
    
    tiles_claimed = []
    
    key = __dictionary_index(basins, [tile])
    
    if grid[y-1][x].t_type != 'border' and not grid[y-1][x].claimed:
        basins[key].append(grid[y-1][x])
        grid[y-1][x].claimed = True
        tiles_claimed.append([y-1, x])
        
    if grid[y+1][x].t_type != 'border' and not grid[y+1][x].claimed:
        basins[key].append(grid[y+1][x])
        grid[y+1][x].claimed = True
        tiles_claimed.append([y+1, x])
        
    if grid[y][x-1].t_type != 'border' and not grid[y][x-1].claimed:
        basins[key].append(grid[y][x-1])
        grid[y][x-1].claimed = True
        tiles_claimed.append([y, x-1])
        
        
    if grid[y][x+1].t_type != 'border' and not grid[y][x+1].claimed:
        basins[key].append(grid[y][x+1])
        grid[y][x+1].claimed = True    
        tiles_claimed.append([y, x+1])
    
    return tiles_claimed


def day_9(part):
    '''
    day_9(int)
    Part 1 prints the sum of the risk levels of all low points on the heightmap.
    Part 2 prints the product of the sizes of the 3 largest basins on the heightmap.
    '''
    
    f = open('input.txt')
    grid = []
    num_line = 0
    
    for line in f:
        
        line = list(line.strip())
        
        if num_line == 0:
            
            temp = []
            
            for n in range(len(line) + 2):
                temp.append(Tile(10, 'border'))
                
            grid.append(temp)
                
        
        for i in range(len(line)):
     
            if line[i] == '9':
                line[i] = Tile(line[i], 'border')
            
            else:
                line[i] = Tile(line[i], 'normal')
            
    
        line.insert(0, Tile(10, 'border'))
        line.append(Tile(10, 'border'))
        grid.append(line)
        num_line += 1
     
    f.close()
    grid.append(temp)
    
    
    for y in range(len(grid)):
        
        for x in range(len(grid[0])):
            
            tile = grid[y][x]
            
            if tile.t_type != 'border':
    
                lowest = True
                
                if lowest and grid[y-1][x] <= tile:
                    lowest = False
                    
                if lowest and grid[y+1][x] <= tile:
                    lowest = False
                    
                if lowest and grid[y][x-1] <= tile:
                    lowest = False
                    
                if lowest and grid[y][x+1] <= tile:
                    lowest = False
                
                if lowest:
                    tile.is_deep = True
                    
    
    if part == 1:
        total_risk = 0
        
        for t in Tile.all_tiles:
            
            if t.is_deep:
                total_risk += t.lvl + 1
        
        print(total_risk)      
        
    else:
        
        num_basins = 0
        basins = {}
        
        for t in Tile.all_tiles:
            
            if t.is_deep:
                num_basins += 1
                t.claimed = True
                basins[str(num_basins)] = [t]
        
        claimed = []
        
        for y in range(len(grid)):
            
            for x in range(len(grid[0])):
                
                tile = grid[y][x]
                
                if tile.is_deep == True:
                    claimed += __claim_surroundings(x, y, tile, grid, basins)
        
        
        while len(claimed) > 0:
            
            c_temp = []
            
            for t in claimed:
                c_temp += __claim_surroundings(t[1], t[0], grid[t[0]][t[1]], grid, basins)
            
            claimed = c_temp
            
        lens = []
        
        for key in basins:
            lens.append(len(basins[key]))
        
        lens.sort()
        print(lens[-1] * lens[-2] * lens[-3])



if __name__ == "__main__":
    day_9(1)
    day_9(2)