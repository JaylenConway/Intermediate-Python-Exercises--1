def count_letters(input_string):
    letter_count = {}
    input_string = input_string.lower()
    for letter in input_string:
        if letter != ' ':
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

input_string = input('Enter a string: ')
letter_count = count_letters(input_string)
print(letter_count)