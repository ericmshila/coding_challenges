"""An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)"""

def isogram(string):
    string = string.lower()
    if string == "":
        return True
    char_list = [char for char in string.lower()]
    char_count= []
    for char in char_list:
        char_count.append(char_list.count(char))
    for any in char_count:
        if any > 1 :
            return False
    return True
            


print(isogram('thequickbrownfoxjumpsoverthelazydog'))