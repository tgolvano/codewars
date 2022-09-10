# DESCRIPTION:

# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

# STRINGS # ALGORITHMS







# my solution

def first_non_repeating_letter(string):
    if len(string) <= 1:
        return string
   
    sorted_str = sorted(string.lower())
   
    not_rep_str = []
    flag_repeating = 0
    for i in range(1, len(string), 1):        
        if sorted_str[i-1] == sorted_str[i]:
            if flag_repeating == 0:
                flag_repeating = 1          
        else:
            if flag_repeating == 0:
                not_rep_str += sorted_str[i-1]
            if i == len(string) - 1:
                not_rep_str += sorted_str[i]
            flag_repeating = 0
            
    if len(not_rep_str) == 0:
        return ''
    
    not_rep_index = len(string)
    for i in range(len(not_rep_str)):
        n_not_rep_index = string.lower().find(not_rep_str[i])
        if n_not_rep_index < not_rep_index:
            not_rep_index = n_not_rep_index
    return string[not_rep_index]