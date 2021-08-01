# Porovnat dve skupiny zda obsahují stejné slova
# 1. Použít Set protože ignoruje obsažené duplikáty (na rozdíl od listu)
# 2. Procházet set1 po jednotlivých slovech a kontrolovat zda slovo obsahuje i druhý set. Pokud ne, nejsou stejné.
# 3. Pokud jsou nalezena všechna slova, jsou stejné

# Načtení dat ze souboru a context managers:
# https://book.pythontips.com/en/latest/context_managers.html

# Procházení dvou listů najednou v jednom cyklu pomocí metody zip()
# https://realpython.com/python-zip-function/


def compare_two():
    data = read_data("data.txt")
    compare(set(data[0]), set(data[1]))


def read_data(file):
    with open(file) as opened_file:
        my_data = []
        for line in opened_file.readlines():
            replaced = line.replace("\n", "")
            my_data.append(replaced.rsplit(","))
    return my_data


def prepare_data(data):
    data_len = len(data)
    my_list = []
    # Upraví všechny listy z načtených dat
    while data_len > 0:
        # Odstrani duplicity z Listu tím že ho převede na slovník, který automaticky zahodí duplicity, a slovník se zpět převede na List.
        temp_list = list(dict.fromkeys(data[data_len-1]))
        # Seřadí slovník pro porovnání v cyklu se zip
        temp_list.sort()
        my_list.append(temp_list)
        data_len -= 1
    return my_list


def compare_zip():
    data = read_data("data.txt")
    my_data = prepare_data(data)
    match = False
    for word1, word2 in zip(my_data[0], my_data[1]):
        if word1 != word2:
            print("Word", word1, "NOT found in both lists.")
            return match
        else:
            print("Word", word1, "found in both lists.")
    match = True
    print(match)
    return match


def compare(my_set1, my_set2):
    match = False
    for word in my_set1:
        if word in my_set2:
            print("Word", word, "found in the second set.")
        else:
            print("Word", word, "NOT found in the second set.")
            print("Sets contain same words: ", match)
            return match
    match = True
    print("Sets contain same words:", match)
    return match


# compare_two()
compare_zip()
