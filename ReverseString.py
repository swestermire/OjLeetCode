# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 07:49:45 2016

@author: swestermire
"""

class Solution(object):
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        self._vowel_dict = {'a': True, 'e':True, 'i':True, 'o': True, 'u': True}
        reverse_vowel_s = ''

        while len(s) > 0:
            if self._vowel_dict[s[-1]]:
                reverse_vowel_s += s[-1]
                s.remove(-1)
            else:
                reverse_vowel_s += s[0]
                s.pop(0)
                
        return reverse_vowel_s
    
soln_obj = Solution()
string = 'hello'
print(soln_obj.reverseVowels(string))