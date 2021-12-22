# Day 8 of Advent of Code 2021
# Completed by cho on December 20, 2021


class Seg():
    '''
    Models a number Segment on the submarine's display.
    '''
    
    def __init__(self):
        self.letter = '.'
        self.on = False
    
    def update_letter(self, new):
        '''
        S.update_letter(str) 
        Sets this Segment's letter to the given new letter.
        '''
        self.letter = new
    
    def turn_on(self):
        '''
        S.turn_on()
        Sets this Segment's on property to True.
        '''
        self.on = True
    
    def turn_off(self):
        '''
        S.turn_off()
        Sets this Segment's on property to False.
        '''        
        self.on = False
    
    def __str__(self):
        '''
        str(S) --> str
        Returns this Segment's letter if this Segment is "on", or returns "." otherwise.
        '''
        if self.on:
            return self.letter
        else:
            return '.'
        

class Dig():
    '''
    Models a numerical Digit on the submarine's display, made up of Segments.
    '''
    
    def __init__(self, seg1, seg2, seg3, seg4, seg5, seg6, seg7):
        
        self.seg1 = seg1
        self.seg2 = seg2
        self.seg3 = seg3
        self.seg4 = seg4
        self.seg5 = seg5
        self.seg6 = seg6
        self.seg7 = seg7


    def reset(self):
        '''
        D.reset() 
        Sets all of this Digit's Segments to 'off'.
        '''
        self.seg1.turn_off()
        self.seg2.turn_off()
        self.seg3.turn_off()
        self.seg4.turn_off()
        self.seg5.turn_off()
        self.seg6.turn_off()
        self.seg7.turn_off()     
    

    def __str__(self):
        '''
        str(D) --> str
        Returns the integer value (0-9) of which this Digit represents.
        '''
        
        if self.seg1.on and self.seg2.on and self.seg3.on and self.seg4.on and self.seg5.on and self.seg6.on and self.seg7.on:
            return '8'
        
        elif self.seg1.on and self.seg2.on and self.seg3.on and self.seg5.on and self.seg6.on and self.seg7.on:
            return '0'
        
        elif self.seg1.on and self.seg2.on and self.seg4.on and self.seg5.on and self.seg6.on and self.seg7.on:
            return '6'
        
        elif self.seg1.on and self.seg2.on and self.seg3.on and self.seg4.on and self.seg6.on and self.seg7.on:
            return '9'        
        
        elif self.seg1.on and self.seg3.on and self.seg4.on and self.seg5.on and  self.seg7.on:
            return '2'        
        
        elif self.seg1.on and self.seg2.on and self.seg4.on and self.seg6.on and self.seg7.on:
            return '5'        

        elif self.seg1.on and self.seg3.on and self.seg4.on and self.seg6.on and self.seg7.on:
            return '3'

        elif self.seg2.on and self.seg3.on and self.seg4.on and self.seg6.on:
            return '4'

        elif self.seg1.on and self.seg3.on and self.seg6.on:
            return '7'
        
        elif self.seg3.on and self.seg6.on:
            return '1'        



def part_1():
    '''
    part_1()
    Prints the number of times that the digits 1, 4, 7, or 8 appear in all the output values.
    '''
    
    f = open('input.txt')
    
    entries = []
    
    for line in f:
        line = line.strip().split()
        entries.append(line)
        
    f.close()
    
    num_occurences = 0
    
    for e in entries:
        
        for i in range(len(e)):
            
            if i > 10:
                
                if len(e[i]) == 2 or len(e[i]) == 4 or len(e[i]) == 7 or len(e[i]) == 3:
                    num_occurences += 1
                    
    print(num_occurences)
    
    

def part_2():
    '''
    part_2()
    Prints the sum of all the output values.
    '''
    
    f = open('input.txt')
    
    entries = []
    
    for line in f:
        line = line.strip().split()
        entries.append(line)
        
    f.close()
    
    sum_nums = 0
    
    for e in entries:
        
        letter_occurences = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0}
        corresponding_segs = {}
        
        seg1 = Seg()
        seg2 = Seg()
        seg3 = Seg()
        seg4 = Seg()
        seg5 = Seg()
        seg6 = Seg()
        seg7 = Seg()

        for i in range(len(e)):
            
            if i < 10:
                
                for letter in e[i]:
                    letter_occurences[letter] += 1            
                
                if len(e[i]) == 2:
                    segs_1 = list(e[i])
                    
                elif len(e[i]) == 3:
                    segs_7 = list(e[i])
            
                elif len(e[i]) == 4:
                    segs_4 = list(e[i])
 
  
        for item in segs_7:
            if item not in segs_1:
                seg1.update_letter(item)
                corresponding_segs[item] = seg1
        
        
        s_6 = list(letter_occurences.keys())[list(letter_occurences.values()).index(9)]
        seg6.update_letter(s_6)
        corresponding_segs[s_6] = seg6
        
        
        segs_1.remove(s_6)
        s_3 = segs_1[0]
        seg3.update_letter(s_3)
        corresponding_segs[s_3] = seg3
        
        
        s_2 = list(letter_occurences.keys())[list(letter_occurences.values()).index(6)]
        seg2.update_letter(s_2)
        corresponding_segs[s_2] = seg2
        
        
        s_5 = list(letter_occurences.keys())[list(letter_occurences.values()).index(4)]
        seg5.update_letter(s_5)
        corresponding_segs[s_5] = seg5
        
        
        segs_4.remove(s_3)
        segs_4.remove(s_2)
        segs_4.remove(s_6)
        
        s_4 = segs_4[0]
        seg4.update_letter(s_4)
        corresponding_segs[s_4] = seg4
        
        
        letter_occurences[s_4] = 0
        s_7 = list(letter_occurences.keys())[list(letter_occurences.values()).index(7)]
        seg7.update_letter(s_7)
        corresponding_segs[s_7] = seg7
        
        #dig = f' {str(seg1)*4} \n{seg2}    {seg3}\n{seg2}    {seg3}\n {str(seg4)*4} \n{seg5}    {seg6}\n{seg5}    {seg6}\n {str(seg7)*4} '   
        
        this_dig = Dig(seg1, seg2, seg3, seg4, seg5, seg6, seg7)
        d_str = ""
        
        for d in e[11:]:
            
            for letter in d:
                corresponding_segs[letter].turn_on()
                
            d_str += str(this_dig)
            this_dig.reset()
        
        sum_nums += int(d_str)
        
    print(sum_nums)
    
    
if __name__ == "__main__":
    part_1()
    part_2()