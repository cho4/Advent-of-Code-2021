# Day 1 of Advent of Code 2021
# Completed by cho on December 1, 2021

def part_1():
    '''
    part_1()
    Prints the number of measurements that are larger than the previous measurement.
    '''
    file = open('input.txt')
    
    num_larger = 0
    counter = 0
    
    prev = int(file.readline().strip())
    
    for line in file:
        counter += 1
        line = line.strip()
        
        if int(line) > prev:
            num_larger += 1
            
        prev = int(line)
    
    file.close()        
    print(num_larger)


def part_2():
    '''
    part_2()
    Prints the number of measurement sums that are larger than the previous sum.
    '''
    file = open('input.txt')
    
    num_larger = 0
    input_list = []
    
    for line in file:
        line = int(line.strip())
        input_list.append(line)
        
    file.close()
    
    prev = sum(input_list[0:3])
    input_list.remove(input_list[0])
    
    for i in range(len(input_list)):
        
        #print(f'{input_list[i:i+3]} --> {sum(input_list[i:i+3])}') Debugging
        
        if sum(input_list[i:i+3]) > prev:
            num_larger += 1
        
        prev = sum(input_list[i:i+3])
        
    print(num_larger)
    
if __name__ == "__main__":
    part_1()
    part_2()