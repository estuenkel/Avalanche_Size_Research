import math
from sympy import factorint

def left_right_factors(n):
    factorization = factorint(n)
    
    if 2 in factorization:
        factorization.pop(2)
        
    global left, right
    limit = math.sqrt(2 * n)
    
    left = 1
    right = n
    
    def choose_factors(factorization, odd):
        global left, right
        
        for i in factorization:
            
            if odd * i < limit and odd * i > left:
                left = odd * i
            elif odd * i > limit and odd * i < right:
                right = odd * i
                
                
            if odd * i < limit:
                copy = factorization.copy()
                
                if copy[i] == 1:
                    copy.pop(i)
                else:
                    copy[i] = copy[i] - 1
                
                choose_factors(copy, odd * i)
    
    choose_factors(factorization, 1)
        
    L_left = int(n / left + (left - 1) / 2)
    L_right = int(n / right + (right - 1) / 2)
    
    if L_left < L_right:
        return (left, right, "left", L_left)
    else:
        return (left, right, "right", L_right)