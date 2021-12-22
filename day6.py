# Day 6 of Advent of Code 2021
# Completed by cho on December 19, 2021

from collections import deque
    
def day_6(part):
    '''
    day_6(int)
    Prints the population of lanternfish after a certain amount of days. Given the
    integer 1 (for part 1), population will be calculated from 80 days of growth,
    given the integer 2 (for part 2), population will be calculated from 256 days,
    else, a custom amount of days will be inputted by the user.
    '''
    
    if part == 1:
        days = 80
        
    elif part == 2:
        days = 256
    
    else:
        days = int(input('Enter number of days: '))
    
    f = open('input.txt')
    fishes = f.readline().strip().split(',')
    f.close()
    
    fs = [0,0,0,0,0,0,0]
    
    for i in fishes:
        fs[int(i)] += 1
    
    queue = [0,0,0]
    
    for day in range(days):
    
        temp = deque(fs)
        temp.rotate(-1)
        fs = list(temp)
    
        queue += [fs[0]]
        fs[6] += queue.pop(0)
        
    print(sum(fs) + queue[0] + queue[1])


if __name__ == "__main__":
    day_6(1)
    day_6(2)


# ----- INITIAL PART 1 SOLUTION (VERY INEFFICIENT) ------

#def fish_tally(fishes):
    
    #sum_fish = len(fishes) 
    
    #for fish_timer in fishes: 
        
        #fish_timer = int(fish_timer)
        
        #for day in range(0, -fish_timer + 256, 7): 
          
            #birthday = day + fish_timer + 1 
            #initial = birthday % 7 + 2 # 
  
            #if initial == 7:
                #initial = 0
                
            #if initial == 8:
                #initial = 1
           
            #sum_fish += fish_tally_helper(initial, birthday)
        
        #print(f'{sum_fish}')
        
    #return sum_fish


#def fish_tally_helper(timer, bday):

    #f_sum = 1
    
    #for day in range(-timer + bday + 1, -timer + 256, 7):
        
        #if day != -timer + bday + 1:
            #birthday = day + timer + 1
            
            #initial = birthday % 7 + 2
            #if initial == 7:
                #initial = 0
                
            #if initial == 8:
                #initial = 1
            
            #f_sum += fish_tally_helper(initial, birthday)
    
    #return f_sum


#print(fish_tally(fishes))