# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:30:18 2016

@author: Mayank Shekhar
"""
import string

def build_shift_dict(shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        cipher = {}
        count = 0
        for i in lower[shift:len(lower)]:
            cipher[lower[count]] = i
            count += 1
        for i in lower[:shift]:
            cipher[lower[count]] = i
            count += 1
        count = 0
        for i in upper[shift:]:
            cipher[upper[count]] = i
            count += 1
        for i in upper[:shift]:
            cipher[upper[count]] = i
            count += 1
        return cipher