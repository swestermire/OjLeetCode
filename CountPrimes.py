# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:33:22 2016

@author: swestermire

Description:

Count the number of prime numbers less than a non-negative number, n.
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        
        Starting from 2 check to see divisibility.  Once it can no longer
        be divided, proceed to 3 and so forth, always checking to see if the next
        number is prime knowing the prime numbers before
        """
        prime_nums = [2]
        n_primes = set([])
        prime_num_sum = 0
        
        if n <= 1:
            return prime_num_sum
        else:
            for prime_num in prime_nums:
                
                running = True
                print('prime num is ' , prime_num)
                while running:
                    if n%prime_num == 0:
                        n_primes.add(prime_num)
                        n = n/prime_num
                    else:
                        running = False
                    
                if n == 1:
                    return len(n_primes)
                else:
                    print(prime_nums, n)
                    if self.check_prime(prime_nums) == n:
                        return len(n_primes)+1
                    else:
                        prime_nums.append(self.check_prime(prime_nums))
    
    
    def check_prime(self, prime_nums):
        '''
        returns the next prime number in the array
        '''
        
        num_check = prime_nums[-1]
        
        running = True
        while running:
            num_check += 1 #can change +1 to +2 I'm sure
            is_num_prime = True
            
            for prime_num in prime_nums:
                if num_check%prime_num == 0:
                    running = False
                    is_num_prime = False
            
            if is_num_prime:
                return num_check
            
soln_obj = Solution()
num = 5

print(soln_obj.countPrimes(num))
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        