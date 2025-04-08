def is_pangram(sentence):            
    import string
    alphabets = list(string.ascii_lowercase)
    sentence = sentence.lower().strip('.')
    not_found = []
    for i in alphabets:
        if i not in sentence:
            not_found.append(i)
    if not_found == []:
         return True
    return False


print(is_pangram(sentence='abcdefghijklmnopqrstuvwxyz'))