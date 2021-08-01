import hashlib

# Zjistit zda dva string obsajují stejná písmena - ve stejném počtu, nikoli v pořadí.
# Porovnání stringů -
# 1. Hash - https://www.pythoncentral.io/hashing-strings-with-python/
# 2. Délka
# 3. Typ a počet písmen ve slovech

word1 = "MOR"
word2 = "ROM"


def compare_words(my_word1, my_word2):
    if compare_words_hash(my_word1, my_word2):
        return True
    if len(my_word1) != len(my_word2):
        print("Len")
        return False
    letters1, letters2 = {}, {}
    for letter1, letter2 in zip(my_word1, my_word2):
        if letter1 in letters1:
            letters1.update({letter1: letters1["letter1"] + 1})
        else:
            letters1.update({letter1: 1})
        if letter2 in letters2:
            letters2.update({letter2: letters2["letter2"] + 1})
        else:
            letters2.update({letter2: 1})
    match = letters1 == letters2
    print(match)


def compare_words_hash(my_word1, my_word2):
    hash1 = hashlib.sha512(my_word1.encode())
    hash2 = hashlib.sha512(my_word2.encode())
    hex_dig1 = hash1.hexdigest()
    hex_dig2 = hash2.hexdigest()
    match = hex_dig1 == hex_dig2
    return match


compare_words(word1, word2)
