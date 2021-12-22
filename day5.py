# Day 5 of Advent of Code 2021
# Completed by cho on December 18, 2021


def day_5(part):
    '''
    day_5(int)
    Prints the number of points that at least two lines overlap. Given the
    integer 2 (representing part 2), diagonal lines will be considered, otherwise
    only vertical and horizontal lines will be considered.
    '''
    
    f = open('input.txt')
    
    used_points = {}
    
    for line in f:
        line = line.strip().split(' -> ')
        
        line[0] = line[0].split(',')
        line[1] = line[1].split(',')
        
        if line[0][0] == line[1][0]:
        # Vertical line
            
            x = int(line[0][0])
            
            for y in range(min(int(line[0][1]), int(line[1][1])), max(int(line[0][1]), int(line[1][1])) + 1):
                
                k = f'({x}, {y})'
                
                if k in used_points:
                    used_points[k] += 1
                
                else:
                    used_points[k] = 1
                    
    
        elif line[0][1] == line[1][1]:
        # horizontal line
            
            y = int(line[0][1])
        
            for x in range(min(int(line[0][0]), int(line[1][0])), max(int(line[0][0]), int(line[1][0])) + 1):
                
                k = f'({x}, {y})'
                
                if k in used_points:
                    used_points[k] += 1
                
                else:
                    used_points[k] = 1            
                     
        else:
        # Diagonal line
            
            if part == 2:
                if int(line[1][0]) > int(line[0][0]):
                    delta_x = 1
                else:
                    delta_x = -1
                    
                if int(line[1][1]) > int(line[0][1]):
                    delta_y = 1      
                else:
                    delta_y = -1
                    
                current_x = int(line[0][0])
                current_y = int(line[0][1])
                
                k = f'({current_x}, {current_y})'
                
                if k in used_points:
                    used_points[k] += 1
                
                else:
                    used_points[k] = 1         
                
                while current_x != int(line[1][0]) and current_y != int(line[1][1]):
                    current_x += delta_x
                    current_y += delta_y            
                    
                    k = f'({current_x}, {current_y})'
                    
                    if k in used_points:
                        used_points[k] += 1
                    
                    else:
                        used_points[k] = 1    
    
    f.close()
    
    num_intersect = 0
    
    for point, num in used_points.items():
    
        if num > 1:
            num_intersect += 1
            
    print(num_intersect)


if __name__ == "__main__":
    day_5(1)