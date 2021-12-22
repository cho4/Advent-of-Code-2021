# Day 3 of Advent of Code 2021
# Completed by cho on December 4, 2021


def part_1():
    '''
    part_1()
    Prints the power consumption of the submarine.
    '''
    file = open('input.txt')

    gamma = ""
    epsilon = ""    
    reports = []
    
    for line in file:
        line = line.strip()
        reports.append(line)
    
    file.close()
    
    num_bits = len(reports[0])
    
    for i in range(num_bits):
        
        num_0s = 0
        num_1s = 0
        
        for num in reports:
            
            if num[i] == '0':
                num_0s += 1
                
            else:
                num_1s += 1
        
        if num_0s > num_1s:
            gamma += '0'
            epsilon += '1'
            
        else:
            gamma += '1'
            epsilon += '0'
            
    print(int(gamma, 2) * int(epsilon, 2))



def part_2():

    file = open('input.txt')
    
    inputs = []
    
    for line in file:
        line = line.strip()
        inputs.append(line)
        
    
    num_bits = len(inputs[0])
    
    for i in range(num_bits):
        
        if len(inputs) == 1:
            break
        
        num_0s = 0
        num_1s = 0
        
        for num in inputs:
            
            if num[i] == '0':
                num_0s += 1
                
            else:
                num_1s += 1
               
        if num_0s <= num_1s:
            
            new = []
            
            for num in inputs:
                if num[i] == '0':
                    new.append(num)
                    
            inputs = new
            
        else:
            new = []
            
            for num in inputs:
                if num[i] == '1':
                    new.append(num)
                    
            inputs = new        
        
    print(inputs)
    

if __name__ == "__main__":
    part_1()
    part_2()