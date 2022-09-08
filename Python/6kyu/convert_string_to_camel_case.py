# DESCRIPTION:
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
#    "the-stealth-warrior" gets converted to "theStealthWarrior"
#    "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# REGULAR EXPRESSIONS ALGORITHMS STRINGS




#my solution
import re

def to_camel_case(text):
    #your code here
    if len(text) == 0:
        return text
    splitted_str = re.split(r'[-_!]', text)
    for i in range(len(splitted_str)):        
      if i > 0:
        joined_str += splitted_str[i].capitalize()
      else:
        joined_str = splitted_str[i]

    return joined_str