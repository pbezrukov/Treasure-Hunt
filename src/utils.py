def next_game():
    """Starting new game or exit"""
    answer = input("Do you want play again? Yes(Y) or No(N)? ")
    if answer == "Y" or answer == "y":
        return True
    elif answer == "N" or answer == "n":
        return False


def validate(r):
    """Check input data"""
    try:
        if len(r) == 5:
            for number in r:
                if number not in range(11, 56):
                    raise ValueError
        else:
            raise ValueError

    except ValueError:
        print("Please, format should be five rows of five numbers between 11 and 55")
    else:
        return True


def open_file(file_name):
    """Read file in list"""
    with open(file_name) as file:
        lines = [row.strip() for row in file]
    return lines
