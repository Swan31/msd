# Zjistit zda dva string obsajují stejná písmena - ve stejném počtu, nikoli v pořadí.
# Porovnání stringů -
# 1. TODO: Hash - https://www.pythoncentral.io/hashing-strings-with-python/
# 2. TODO: Délka

word1 = "MOR"
word2 = "ROM"


# fjk
# fld
#
# ffk
# ffd
#
# fgfgf
# fdgf

def zip_it(my_word1, my_word2):
    result = zip(my_word1, my_word2)
    result_set = list(result)
    unzip_result = zip(*result_set)
    print(result_set)
    print(set(unzip_result))


def get_letters(word):
    letters = {}
    for letter in word:
        if letter in letters:
            letters.update({letter: letters["letter"] + 1})
        else:
            letters.update({letter: 1})
            # letters[letter] = 1
    return letters


def compare(my_word1, my_word2):
    letters1 = get_letters(my_word1)
    letters2 = get_letters(my_word2)
    print(letters1)
    print(letters2)
    match = letters1 == letters2
    print(match)


# compare(word1, word2)
zip_it(word1, word2)
