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
        
        Method extracts vowels b
        """
        self._vowel_dict = {'a': True, 'A': True,
                            'e':True, 'E': True,
                            'i':True, 'I':True,
                            'o': True, 'O': True,
                            'u': True, 'U':True}
        
        reverse_vowel_s = ''       
        final_soln = ''    
        s_list = list(s)
        print(s_list)
        
        for idx in range(0, len(s_list)):
            try:
                self._vowel_dict[s_list[idx]]
                reverse_vowel_s += s_list[idx]
            except KeyError:
                None
                
        reverse_vowel_s = reverse_vowel_s[::-1]
        
        vowel_idx = 0
        for idx in range(0,len(s_list)):
            try:
                self._vowel_dict[s_list[idx]]
                final_soln += reverse_vowel_s[vowel_idx]
                vowel_idx += 1
            except KeyError:
                final_soln += s_list[idx]
        
        return final_soln
        
    def reverseVowelsFaster(self,s):
        '''
        in-line replacement of letters in final_soln list that is initiated
        from s(list)
        '''
        self._vowel_dict = {'a': True, 'A': True,
                    'e':True, 'E': True,
                    'i':True, 'I':True,
                    'o': True, 'O': True,
                    'u': True, 'U':True}
                    
        final_soln = list(s)
        
        idx_vowel, idx = len(s)-1,0 
        while idx_vowel - idx > 0:

            try:
                self._vowel_dict[s[idx]]
                
                running = True
                while running:
                    try: 
                        self._vowel_dict[s[idx_vowel]]
                        final_soln[idx] = s[idx_vowel]
                        final_soln[idx_vowel] = s[idx]
                        running = False
                        idx_vowel -=1
                    except KeyError:
                        idx_vowel -= 1
                idx += 1
            except KeyError:
                idx += 1
                
        return ''.join(final_soln)
    
soln_obj = Solution()
string = 'blae bluh blagi'
print(string)
print(soln_obj.reverseVowelsFaster(string))





























