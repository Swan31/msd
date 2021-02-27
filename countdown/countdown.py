def get_user_input():
    """Function which retrieves user input and verify that it is a non-zero natural number
    :returns Verified number given by user
    :rtype: Integer
    """
    number = None
    while number is None:
        user_input = input("Enter a non-zero natural number:")
        try:
            number = int(user_input)
            if number < 0:
                print(f"Given input {user_input} a negative number, not natural number!")
                number = None
            elif number == 0:
                print(f"Given input is {user_input}. While zero may be considered a natural number"
                      f" we cannot play countdown with it. Try it again.")
                number = None
        except ValueError:
            print(f"Given input {user_input} is not a non-zero natural number!")
    print(f"You have successfully entered number {number}. Let's play countdown!")
    return number

def number_divisible_by_divisor(dividend, divisor):
    """Returns true if number is divisible by divisor.
    :param dividend: number to be divided
    :param divisor: dividing number
    :returns True if dividend is divisible by divisor, else False
    :rtype Boolean
    """
    return dividend % divisor == 0

def countdown():
    """Function counts backwards from value provided by user to 1 and prints:
    “Agile” if the number is divisible by 5, “Software” if the number is divisible by 3,
    “Testing” if the number is divisible by both, or prints just the number if none of those cases are true."""
    user_number = get_user_input()
    while user_number > 0:
        div3 = number_divisible_by_divisor(user_number, 3)
        div5 = number_divisible_by_divisor(user_number, 5)
        if div3:
            if div5:
                print("Testing")
            else:
                print("Software")
        elif div5:
            print("Agile")
        else:
            print(user_number)
        user_number -= 1

countdown()