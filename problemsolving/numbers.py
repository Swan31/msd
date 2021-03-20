"""There two sets of numbers. The arrays have the same length. Sum of a pair of numbers, one from the fist set, the
other from the second, must be the same as target number. Fina all occurrences. If no exact match is found,
print all the closest matches found."""
setx = [-1, 3, 8, 2, 9, 5]
sety = [4, 1, 2, 10, 5, 20]
target = 24
matches = {}

# Sort the arrays.
# Count the last number from the second array (y) with the first number from the first array (x)
# If the sum is less or equal than the target, go to the next number from the array x.
# All sums with additional numbers from array y would be smaller, thus worse match with the target.
# If the sum is more or equal than the target, go to the next number from the array y.
# All sums with additional numbers from array x would be greater, thus worse match with the target.


def find_closest_match():
    setx.sort()
    sety.sort()
    i = len(sety)-1
    j = 0
    result_count = 1
    while (i >= 0) and (j <= (len(setx)-1)):
        sums = sety[i] + setx[j]
        diff = target - sums
        matches.update({result_count: {"sum": sums, "x": setx[j], "y": sety[i], "diff": diff}})
        if sums <= target:
            j += 1
        elif sums >= target:
            i -= 1
        result_count += 1
    results(result_count-1)


def results(result_count):
    exact_match = {}
    close_matches = {}
    min_diff = 1000000
    while result_count > 0:
        current_diff = matches[result_count]["diff"]
        if current_diff == 0:
            exact_match[len(exact_match)] = matches[result_count]
        elif current_diff <= min_diff and len(exact_match) == 0:
            if current_diff < min_diff:
                close_matches.clear()
            close_matches[len(close_matches)] = matches[result_count]
            min_diff = abs(current_diff)
        result_count -= 1
    if len(exact_match) != 0:
        print("Found exact matches:")
        print(exact_match)
    else:
        print("No exact matches found. Closest matches:")
        print(close_matches)


find_closest_match()
