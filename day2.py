# Day 2 of Advent of Code 2021
# Completed by cho on December 2, 2021

def part_1():
    '''
    part_1()
    Prints the product of the submarine's final horizontal position and depth.
    '''
    file = open('input.txt')
    
    hor = 0
    vert = 0
    
    for line in file:
        
        line = line.split()
    
        if line[0] == 'down':
            vert += int(line[1])
        
        elif line[0] == 'up':
            vert -= int(line[1])       
            
        else:
            hor += int(line[1])    
            
    file.close()
    print(hor * vert)    
    
    
def part_2():
    '''
    part_2()
    Prints the product of the submarine's final horizontal position and depth,
    with the submarine's aim taken into consideration.
    '''
    file = open('input.txt')
    
    hor = 0
    vert = 0
    aim = 0
    
    for line in file:
        
        line = line.split()
    
        if line[0] == 'down':
            aim += int(line[1])
        
        elif line[0] == 'up':
            aim -= int(line[1])       
            
        else:
            hor += int(line[1])    
            vert += (aim * int(line[1]))
            
    file.close()
    print(hor * vert)


if __name__ == "__main__":
    part_1()
    part_2()