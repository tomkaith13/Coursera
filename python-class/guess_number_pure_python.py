'''
Created on Oct 22, 2013

@author: Bibin
'''
import random
import math



class Guess_game():
    ''' The class for starting each guess my number game '''
    computer_guess=0
    win=0
    
    def __calculate_player_guess(self):
            self.pguess=int(math.ceil(math.log((self.high - self.low + 1),2)))
            
    def __fill_comp_guess(self):
        self.computer_guess=random.randrange(self.low, self.high)
        
    def print_high(self):
        print 'the high allocated is ',self.high
    def print_low(self):    
        print 'the low allocated is ',self.low
                
    def print_pguess(self):         
        print 'the player chances',self.pguess
        
    def print_compguess(self):    
        print 'computer guess:',self.computer_guess
    
    def player_guess(self,guess):
        if self.pguess > 0:
            print 'this the player\'s  chance#',self.pguess
            if guess < self.computer_guess:
                print 'Higher'
            elif guess > self.computer_guess:
                print 'Lower'
            else:
                print 'You guessed right!! '
                self.win=1
                self.pguess=0
                pass    
            self.pguess = self.pguess - 1
        
            
               
    def __init__(self, low=0, high=100):
        self.low=low
        self.high=high        
        self.__fill_comp_guess()    
        self.__calculate_player_guess()
        

if __name__ == '__main__':
    g=Guess_game()
    
    g.print_high()
    g.print_low()
    chances=g.pguess
    print 'No of chances you have:',chances
    
    while chances > 0:
        p=int(raw_input('\n\nEnter your guess:'))
        g.player_guess(p)
        chances=g.pguess
        
    if g.win != 1:        
            print '\n\nYou have zero chances left'
            print 'The computer\'s number was:', g.computer_guess    
    
    
    
    print '\nGame Over !!'