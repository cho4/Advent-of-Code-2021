# Day 4 of Advent of Code 2021
# Completed by cho on December 7, 2021

class Tile():
    '''
    Models a Bingo Tile.
    '''
    
    def __init__(self, number):
        self.number = number
        self.called = False

    def toggle(self):
        '''
        T.toggle() --> bool
        Toggle this Tile's called attribute to True.
        '''
        self.called = True
    
    def __lt__(self, other):
        '''
        T < Tile --> bool
        Returns True if this Tile's called attribute is False and the other 
        Tile's is True or returns False otherwise.
        '''
        return self.called < other.called
    
    def __gt__(self, other):
        '''
        T > Tile --> bool
        Returns True if this Tile's called attribute is True and the other 
        Tile's is False or returns False otherwise.
        '''
        return self.called > other.called
    
    def __eq__(self, other):
        '''
        T == Tile --> bool
        Returns True if this Tile's called attribute is equal to the other Tile's,
        or returns False otherwise.
        '''
        return self.called == other.called
        
    
    def __str__(self):
        '''
        str(T) --> str
        Returns this Tile's number as a string.
        '''
        return self.number
    
    def __repr__(self):
        '''
        repr(T) --> str
        Returns this Tile's number as a string (to be displayed when a list of Tiles is printed)
        '''
        return self.number
    
    
class Board():
    '''
    Models a Bingo Board with Tiles
    '''
    
    def __init__(self, tiles_list):
        self.tiles_list = tiles_list
        self.oned_list = tiles_list[0] + tiles_list[1] + tiles_list[2] + tiles_list[3] + tiles_list[4]
        self.oned_val_list = []
        
        for item in self.oned_list:
            self.oned_val_list.append(item.number)

    
    def call(self, num):
        '''
        B.call(str) --> bool
        "Calls" the given bingo number and checks to see if a bingo has been achieved.
        Returns True if a bingo has been achieved or False otherwise.
        '''
        
        if num in self.oned_val_list:
            
            self.tiles_list[self.oned_val_list.index(num) // 5][self.oned_val_list.index(num) % 5].toggle()
            
            for line in self.tiles_list:

                if min(line).called == True:
                    return True
                
                
            for i in range(5):
                
                temp = []
                
                for line in self.tiles_list:
                    temp.append(line[i])
                
                if min(temp).called == True:
                    return True
                
        return False
           
            
    def __str__(self):
        '''
        str(B) --> str
        Returns a string representation of this Bingo Board.
        '''
        string = ""
        
        for line in self.tiles_list:
            
            for num in line:
                
                string += f"{num} "
                
            string += "\n"
        
        return string
    
   
def part_1():
    '''
    part_1()
    Prints the final score of the bingo board that wins first.
    '''
    
    file = open('input.txt')
    
    boards = []
    nums = file.readline().split(',')
    
    for k in range(100): # Hardcoded this since I didn't want to loop through the file and extra time to see how many lines there 
        file.readline()
        temp = []
        
        for i in range(5):
            temp_line = file.readline().split()
            
            for n in range(5):
                temp_line[n] = Tile(temp_line[n])
                
            temp.append(temp_line)
        
        boards.append(Board(temp))
    
    file.close()
    
    for num in nums:
        
        for board in boards:
            
            bingo = board.call(num)
            
            if bingo:
                break
            
        if bingo:
            break
        
    if bingo:
        
        total = 0
        for val in board.oned_list:
            
            if val.called == False:
                total += int(val.number)
               
        print(int(num) * total)


def part_2():
    '''
    part_2()
    Prints the final score of the bingo board that wins last.
    '''
    file = open('input.txt')
    
    boards = []
    nums = file.readline().split(',')
    
    for k in range(100):
        file.readline()
        temp = []
        
        for i in range(5):
            temp_line = file.readline().split()
            
            for n in range(5):
                temp_line[n] = Tile(temp_line[n])
                
            temp.append(temp_line)
        
        boards.append(Board(temp))
    
    file.close()
    
    for num in nums:
    
        i = 0
        
        while i < len(boards):
    
            bingo = False
            bingo = boards[i].call(num)
            
            if bingo:
    
                recent_bingo = boards[i]
                winning_num = num
                boards.remove(boards[i])
            
            else:
                i += 1

    total = 0
    
    for val in recent_bingo.oned_list:
        
        if val.called == False:
            total += int(val.number)
           
    print(int(winning_num) * total)

if __name__ == "__main__":
    part_1()
    part_2()