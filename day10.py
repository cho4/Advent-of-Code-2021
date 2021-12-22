# Day 10 of Advent of Code 2021
# Completed by cho on December 22, 2021


class Brack():
    '''
    Models a type of Bracket in the submarine's navigation system.
    '''
    
    def __init__(self, b_type):
        self.b_type = b_type
        
        if self.b_type == '[':
            self.opposite = ']'
            
        elif self.b_type == '{':
            self.opposite = '}'
            
        elif self.b_type == '<':
            self.opposite = '>'
            
        elif self.b_type == '(':
            self.opposite = ')'
        
    def __repr__(self):
        return self.b_type


def day_10(part):
    '''
    day_10(int)
    Part 1 prints the total syntax error score
    Part 2 prints the middle score of all the completion strings.
    '''
    
    f = open('input.txt')

    stack = []
    points = 0
    incomplete_lines = []
    
    for line in f:
            
        line = line.strip()
        invalid_found = False    
        i = 0
        stack.insert(0, Brack(line[i]))
        expecting = stack[0].opposite
        
        while i < len(line) - 1 and not invalid_found:
            
            i += 1
            current = line[i]
            
            if line[i] == '(' or line[i] == '<' or line[i] == '{' or line[i] == '[':
                stack.insert(0, Brack(line[i]))
                expecting = stack[0].opposite
                
                
            else:
                if line[i] == expecting:
                    stack.pop(0)
                    expecting = stack[0].opposite
                    
                else:
                    invalid_found = True
                    invalid_char = line[i]  
                    
        if invalid_found:
            
            if invalid_char == ')':
                points += 3
                
            elif invalid_char == ']':
                points += 57
                
            elif invalid_char == '}':
                points += 1197
                
            elif invalid_char == '>':
                points += 25137
                
        else:
            incomplete_lines.append(line)
    
    f.close()       
    
    if part == 1:
        print(points)
    
    elif part == 2:
        all_scores = []
        
        for line in incomplete_lines:
            
            stack = []
            i = 0
            stack.insert(0, Brack(line[i]))
            expecting = stack[0].opposite
            
            while i < len(line) - 1:
                
                i += 1
                current = line[i]
         
                if line[i] == '(' or line[i] == '<' or line[i] == '{' or line[i] == '[':
                
                    stack.insert(0, Brack(line[i]))
                    expecting = stack[0].opposite
                    
                    
                else:
                    
                    if line[i] == expecting:
                        stack.pop(0)
                        if len(stack) > 0:
                            expecting = stack[0].opposite
 
                    else:
                        invalid_found = True
                        invalid_char = line[i]  
        
            score = 0
            
            for char in stack:
                
                score *= 5
                
                if char.opposite == ')':
                    score += 1
                    
                elif char.opposite == ']':
                    score += 2
                    
                elif char.opposite == '}':
                    score += 3
                    
                elif char.opposite == '>':
                    score += 4
                    
            all_scores.append(score)
            
        all_scores.sort()
        print(all_scores[len(all_scores) // 2])


if __name__ == "__main__":
    day_10(1)
    day_10(2)