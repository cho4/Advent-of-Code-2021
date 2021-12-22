# Day 7 of Advent of Code 2021
# Completed by cho on December 20, 2021

def day_7(part):
    '''
    day_7(int)
    Determines the horizontal position that the crabs can align to using the 
    least fuel possible and prints that amount of fuel. 
    '''
    
    f = open('input.txt') 
    crab_positions = f.readline().strip().split(',')
    f.close()
    
    for i in range(len(crab_positions)):
        crab_positions[i] = int(crab_positions[i])
    
    largest = max(crab_positions)
    smallest = min(crab_positions)
    
    smallest_amount_fuel = 999999999999999999999999999999999999
    
    for i in range(smallest, largest + 1):
        
        fuel_used = 0
        
        for pos in crab_positions:
            
            if part == 1:
                fuel_used += abs(pos - i)
                
            elif part == 2:
                temp_fuel_used = abs(pos - i)
                fuel_used +=  (temp_fuel_used / 2) * (1 + temp_fuel_used)
            
        if fuel_used < smallest_amount_fuel:
            smallest_amount_fuel = fuel_used
    
    print(smallest_amount_fuel)


if __name__ == "__main__":
    day_7(1)
    day_7(2)