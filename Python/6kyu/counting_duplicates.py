# DESCRIPTION:
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. 
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice





#my solution
def duplicate_count(text):
    import re
    
    s = re.sub(r'[^a-zA-Z0-9]','',text)
    s = sorted(s.lower())
    nb_rep_chars = 0
    flag = 0
    for i in range(len(s)):
        if i>0 and s[i] == s[i-1]:
            flag = 1
        elif flag == 1:
            nb_rep_chars += 1
            flag = 0
    if flag == 1:
        nb_rep_chars += 1
    return nb_rep_chars