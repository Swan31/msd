"""Compare two words if the have the same characters in the same count regardless of their position in the word."""

""" Analysis:
1. Go through the string in a cycle and modify the word dictionary so that:
   a. If a character is not in the dictionary, add it with value 1
   b. If a character is in the dictionary, modify its value by 1 (add 1 to its value)
 2. Compare the two dictionaries and return the result
"""


def get_characters_from_string(word):
    """
    Gets different types and count of each character in given word.
    :param word: word (string)
    :return: dictionary where key is a character of the word and value is count of the character in the word.
    """
    characters = {}
    print(word)
    for x in word:
        print(x)
        if x in characters.keys():
            characters[x] = characters[x] + 1
        else:
            characters[x] = 1
    print(characters)
    return characters


def compare_words():
    """
    Compares two words given as input by a user.
    :return: True if words are a match, else False.
    """
    word1 = input("Enter first word:")
    word2 = input("Enter second word:")
    chars1 = get_characters_from_string(word1)
    chars2 = get_characters_from_string(word2)
    match = chars1 == chars2
    print("Given words are equal in number of characters:", match)
    return match


compare_words()
