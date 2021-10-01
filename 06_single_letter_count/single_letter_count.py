def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    counter = 0
    for ltr in word.lower():
        if letter == ltr:
            counter += 1
    return counter
    
    # SB Solution:
    # return word.lower().count(letter.lower())


