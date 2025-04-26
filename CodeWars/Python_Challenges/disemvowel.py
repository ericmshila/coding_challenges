def disemvowel(string_):
    vowels = ['a','e','i','o','u','A','E','I','O','U','']
    processor = [char for word in string_ for char in word]
    no_vwl_list = [char for char in processor if char not in vowels]
    return ''.join(no_vwl_list)
    