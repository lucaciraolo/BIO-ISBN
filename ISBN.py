
def find_missing_digit(input):
    total = 0
    question_pos = None
    for i in range(len(input)):
        # if number multiply by 10 - position and add to total
        character = input[i]
        if character.isdigit():
            total += (10 - i) * int(character)
        elif character.capitalize() == 'X':
            total += (10 - i) * 10
        elif character == '?':
            question_pos = i

    # Try all digits and see if it adds up to multiple of 11
    for i in range(11):
        if (total + (i * (10 - question_pos))) % 11 == 0:
            if question_pos == 9 and i == 10:
                return 'X'
            else:
                return i

    return False


def run_tests(dictionary):
    for input, expected in dictionary.items():
        result = find_missing_digit(input)
        if result == expected:
            passed = "Passed!"
        else:
            passed = "Failed!"
        print('Testing ISBN: {} Expected: {} Got: {} \t\t{}'.format(input, expected, result, passed))


if __name__ == "__main__":

    d = {
        "15688?111X": 1,
        "812071988?": 3,
        "020161586?": 'X',
        "?131103628": 0,
        "?86046324X": 1,
        "1?68811306": 5,
        "951?451570": 4,
        "0393020?31": 2,
        "01367440?5": 9
    }

    run_tests(d)
