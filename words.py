# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                    must_start_with={"h", "y"})
def print_upper_words(words):
    '''Print each word on a seperate line, uppercased.

        >>> print_upper_words(["Programming", "is", "pretty", "fun"])
        PROGRAMMING
        IS
        PRETTY
        FUN
    '''
    for word in words:
        print(word.upper())

def print_upper_words2a(words):
    '''Print each word on a seperate line, uppercased, if the word begins with "E" or "e"

        >>> print_upper_words2(["eagle", "Edward", "Alfred"])
        EAGLE
        EDWARD
    '''
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def print_upper_words2b(words, char='e'):
    '''Print each word on a seperate line, uppercased, if the word begins with "E" or "e"

        >>> print_upper_words2(["eagle", "Edward", "Alfred"])
        EAGLE
        EDWARD
    '''
    for word in words:
        if word.startswith(char) or word.startswith(char.upper()):
            print(word.upper())

def print_upper_words3(words,start_with):
    '''Print each word on a seperate line,uppercased, if it starts with one of the given characters (start_with),case-sensitive

    >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    '''
    for word in words:
        for char in start_with:
            if word.startswith(char):
                print(word.upper())