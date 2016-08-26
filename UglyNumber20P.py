# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 07:55:27 2016

@author: swestermire

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""

class Solution(object):
    def isUglyLong(self, num):
        """
        :type num: int
        :rtype: bool
        
        long solution - calculates all prime numbers and checks num based on prime numbers
        """
        prime_nums_ugly = set([2,3,5])
        prime_nums_other = set([7])
        
        if num <= 0:
            return False
        elif num == 1:
            return True
        
        ugly_bool = False
        for prime_num_ugly in prime_nums_ugly:
            if num%prime_num_ugly == 0:
                ugly_bool = True
        
        num_check = 8
        while num_check <= num:
            num_check_bool = True
            
            if ugly_bool == True:
                for prime_num_other in prime_nums_other:
                    if num_check%prime_num_other == 0:
                        num_check_bool = False
                        
            if num_check == num:
                if ugly_bool == False or num_check_bool == False:
                    return False
                else:
                    return True
                    
            if num_check_bool:
                for prime_num_ugly in prime_nums_ugly:
                    if num_check%prime_num_ugly == 0:
                        num_check_bool = False
                if num_check_bool == True:
                    prime_nums_other.add(num_check)            
            
            num_check += 1
            
        return ugly_bool
        
    
    def isUglyShorter(self, num):
        '''
        :type num: int
        :rtype: bool
        
        This divides the num by the ugly prime numbers and sees if the
        quotient evaluates to 1.  If it does, then there are no other
        prime numbers that can divide into num.  If the quotient is not 1, 
        it'll evaluate to a PRIME NUMBER!
        
        20% percentile
        '''
        
        prime_nums_ugly = set([2,3,5])
        
        if num <= 0:
            return False
            
        elif num == 1:
            return True
            
        else:
            for prime_num_ugly in prime_nums_ugly:
                running = True
                while running:
                    
                    if num%prime_num_ugly == 0:
                        num = num/prime_num_ugly
                    else:
                        running = False
                        
            if num == 1:
                return True
            else:
                return False
                

soln_obj = Solution()
num = -1
print('num is ' , num, ' ' , soln_obj.isUglyShorter(num))
            



                
                
                
                    
            
        
        
        