# Funkce která vrátí druhé nejvyšší číslo v listu
# 1. Na začátku z prvních dvou čísel listu nastavit to vyšší jako nejvyšší a to menší jako druhé nejvyšší
# 2. Projít listem a pokud je dané číslo vyšší než nejvyšší, nastavit to dosud nejvyšší jako druhé nejvyšší a nové jako nejvyšší
# 3. Pokud je číslo vyšší než druhé nejvyšší, nastavit ho jako druhé nejvyšší

listN = [5, 4, 1]
listA = [1, 5, 4]


def numbers(my_list):
    highest = max(my_list[0], my_list[1])
    second_highest = min(my_list[0], my_list[1])
    for i in my_list:
        if i > highest:
            second_highest = highest
            highest = i
        elif second_highest < i < highest:
            second_highest = i
    print(second_highest)
    return second_highest


def numbers_sort(my_list):
    my_list.sort()
    print(my_list[-2])


numbers(listN)
numbers_sort(listN)
