input = '15688?111X'

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


for i in range(10):
    if (total + (i * question_pos)) % 11 == 0:
        print('missing digit is', i)
        break

