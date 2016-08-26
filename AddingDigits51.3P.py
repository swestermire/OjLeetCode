# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 07:55:27 2016

@author: swestermire

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution(object):
    def addDigitsLong(self, num):
        """
        :type num: int
        :rtype: int
        
        51.3% percentile
        """
        
        while True:
            str_num = str(num)
            sum = 0
            
            if len(str_num) == 1:
                return num
            else:
                for char in str_num:
                    sum += int(char)
                num = sum
                    
            
        
        
        